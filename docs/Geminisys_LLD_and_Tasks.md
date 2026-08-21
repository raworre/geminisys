# Geminisys: Low-Level Design (LLD) & Task Tree

**Goal:** Playable MVP by Saturday Evening.
**Architecture Pattern:** Decoupled Client-Server (Frontend UI interacts with a local Python Backend Engine).

---

## 1. LOW-LEVEL ARCHITECTURE (LLD)

### A. The State Manager (Data Layer)
*   **Files:** `genesys.schema.json`, `warlock.json`, `luckii.json`, `campaign_state.md`.
*   **Logic:** A Python class (`StateManager`) that loads JSON/MD files into memory on boot. It provides methods to safely overwrite these files (e.g., `update_wounds(character, amount)`).

### B. The Context Injector (Prompt Pipeline)
*   **Logic:** A Python class (`PromptBuilder`) that intercepts the user's raw input from the UI.
*   **Process:** 
    1. Reads `warlock.json` and `luckii.json`.
    2. Reads `campaign_state.md`.
    3. Bundles them into a hidden payload.
    4. Appends the user's input (e.g., `[WARLOCK]: I shoot the door.`).
    5. Sends the massive bundled prompt to the Gemini API.

### C. The Interceptor (Output Parser)
*   **Logic:** A Regex/JSON parser that catches the LLM's raw response *before* it hits the UI.
*   **Process:**
    1. Scans for `[STATE_UPDATE: {...}]`.
    2. If found, extracts the JSON, passes it to the `StateManager` to save to disk, and strips the block from the text.
    3. Scans for `[MECHANICS: ...]`.
    4. Passes the remaining narrative text and the mechanics block to the UI via a structured payload (e.g., a Python dictionary or JSON object).

### D. The Presentation Layer (Frontend - Luckii's Domain)
*   **Logic:** A Python GUI (PyQt, CustomTkinter, or local Web App) that remains entirely "dumb" to the rules. It only handles rendering text, catching button clicks, and triggering STT/TTS.

---

## 2. DEPENDENCY TREE & TASK CHECKLIST

*Use this as our master roadmap. Tasks are grouped by dependency. Luckii can operate completely independently on Phase 4 while we build Phases 2 & 3.*

### Phase 1: Foundation (Completed)
- [x] High-Level Design (HLD) & Concept Approval
- [x] Core JSON Schemas designed and formalized (`genesys.schema.json`)

### Phase 2: The Core Engine (Backend - We are here)
- [ ] **Task 2.1: The Master System Prompt.** Write the rules document that teaches Gemini how to negotiate dice pools, wait for "Staged Resolutions", and output `[STATE_UPDATE]` blocks. *(Blocks Phase 3)*
- [ ] **Task 2.2: StateManager Script.** Write the Python functions to load and save the JSON/MD files safely.
- [ ] **Task 2.3: API Hook.** Write a basic Python script that can send a prompt to the Gemini API and print the response.

### Phase 3: The Interceptor (Backend)
- [ ] **Task 3.1: The Regex Parser.** Write the Python logic to extract state updates from the LLM's output. *(Depends on 2.1 & 2.2)*
- [ ] **Task 3.2: Terminal Testing.** Run a mock combat encounter entirely in the terminal to prove the AI can auto-update the local JSON files when someone takes damage. *(Proves Backend MVP)*

### Phase 4: The Presentation Layer (Frontend - Luckii)
- [ ] **Task 4.1: UI Mockups.** Design the visual layout (Shared console, Staging Area, Narrative Stage, Dice Tray).
- [ ] **Task 4.2: Framework Selection.** Decide on PyQt6, CustomTkinter, or Textual.
- [ ] **Task 4.3: UI Skeleton.** Build the buttons and text boxes (even if they don't do anything yet).
- [ ] **Task 4.4: The Dice Tray.** Build the visual component that converts clicks on the 6 Genesys symbols into a text string (e.g., `3 Success, 1 Threat`). *(Can be done concurrently with everything else).*

### Phase 5: Integration & Audio (Saturday Morning)
- [ ] **Task 5.1: The Hookup.** Connect Luckii's UI buttons to our Backend Python functions.
- [ ] **Task 5.2: Voice Input (STT).** Integrate Whisper for hold-to-talk.
- [ ] **Task 5.3: Voice Output (TTS).** Integrate ElevenLabs/OpenAI TTS for the GM's voice.
- [ ] **Task 5.4: Playtest!**
