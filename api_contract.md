# Geminisys API Contract (v2.0) - Multiplayer "Jackbox" Model

The backend runs a local server on `http://<HOST_IP>:8000`. It acts as the game engine and a "Holding Pen" for player actions.

---

## 1. GET `/api/state`
**Purpose:** Returns the current game state, including character sheets and the central narrative. 
**Frontend Usage:** Both the TV (Stage) and the Controllers (Phones/Laptops) should poll this endpoint every 2 seconds to keep the UI visually updated.

**Response (200 OK):**
```json
{
  "warlock": { ... },
  "luckii": { ... },
  "campaign_state": "The party is currently trapped in a cantina shootout...",
  "holding_pen": ["Warlock"] 
}
```
*(Note: `holding_pen` is a list of characters who have currently staged an action but haven't resolved yet. The UI can use this to show a "Ready" checkmark next to their name).*

---

## 2. POST `/api/intent`
**Purpose:** Sent by a Controller when a player wants to stage an action in the Holding Pen.

**Request Payload:**
```json
{
  "character": "Warlock",
  "action_text": "I vault the table and shoot the bounty hunter.",
  "dice_result": "2 Success, 1 Threat" 
}
```
*(Note: `dice_result` is optional. If left blank, it means they are just talking or doing something that doesn't require a roll. If a player is not participating in the current scene, they can submit an `action_text` of `"PASS"` or `"INACTION"` so the server knows they are ready and can auto-resolve).*

**Response (200 OK):**
```json
{ "status": "staged", "message": "Warlock's action is in the holding pen." }
```

---

## 3. POST `/api/resolve`
**Purpose:** Triggers the GM to take everything currently sitting in the Holding Pen, weave it together into a narrative, update the JSON files, and push the response to the `/api/state`.

**Request Payload:** 
*(Empty POST request. Any player can click the "Resolve Scene" button on their controller to trigger this).*
```json
{}
```

**Response (200 OK):**
```json
{ "status": "resolving", "message": "The GM is writing the narrative..." }
```
