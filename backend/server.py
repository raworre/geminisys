from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any, Optional

app = FastAPI(
    title="Geminisys Omni-Director API",
    description="Core API for interactions with the Genesys Omni Director",
    version="1.0.0",
    docs_url="/docs" # This gives us the free Swagger UI!
)

# Allow CORS for the local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models for our API ---
class PlayerIntent(BaseModel):
    character: str
    action_text: str

class PlayerRoll(BaseModel):
    character: str
    dice_result: str

# --- API Endpoints (Dummy Responses) ---

@app.get("/api/campaigns")
async def list_campaigns():
    """Get a collection of available game campaigns/states."""
    # Dummy response returning an empty array
    return []

@app.get("/api/campaigns/{campaign_id}")
async def get_campaign_by_id(campaign_id: str):
    """Get the current state of a campaign by its ID."""
    # Dummy response matching the GameState schema
    return {
        "scene_status": "INTENT_COLLECTION",
        "narrative_log": [
            "The blast doors hiss open, revealing the bounty hunter."
        ],
        "pending_rolls": {},
        "characters": [
            {"name": "Warlock", "wounds": 4},
            {"name": "Luckii", "wounds": 2}
        ]
    }

@app.get("/api/campaigns/{campaign_id}/characters/{character_id}")
async def get_character_by_id(campaign_id: str, character_id: str):
    """Get the current stats and details of a specific character."""
    # Dummy response
    return {
        "name": character_id.capitalize(),
        "species": "Human",
        "career": "Smuggler",
        "wounds": {"current": 2, "threshold": 12},
        "strain": {"current": 1, "threshold": 10}
    }

@app.post("/api/campaigns/{campaign_id}/intents", status_code=202)
async def submit_intent(campaign_id: str, intent: PlayerIntent):
    """Submit a text-based action."""
    # Dummy logic
    print(f"[{campaign_id}] Received intent from {intent.character}: {intent.action_text}")
    return {"message": "Intent successfully queued"}

@app.post("/api/campaigns/{campaign_id}/rolls", status_code=202)
async def submit_roll(campaign_id: str, roll: PlayerRoll):
    """Submit physical dice results."""
    # Dummy logic
    print(f"[{campaign_id}] Received roll from {roll.character}: {roll.dice_result}")
    return {"message": "Roll successfully queued"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
