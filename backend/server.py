from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum
import json
import os

# Import the massive generated model
from models import GenesysCharacterSheet

app = FastAPI(
    title="Geminisys Omni-Director API",
    description="Core API for interactions with the Genesys Omni Director",
    version="1.0.0",
    docs_url="/docs"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models ---

class SceneStatus(str, Enum):
    INTENT_COLLECTION = "INTENT_COLLECTION"
    POOL_ASSIGNMENT = "POOL_ASSIGNMENT"
    ROLL_COLLECTION = "ROLL_COLLECTION"
    RESOLUTION = "RESOLUTION"

class PlayerIntent(BaseModel):
    character: str = Field(..., example="Warlock")
    action_text: str = Field(..., example="I vault the table and shoot the bounty hunter.")

class PlayerRoll(BaseModel):
    character: str = Field(..., example="Warlock")
    dice_result: str = Field(..., example="2 Success, 1 Threat")

class PendingRoll(BaseModel):
    pool: List[str] = Field(..., example=["Green", "Green", "Purple"])
    reason: str = Field(..., example="Ranged (Light) check.")

class CampaignSummary(BaseModel):
    model_config = {"populate_by_name": True}
    id: str
    link: str = Field(alias="_link")

class CharacterSummary(BaseModel):
    model_config = {"populate_by_name": True}
    id: str
    name: str
    link: str = Field(alias="_link")

class GameState(BaseModel):
    scene_status: SceneStatus
    narrative_log: List[str]
    pending_rolls: Dict[str, PendingRoll]
    characters: List[CharacterSummary]

class MessageResponse(BaseModel):
    message: str

# --- Helper Functions ---

def load_character(campaign_id: str, character_id: str) -> GenesysCharacterSheet:
    file_path = os.path.join("campaigns", campaign_id, f"{character_id}.json")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"Character {character_id} not found in campaign {campaign_id}")
    
    with open(file_path, "r") as f:
        data = json.load(f)
    
    # Parse the raw dictionary through the strict Pydantic model
    return GenesysCharacterSheet(**data)

# --- API Endpoints ---

@app.get("/api/campaigns", response_model=List[CampaignSummary])
async def list_campaigns(request: Request):
    """Get a collection of available game campaigns/states."""
    campaigns_dir = "campaigns"
    if not os.path.exists(campaigns_dir):
        return []
    
    found_campaigns = []
    for item in os.listdir(campaigns_dir):
        if os.path.isdir(os.path.join(campaigns_dir, item)):
            found_campaigns.append(
                CampaignSummary(
                    id=item,
                    link=str(request.url_for("get_campaign_by_id", campaign_id=item))
                )
            )
    return found_campaigns

@app.get("/api/campaigns/{campaign_id}", response_model=GameState)
async def get_campaign_by_id(campaign_id: str, request: Request):
    """Get the current state of a campaign by its ID."""
    
    # Generate character summaries (in a real app, you'd scan the directory for all .json files)
    char_summaries = []
    for char_id in ["warlock", "luckii"]:
        try:
            char_data = load_character(campaign_id, char_id)
            char_summaries.append(
                CharacterSummary(
                    id=char_id,
                    name=char_data.character_name if hasattr(char_data, "character_name") else char_id.capitalize(),
                    link=str(request.url_for("get_character_by_id", campaign_id=campaign_id, character_id=char_id))
                )
            )
        except HTTPException:
            pass

    if not char_summaries:
         raise HTTPException(status_code=404, detail="Campaign state not found")

    # Load the narrative log from current_state.md
    narrative_log = []
    state_path = os.path.join("campaigns", campaign_id, "current_state.md")
    if os.path.exists(state_path):
        with open(state_path, "r") as f:
            narrative_log = [p.strip() for p in f.read().split("\n\n") if p.strip()]

    return GameState(
        scene_status=SceneStatus.INTENT_COLLECTION,
        narrative_log=narrative_log if narrative_log else ["Awaiting GM initialization..."],
        pending_rolls={},
        characters=char_summaries
    )

@app.get("/api/campaigns/{campaign_id}/characters/{character_id}", response_model=GenesysCharacterSheet)
async def get_character_by_id(campaign_id: str, character_id: str):
    """Get the current stats and details of a specific character."""
    return load_character(campaign_id, character_id)

@app.post("/api/campaigns/{campaign_id}/intents", status_code=202, response_model=MessageResponse)
async def submit_intent(campaign_id: str, intent: PlayerIntent):
    """Submit a text-based action."""
    print(f"[{campaign_id}] Received intent from {intent.character}: {intent.action_text}")
    return MessageResponse(message="Intent successfully queued")

@app.post("/api/campaigns/{campaign_id}/rolls", status_code=202, response_model=MessageResponse)
async def submit_roll(campaign_id: str, roll: PlayerRoll):
    """Submit physical dice results."""
    print(f"[{campaign_id}] Received roll from {roll.character}: {roll.dice_result}")
    return MessageResponse(message="Roll successfully queued")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
