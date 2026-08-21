import os
import json
import re
import subprocess
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import uvicorn
from dotenv import load_dotenv
from google.antigravity import Agent, LocalAgentConfig

# Attempt to load local project .env, then fallback to user's global WBW config
load_dotenv()
load_dotenv(os.path.expanduser("~/.wbw/.env"))

app = FastAPI(title="Geminisys Omni-Director")

# -----------------------------------------------------------------
# DATA LAYER (State Manager)
# -----------------------------------------------------------------
def load_json(filepath: str) -> dict:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    return {}

def save_json(filepath: str, data: dict):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def load_file(filepath: str) -> str:
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return f.read()
    return ""

def apply_state_update(update_payload: dict):
    """
    Parses dynamic updates like {"wounds": {"current": "+2"}} 
    and applies them to the character files.
    """
    for character_name, stats in update_payload.items():
        filepath = f"state/{character_name.lower()}.json"
        if not os.path.exists(filepath):
            continue
            
        char_data = load_json(filepath)
        
        # Apply deltas to derived_attributes safely
        for stat_type, change in stats.items():
            if stat_type in ["wounds_current", "strain_current"]:
                category, subcategory = stat_type.split("_")
                try:
                    current_val = char_data["derived_attributes"][category][subcategory]
                    # Evaluate the string math (e.g. "0" + "+2" = 2)
                    new_val = current_val + int(change)
                    char_data["derived_attributes"][category][subcategory] = max(0, new_val)
                    print(f"[STATE] Updated {character_name} {stat_type} by {change} (New: {new_val})")
                except KeyError:
                    pass
                    
        save_json(filepath, char_data)

# -----------------------------------------------------------------
# MEMORY / QUEUE
# -----------------------------------------------------------------
holding_pen = []

class ActionIntent(BaseModel):
    character: str
    action_text: str
    dice_result: Optional[str] = ""

# -----------------------------------------------------------------
# THE CIRCUIT BREAKER GM HOOK
# -----------------------------------------------------------------
async def ask_gm(prompt: str) -> str:
    api_key = os.environ.get("GEMINISYS_API_KEY") or os.environ.get("GEMINI_API_KEY")
    
    if api_key:
        try:
            print("[ENGINE] Attempting Fast API Route...")
            config = LocalAgentConfig(
                system_instructions=load_file("state/genesys_gm.md"),
                api_key=api_key
            )
            async with Agent(config) as agent:
                response = await agent.chat(prompt)
                full_text = ""
                async for token in response:
                    full_text += token
                return full_text
        except Exception as e:
            print(f"[ENGINE] Fast API Failed ({e}). Tripping Circuit Breaker...")
    else:
        print("[ENGINE] No API Key found. Defaulting to CLI pipe.")

    print("[ENGINE] Routing via Antigravity CLI (Expect 3-4s delay)...")
    env = os.environ.copy()
    env["TERM"] = "dumb"
    process = subprocess.Popen(
        ["agy", "--print", prompt, "--continue"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        env=env
    )
    stdout, _ = process.communicate()
    # Strip ANSI
    clean_text = re.sub(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])', '', stdout)
    return clean_text

# -----------------------------------------------------------------
# ENDPOINTS
# -----------------------------------------------------------------
@app.get("/api/state")
async def get_state():
    return {
        "warlock": load_json("state/warlock.json"),
        "luckii": load_json("state/luckii.json"),
        "campaign_state": load_file("state/current_state.md"),
        "holding_pen": [a.character for a in holding_pen]
    }

@app.post("/api/intent")
async def stage_intent(intent: ActionIntent):
    if intent.action_text.upper() in ["PASS", "INACTION"]:
        print(f"[{intent.character}] passed their turn.")
    holding_pen.append(intent)
    return {"status": "staged", "message": f"{intent.character} added to queue."}

@app.post("/api/resolve")
async def resolve_scene():
    global holding_pen
    if not holding_pen:
        return {"status": "error", "message": "Nothing in holding pen."}
    
    # 1. Build the massive injected prompt
    prompt = "CONTEXT:\n"
    prompt += "WARLOCK STATS: " + json.dumps(load_json("state/warlock.json")) + "\n"
    prompt += "LUCKII STATS: " + json.dumps(load_json("state/luckii.json")) + "\n"
    prompt += "SCENE: " + load_file("state/current_state.md") + "\n\n"
    
    prompt += "NEW PLAYER ACTIONS TO RESOLVE:\n"
    for action in holding_pen:
        prompt += f"[{action.character}]: {action.action_text}\n"
        if action.dice_result:
            prompt += f"(Rolled: {action.dice_result})\n"
            
    holding_pen = [] # Clear the queue
    
    # 2. Ask the GM
    raw_response = await ask_gm(prompt)
    
    # 3. THE INTERCEPTOR: Parse out the [STATE_UPDATE: {...}] block
    # We look for [STATE_UPDATE: followed by anything, ending with ]
    state_match = re.search(r'\[STATE_UPDATE:\s*(\{.*?\})\s*\]', raw_response, re.DOTALL)
    
    clean_narrative = raw_response
    if state_match:
        try:
            update_json = json.loads(state_match.group(1))
            apply_state_update(update_json)
            # Remove the ugly JSON block so the players don't see it
            clean_narrative = raw_response.replace(state_match.group(0), "").strip()
        except json.JSONDecodeError:
            print("[ERROR] GM output invalid JSON state update.")

    return {"status": "resolved", "narrative": clean_narrative}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
