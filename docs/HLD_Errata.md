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

## 3. Network Topology & Hardware Deployment
Because this is a local-first application designed for physical tabletop sessions, the deployment architecture relies on standard LAN routing rather than cloud hosting. The backend API explicitly binds to `0.0.0.0` to accept incoming connections from the local WiFi subnet (e.g., `192.168.x.x`).

### Phase 1: The "50-Foot HDMI" Setup (Current Sandbox)
*   **The Server:** Runs locally on the Host Laptop. 
*   **The Director Screen (Communal UI):** The Host Laptop is physically tethered to a 50" living room TV via a 50' HDMI cable. A browser window is dragged to the TV pointing to the communal GM UI endpoint.
*   **The Player Clients:** The Host Laptop opens a second local browser window pointing to the "Player Login" UI to select their character. The Client Laptop (Luckii) connects to the Host's internal IP over the local WiFi to access their respective Player UI.
*   **Zero-Cost Network Optimization (The Hotspot Trick):** To prevent "WiFi Hairpinning" (where local traffic goes down to the router and back up), the Host Laptop can enable the Windows "Mobile Hotspot" feature. Client laptops connect directly to the Host's hotspot. This creates a pristine `1ms` ping local LAN for the VTT, while the Host Laptop independently maintains the finicky connection to the internet for LLM API calls.

### Phase 2: The Raspberry Pi Micro-Console (Future Ideal)
*   Because the tech stack (FastAPI + lightweight JSON state) is incredibly small, the entire backend can be deployed to a Raspberry Pi with a built-in WiFi adapter.
*   The Pi physically sits at the TV, connected via a standard 3-foot HDMI cable, displaying the communal GM UI.
*   Both players act purely as lightweight web clients, connecting to the Pi over the local WiFi. This eliminates the need for physical tethers across the living room while maintaining zero cloud-hosting costs.

**Recommended Hardware List:**
*   **Raspberry Pi 4 (4GB) or Pi 5:** Running a Chromium window for the TV plus the FastAPI backend is lightweight, but 4GB ensures the UI won't stutter during animations.
*   **High-Gain USB WiFi Adapter (Crucial):** The built-in Pi antenna is weak. For a split-level house with interference, a Linux-native dual-antenna adapter (like the *Panda Wireless PAU09* or *BrosTrend AC1200*) is required to punch through the floor down to the router.
*   **Passive Cooling Case:** A *Flirc Aluminum Case* acts as a giant passive heatsink. Zero fan noise means no buzzing distractions during quiet, dramatic roleplay moments.
*   **High-Endurance MicroSD Card:** Because the state machine is constantly writing to `current_state.md` and character JSONs, a dashcam-rated "High Endurance" SD card (like SanDisk High Endurance) is highly recommended to prevent file-system corruption over time.
