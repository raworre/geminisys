# HIGH-LEVEL DESIGN (HLD) & GAME DEV DOCUMENT
**Project Name:** Omni-Director (AI GM Interface)
**System:** Genesys RPG
**Stack:** Python (Local Backend) + UI (TBD: PyQt, Textual, or Local Web-App)

## 1. OVERVIEW
A sleek, state-aware UI overlay designed to act as a "Forever GM" for a 2-player Genesys campaign. It bridges physical tabletop rolling with LLM narrative generation, prioritizing ease of use, hybrid input (Voice/Text), and automated state management.

## 2. USER INTERFACE (UX/UI) LAYOUT
The interface is divided into three primary zones to accommodate two players on a single screen/couch setup.

### A. The "Stage" (Center/Top)
* **Narrative Log:** A scrolling text window displaying the GM's narration and historical actions.
* **Mechanical Callouts (Luckii's Protocol 2):** The UI parses the GM's output for `[MECHANICS]` blocks. Any mechanical implications (e.g., "Luckii recovers 2 Strain", "Warlock takes 1 Wound") are automatically rendered in a highly visible, distinct color/alert box at the bottom of the narrative post. This ensures players never miss a stat update while reading the flavor text.
* **Audio Controls:** Toggle TTS (Text-to-Speech) on/off, replay last narration.

### B. The "Player Consoles" (Bottom Left & Right)
Two distinct, dedicated input zones (One for Warlock, one for Luckii).
* **Hybrid Input:** 
  * A standard text box for typing out actions deliberately.
  * A "Hold-to-Talk" button (STT via Whisper) for quick-shot vocal input.
* **IC / OOC Toggle (Luckii's Protocol):** A UI switch on the input box to flag the payload as In-Character (Action) or Out-of-Character (Question for the GM). This prepends `[OOC]` to the prompt so the GM knows to answer mechanically rather than narratively.
* **Identity Tagging:** Because the boxes are distinct, the system automatically prepends the character's name to the payload (e.g., `[WARLOCK]: "I dive for the terminal."`), preventing the GM from confusing who is doing what.

### C. The "Dice Tray" (Visual Input Component)
Instead of typing "2 Successes, 4 Threats", the UI features a visual row of the 6 core result symbols.
* **Counters:** [+] and [-] buttons next to icons for:
  * 💥 Success
  * 🦅 Advantage
  * 🏆 Triumph
  * 🔺 Failure
  * ⚙️ Threat
  * 🔴 Despair
* **Commit:** A "Send Roll" button that automatically parses the visual input into a structured text string for the GM (e.g., `[LUCKII ROLLS: 3 Success, 1 Threat]`).

## 3. AUDIO PIPELINE
* **Input (STT):** OpenAI Whisper API (or local Whisper model) for highly accurate transcription of sci-fi/RPG jargon.
* **Output (TTS):** ElevenLabs API (or OpenAI TTS) to read the GM's text aloud with dramatic pacing and cinematic voice modulation.

## 4. MODEL CONFIGURATION (Latency & Cost Optimization)
Real-time TTRPG sessions require low latency to maintain immersion. 
* **Model Selector UI:** A dropdown in the UI (or a config setting) allowing the user to select the active backend model.
* **The "Flash" Default:** The system should default to a "Flash" class model for standard gameplay. Flash models are significantly faster and cheaper, making them perfect for resolving standard dice rolls and snappy dialogue.
* **Hot-Swapping:** Players can hot-swap to a heavier "Pro" model mid-session if they need the GM to resolve an incredibly complex narrative mystery or generate a massive, intricate setting description, then drop back to Flash for combat.

## 5. STATE MANAGEMENT (The "Brain")
The UI acts as the state manager to prevent context-window sliding.
* **On Boot:** Loads `campaign_setting.md`, `warlock.json`, `luckii.json`, and `current_state.md`.
* **State Injection & Auto-Updating (Luckii's Protocol 4):** Appends a hidden JSON payload to every user prompt detailing current Wounds, Strain, and Inventory. Furthermore, when the GM outputs a `[STATE_UPDATE: {...}]` block, the Python UI intercepts it, automatically updates the local `warlock.json` or `luckii.json` files, and refreshes the UI. Players do not have to manually track their own health.
* **Stat Trackers & Visual Bars:** The UI renders Wounds and Strain as distinct, visual progress bars (e.g., green-to-red for Wounds, blue for Strain) using the live data. The bars include a clear "X / Y" text overlay (e.g., "4 / 12") for precise reading. Because the GM auto-updates the stats, these bars will dynamically fill or empty the moment the GM's response loads.
* **Session End:** On session end, the GM (LLM) MUST generate a summary of the session that just ended and write this to the `current_state.md` document.

## 6. CHARACTER MANAGER (Feature Indulgence)
A dedicated "Character Sheet" tab within the UI allowing players to sit with their physical books and digitize their characters without writing raw JSON.
* **Form-Based Entry:** Simple input fields for Attributes, Skills, and Talents that map directly to the `genesys_schema_template.json`.
* **Book Referencing:** Includes small "Ref Pg." text fields next to Talents and Weapons, allowing players to note the physical book page (e.g., "Core 72") for quick lookup during the game, bypassing the need for an integrated PDF viewer.
* **OPEN QUESTION:** Can the schema have space for a character background and all that jazz.