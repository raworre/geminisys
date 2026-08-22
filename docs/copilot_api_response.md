# Copilot API Review Response

Thank you for the thorough API review! You caught exactly the missing structural links we needed to make the Phase 2 -> Phase 3 -> Phase 4 handoffs work correctly. 

We have updated the `api/creator-api.yaml` and the Python backend to resolve your blockers. Here are the answers to your remaining architectural questions:

### 1. Phase Handoffs & Context Injection
**Resolved:** We added `campaign_id` and `character_id` to the `ChatRequest` schema. 
- During **Phase 2 (Narrative)**, if you pass the `campaign_id`, the backend silently loads the campaign lore and injects it into the AI's system prompt.
- During **Phase 3 (Crunch)**, if you pass both `campaign_id` and `character_id`, the backend loads the user's active draft character sheet into the AI's prompt so it can offer mechanical advice (e.g. "Buy the Athletics skill!").
- During **Phase 4 (Ignition)**, the backend physically scans the campaign directory, loads every saved character JSON it finds, and injects them into the AI's prompt so it can weave them together.

### 2. Semantic Flip: Save vs Finalize
**Resolved:** We have swapped the names of our endpoints to be more semantically accurate:
- `POST /api/creator/character/save` now marks the end of the Narrative Phase. It reads the chat history, returns the `narrative_profile` JSON draft, and deletes the history file.
- `POST /api/creator/character/finalize` now marks the end of the Crunch Phase. The UI POSTs the completed, human-verified sheet here to be permanently written to the disk.

### 3. The Crunch Engine (Phase 3 Pivot)
**Resolved:** You correctly pointed out the nightmare of putting Genesys XP math into the frontend. **We have moved the Rule Engine to the backend.**
- The frontend is now a pure presentation layer. 
- You will use `PATCH /api/creator/character/crunch/buy` to attempt to purchase skills/talents.
- The backend will perform the math (e.g., checking if they have enough XP, or if they satisfy the Talent Pyramid). 
- If the purchase is illegal, the backend returns a `400 Bad Request` formatted as an RFC 7807 `Problem+JSON` (e.g. `urn:geminisys:error:invalid-upgrade`). You simply display the `detail` string in a toast notification!

### 4. Session Lifecycle & Idempotency
- **Concurrency:** This is a local-only tool. Sessions are just an array in a local `.json` file (`campaigns/history/{session_id}.json`). They never expire, they don't lock, and they aren't sensitive.
- **Idempotency:** You can call `/save` on the same session as many times as you want. It simply reads the history array and outputs a summary. 
- **Start Over:** If the user wants to start over, the frontend just drops the `session_id` and hits `/chat` to generate a brand new one.

### 5. AI Readiness vs UI Control
- You correctly deduced that `is_complete` is merely an AI *suggestion*. The frontend UI is the absolute source of truth. If `is_complete: true`, you can show the Next Phase button, but if the user keeps typing, just keep sending requests! The backend is totally stateless and will happily keep adjusting the narrative.
- We also added a `turn_number` to the Chat responses so you can monitor session length and delay spikes.

### 6. Static Reference Data
- To save you from hardcoding rules, you can pull the base game data from `GET /api/rules/skills` and `GET /api/rules/talents`. These JSON arrays contain the exact definitions, IDs, and mapped characteristics for the Genesys system.

### 7. Security & CORS
- `security: []` is intentional. This is a local CLI tool designed to run on `localhost`. There is no auth.
- CORS is currently unrestricted in the FastAPI backend, so the frontend can hit it from `localhost:3000` or `localhost:5173` without issue.
