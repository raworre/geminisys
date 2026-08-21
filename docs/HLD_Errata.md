# HLD Errata & Architectural Addendums

*This document captures mid-development architectural pivots and state-machine designs that supersede the original HLD.*

## 1. The Scene State Machine (The 4-Phase Loop)
Because Genesys requires the GM to dictate the difficulty (the dice pool) *after* the player states their intent but *before* the narrative resolves, the simple Jackbox queue has been expanded into a true RESTful 4-state machine for any given Scene:

1. **`INTENT_COLLECTION`**: 
   - UI State: Text inputs open.
   - Action: Players submit their desired actions to the holding pen.
2. **`POOL_ASSIGNMENT`**: 
   - UI State: "Waiting for GM..."
   - Action: Backend detects a full queue and pings the AI GM to analyze the intents and assign required Genesys dice pools based on character sheets.
3. **`ROLL_COLLECTION`**: 
   - UI State: Client JS detects their character has a pending roll in the JSON state. Text inputs hide, and the visual Dice Tray modal slides up.
   - Action: Players roll physical dice and tap the visual results into their phones.
4. **`RESOLUTION`**:
   - UI State: "Uplinking to Omni-Director..." animation.
   - Action: Backend bundles Intents + Dice Results, pings the AI GM for the cinematic outcome, updates JSON character sheets (Wounds/Strain), and commits to Campaign history.

## 2. Latency Masking (The "Feature, Not a Bug" Strategy)
By utilizing the Antigravity CLI as the backend pipe (`agy`), we absorb zero API costs and gain enterprise-tier model access. However, this introduces a ~4-second boot latency per turn. 
- **The UX Solution**: Because tabletop RPGs naturally have tension during resolution, the 4-8 second total delay (CLI boot + LLM generation + 2s UI polling) will be masked by thematic UI animations (e.g., "Uplinking to Corporate...", "Calculating Probabilities..."). This converts backend latency into dramatic tension.
