# Geminisys: Backend Low-Level Design (LLD) & Task Tree

**Goal:** Provide a Playable MVP by Saturday Evening.
**Architecture Pattern:** Decoupled Client-Server. The Python Backend acts as the API Server and State Manager, driving a pure HTML/JS Frontend UI.

---

## 1. LOW-LEVEL ARCHITECTURE (LLD)

### A. The State Manager (Data Layer)
*   **Files as DB:** `genesys.schema.json` (model definitions), `{campaign_id}/warlock.json`, `{campaign_id}/luckii.json`, `{campaign_id}/current_state.md`.
*   **Logic:** A Python module (in `server.py` or `state.py`) that loads JSON/MD files into memory on boot. It provides methods to safely parse data through Pydantic models (from `models.py`) and write updates back to disk cleanly.
*   **State Machine Coordinator:** The state manager oversees the 4-Phase loop: `INTENT_COLLECTION` -> `POOL_ASSIGNMENT` -> `ROLL_COLLECTION` -> `RESOLUTION`. 

### B. The Scene Orchestrator (API Endpoints)
*(Note for Frontend/Luckii: The absolute source of truth for the API contract is the OpenAPI spec located at `api/omni-director-api.yaml`. Do not rely on legacy markdown contracts.)*
*   **Logic:** FastAPI endpoints (`/api/...`) that accept player intents and rolls.
*   **Process:**
    1. During `INTENT_COLLECTION`, accepts POSTs to `/api/campaigns/{id}/intents`. 
    2. Once all players have submitted their intents, transitions the state to `POOL_ASSIGNMENT`.
    3. Calls the Prompt Builder to ping Gemini for the required dice pools.
    4. Upon receiving the pools, updates state to `ROLL_COLLECTION` and exposes them in `/api/campaigns/{id}`.
    5. During `ROLL_COLLECTION`, accepts POSTs to `/api/campaigns/{id}/rolls`.
    6. Once all players have submitted their physical dice rolls, transitions to `RESOLUTION`.
    7. Pings Gemini with intents + rolls for a cinematic narrative outcome.
    8. Updates game state and loops back to `INTENT_COLLECTION`.

### C. The Context Injector (Prompt Pipeline)
*   **Logic:** A Python class (`PromptBuilder`) that constructs prompts for Gemini.
*   **Process:** 
    1. Reads character JSONs (`warlock.json`, `luckii.json`).
    2. Reads the campaign history (`current_state.md`).
    3. Bundles them into a hidden system prompt context payload.
    4. Appends the structured user intents (and optional rolls).
    5. Sends the combined prompt to the Gemini API (via Antigravity CLI/Python SDK).

### D. The Interceptor (Output Parser)
*   **Logic:** A Regex/JSON parser that catches the LLM's raw response before persisting it.
*   **Process:**
    1. Scans for `[STATE_UPDATE: {...}]`.
    2. If found, extracts the JSON, passes it to the `StateManager` to save character updates to disk, and strips the block from the text.
    3. Scans for `[MECHANICS: ...]`.
    4. Extracts mechanical impacts for the frontend UI to display as special callouts.
    5. Persists the clean narrative text to `current_state.md` and makes it available to the frontend.

---

## 2. DEPENDENCY TREE & TASK CHECKLIST

*Use this as the backend master roadmap. The Frontend (Phase 4 in previous planning) is entirely handled by Luckii in `FE_LLD.md`.*

### Phase 1: Foundation (Completed)
- [x] High-Level Design (HLD) & Concept Approval
- [x] Core JSON Schemas designed and formalized (`genesys.schema.json`)
- [x] Pydantic models auto-generated (`models.py`)
- [x] Initial FastAPI server scaffolding (`server.py`) with OpenAPI spec

### Phase 2: State Machine Logic (We are here)
- [ ] **Task 2.1: The 4-Phase Loop.** Implement state transitions in the backend (from `INTENT_COLLECTION` to `RESOLUTION`).
- [ ] **Task 2.2: StateManager File IO.** Ensure `update_wounds(character, amount)` and similar functions safely overwrite the character JSONs to disk.
- [ ] **Task 2.3: API Handlers.** fully implement `submit_intent` and `submit_roll` logic to check if all players are ready, triggering state transitions.

### Phase 3: Gemini Integration & Prompt Engineering
- [ ] **Task 3.1: The Master System Prompt.** Write the instructions that teach Gemini how to assign dice pools during `POOL_ASSIGNMENT`, resolve scenes during `RESOLUTION`, and output `[STATE_UPDATE]` blocks.
- [ ] **Task 3.2: SDK/CLI Hook.** Connect `PromptBuilder` to the Gemini API (via Antigravity Python SDK or `agy` CLI calls).
- [ ] **Task 3.3: Output Interceptor.** Write the Python logic/regex to extract `[STATE_UPDATE]` and `[MECHANICS]` blocks from Gemini's responses.

### Phase 4: Integration Testing (Terminal MVP)
- [ ] **Task 4.1: Terminal Mock Encounter.** Run a mock combat encounter entirely via raw API calls (e.g. `curl` or a test script) to prove the AI can assign pools, generate narrative, and auto-update the local JSON files. *(Proves Backend MVP)*

### Phase 5: UI Hookup & Polish (Saturday Morning)
- [ ] **Task 5.1: The Handshake.** Serve the endpoints to Luckii's Frontend UI.
- [ ] **Task 5.2: Network Tuning.** Test the 50-Foot HDMI/Mobile Hotspot setup for local VTT play.
- [ ] **Task 5.3: Playtest!**
