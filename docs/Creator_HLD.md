# Geminisys: Campaign & Character Creator HLD

## 1. Project Goal
Build a standalone, AI-assisted web tool (SPA Frontend + FastAPI Backend) to generate fully-formatted `campaign_setting.md`, `current_state.md`, and `character.json` files that adhere strictly to the Geminisys schemas.

To prevent the AI from generating "slim" characters and robbing players of their mechanical agency, the tool splits generation into a Narrative Socratic phase and a Mechanical Crunch phase.

---

## 2. The 4-Phase Creation Flow

### Phase 1: The Sandbox Pitch (Setting)
* **Goal:** Establish the broad genre, tone, and tech level (e.g., "Low-grit sci-fi salvage crew on the outer rim"). 
* **Mechanic:** Socratic chat with the AI.
* **Result:** Locks in the universe bounds and the legal Genesys skill/gear palette.

### Phase 2: Character Concepts (The Actors)
* **Goal:** Generate the narrative profiles, backstories, and Genesys Motivations (Desire, Fear, Strength, Flaw).
* **Mechanic:** The Socratic AI interviews the players ("Who are you? How did you meet? What is your biggest shared debt or flaw?").
* **Result:** Generates a draft `character.json` file for each player containing *only* the `narrative_profile`.

### Phase 3: Character Crunch (Player Agency)
* **Goal:** Spend starting XP on stats, skills, and talents to make the character mechanically playable.
* **Mechanic:** The UI transitions from a Chat Box to a Character Sheet form with a **Veteran Toggle**:
  * *Veteran ON:* The AI steps back. The player uses standard UI dropdowns and sliders to allocate stats manually.
  * *Veteran OFF (Guided):* The AI acts as an advisor, using the Phase 2 backstory to suggest specific mechanical stats (e.g., "Since you said you were a hacker, I recommend taking 2 ranks in Computers. Should we apply that?").
* **Result:** A fully populated, mechanically legal `character.json` file.

### Phase 4: Campaign Ignition (The Plot)
* **Goal:** Tie the finalized characters into a concrete inciting incident.
* **Mechanic:** The AI reads the finished characters' Motivations and Debts and pitches a campaign hook (e.g., "Since Luckii's character owes money to a syndicate boss, and Roger's character is running from a corporate warrant, the campaign kicks off when that syndicate boss threatens to turn Roger in unless you both pull a heist").
* **Result:** Finalizes the `campaign_setting.md` lore and generates the opening scene in `current_state.md`.

---

## 3. Architecture & API (For the Frontend Developer)

The frontend is a Single Page Application (SPA) that will sequentially step the user through the 4 phases above. 

It communicates with the Python backend entirely via stateless REST endpoints defined in the **`api/creator-api.yaml`** OpenAPI spec.

### Frontend Responsibilities
1. **Chat UI:** Render a standard message feed for Phases 1, 2, and 4.
2. **Crunch UI:** Render a form/sheet interface for Phase 3. It should use `genesys.schema.json` as a guide for what inputs need to be collected.
3. **Session Management:** The backend APIs are stateless. When the frontend hits `/chat`, it will receive a `session_id`. The frontend *must* hold onto this `session_id` and pass it back to the server on subsequent chat messages, and finally pass it to the `/finalize` endpoints so the backend knows which chat history to convert into files.

### Backend Endpoints Available
* `POST /api/creator/campaign/chat` - Drive the Socratic brainstorming for Phase 1 & 4.
* `POST /api/creator/character/chat` - Drive the Socratic brainstorming for Phase 2.
* `POST /api/creator/character/finalize` - Command the backend to write the draft character file.
* `POST /api/creator/campaign/finalize` - Command the backend to write the final Campaign files.
