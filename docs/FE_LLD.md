# Geminisys Frontend Low-Level Design

**Project:** Geminisys / Omni-Director
**Audience:** Luckii (UI owner), with backend support from the software engineer on the project
**Status:** MVP implementation specification
**Primary recommendation:** Local web app using HTML, CSS, and JavaScript, served by the Python backend

## 1. Purpose and Scope

This document turns the presentation-layer requirements in the main LLD section 1.D and the dice-tray requirement currently listed as Phase 4, Task 4.4 into an implementable frontend plan.

The frontend is a **dumb client**. It displays information, collects player input, and sends requests. It does not decide whether an action succeeds, calculate Genesys rules, modify character files, or interpret the GM's state changes. Those decisions belong to the Python backend.

The MVP frontend must support:

- A shared narrative stage showing the GM response and recent actions.
- A visible mechanics callout attached to a GM response.
- A character console for either Warlock or Luckii.
- Wounds and strain trackers with current and maximum values.
- Text action entry.
- In-character / out-of-character input selection.
- Automatic character identity tagging.
- A six-symbol dice tray with increment/decrement counters.
- Staging an action before resolution.
- A resolve-scene control for the shared session.
- TTS controls represented in the UI, with playback integration added after the MVP.

The frontend should work in two modes:

1. **Mock mode:** uses local sample data and fake responses so the interface can be designed and tested without a running backend.
2. **Connected mode:** calls the FastAPI endpoints described in section 7.

## 2. Design Decisions

### 2.1 Choose a local web app

A local web app is the best fit for this project and for the current skill set:

- Existing work already includes `frontend/index.html`.
- HTML and CSS provide a direct bridge from visual art and layout into UI design.
- The Python server can expose JSON endpoints without requiring a new desktop GUI framework.
- The browser gives useful built-in controls for forms, buttons, scrolling, responsive layout, and audio.
- A single page can later be opened on two devices if the backend is made reachable on the local network.

The first version should use plain HTML, CSS, and JavaScript. A framework is not required for the MVP. If the interface later becomes difficult to maintain, the existing component boundaries can be migrated to a framework without changing the API contract.

### 2.2 Visual direction

Use a **warm spacecraft operations console** rather than a generic green terminal. The interface should feel like a game table: readable under low light, tactile, and slightly dramatic without making the text difficult to scan.

Suggested visual language:

- Near-black blue-gray background for the application shell.
- Warm ivory text for narrative content.
- Amber for staged actions and attention states.
- Cyan for strain and system information.
- Coral/red for wounds and danger.
- Muted green only for healthy or successful states.
- One display face for section labels and one highly readable text face for paragraphs.
- Small square corners or a maximum 6px radius; this is a console, not a collection of floating cards.

Choose colors by function, not decoration. Every important meaning must also be communicated by text, position, or icon shape so color is never the only signal.

### 2.3 Layout principle

The shared narrative is the largest area. Player controls remain close to the bottom or side so a player can read the scene, compose an action, add a roll, and stage it without losing context.

Desktop layout:

```text
+---------------------------------------------------------------+
| Header: session name | connection | model | audio              |
+-------------------------------+-------------------------------+
| Narrative Stage                | Character Console             |
| GM narration                   | Character identity            |
| Mechanics callouts             | Wounds / strain               |
| Recent staged actions          | action input                  |
|                               | dice tray                     |
+-------------------------------+-------------------------------+
| Shared footer: staged count | Resolve Scene                    |
+---------------------------------------------------------------+
```

Mobile layout:

1. Header and connection status.
2. Character identity and trackers.
3. Narrative stage.
4. Action composer.
5. Dice tray.
6. Staging and resolve controls.

The dice tray must remain usable on a narrow screen. Its six result controls should wrap into two rows rather than shrink until labels become unreadable.

## 3. Frontend Components

### 3.1 App shell

Responsibilities:

- Load the initial state on startup.
- Track whether the app is in mock or connected mode.
- Display connection/loading/error status.
- Route data into child components.
- Never modify state files directly.

Suggested DOM regions:

- `#app-header`
- `#narrative-stage`
- `#character-console`
- `#action-composer`
- `#dice-tray`
- `#session-footer`

### 3.2 Header

Displays:

- `GEMINISYS` and current session/campaign name.
- Active character selector: Warlock or Luckii.
- Backend status: Connecting, Connected, Mock Mode, or Error.
- Model label: Flash or Pro. The control may be display-only until model selection exists in the backend.
- TTS toggle and replay-last-narration button.

The header is informational and should not compete visually with the narrative.

### 3.3 Narrative stage

Responsibilities:

- Render a chronological list of entries.
- Distinguish player actions from GM narration.
- Keep the newest entry visible after a successful resolution.
- Render mechanics as a separate, high-contrast callout under the relevant narration.

An entry should have:

- Speaker label: `GM`, `WARLOCK`, or `LUCKII`.
- Optional timestamp.
- Main text.
- Optional mechanics list.

Do not show raw `[STATE_UPDATE: ...]` data in the UI. The backend interceptor owns that operation and returns clean presentation data.

### 3.4 Character console

Displays the selected character's:

- Name and player identity.
- Wounds as `current / threshold`.
- Strain as `current / threshold`.
- Soak value and defense as small secondary statistics.
- Optional compact inventory summary.

Tracker behavior:

- Wounds fill from green through amber to coral as current value approaches threshold.
- Strain uses cyan.
- The numeric value is always visible above or inside the bar.
- Values must not be editable in the player console. They are refreshed from `/api/state` after resolution.

### 3.5 Action composer

Controls:

- A multiline text field with a prompt such as `What does your character do?`.
- An IC/OOC segmented control, defaulting to IC.
- A `Stage Action` button.
- A hold-to-talk button placeholder for future STT.
- A small preview of the final tagged payload.

Behavior:

- Empty text cannot be staged.
- The selected identity is added by the frontend request's `character` field; it is not typed manually by the player.
- OOC mode prepends `[OOC]` to the submitted action text, or sends an explicit `mode: "ooc"` once the backend supports it.
- On success, clear the composer and show the action in the staged-actions list.
- On failure, retain the text and show a recoverable error.

### 3.6 Dice tray

The tray contains one control for each Genesys result symbol. The visible label should include the name, not only an icon, because symbols and emoji render inconsistently across operating systems.

Required counters:

| Result | Internal key | Initial value |
|---|---|---:|
| Success | `success` | 0 |
| Advantage | `advantage` | 0 |
| Triumph | `triumph` | 0 |
| Failure | `failure` | 0 |
| Threat | `threat` | 0 |
| Despair | `despair` | 0 |

Each control has a minus button, a visible count, and a plus button. Counts cannot go below zero. The tray also shows a plain-text summary, for example `3 Success, 1 Threat`, and a `Clear Roll` control.

When the player stages an action, the serialized result is:

```text
[LUCKII ROLLS: 3 Success, 1 Threat]
```

If every count is zero, omit the roll field rather than sending an empty roll string.

The dice tray is a frontend formatter only. It must not cancel opposing symbols or determine the final Genesys result.

### 3.7 Staged-actions area and footer

Show:

- Number of staged actions.
- Character name for each staged action.
- A short action preview.
- Dice summary when present.
- A `Resolve Scene` button.

`Resolve Scene` is a shared action. It should be disabled while a request is in progress and while there are no staged actions. The UI should ask for confirmation only if the team decides accidental resolution is a real risk during playtesting; avoid a modal by default for speed.

## 4. Client State Model

The browser maintains presentation state only:

```js
{
  mode: "mock" | "connected",
  connection: "loading" | "connected" | "error",
  activeCharacter: "warlock" | "luckii",
  characters: { warlock: {}, luckii: {} },
  campaignState: "",
  stagedActions: [],
  narrativeEntries: [],
  draftAction: "",
  inputMode: "ic" | "ooc",
  dice: {
    success: 0,
    advantage: 0,
    triumph: 0,
    failure: 0,
    threat: 0,
    despair: 0
  },
  isSubmitting: false,
  errorMessage: null,
  ttsEnabled: false,
  lastNarration: ""
}
```

The backend remains the source of truth for character data and campaign state. After `resolve`, the frontend must fetch `/api/state` again rather than trying to predict the new wound or strain values.

## 5. Interaction Flows

### 5.1 Boot

1. Render a loading shell immediately.
2. Request `GET /api/state`.
3. Populate character trackers and campaign context.
4. Set status to Connected.
5. If the request fails, switch to Mock Mode or show a clear retry control, depending on the selected development mode.

### 5.2 Stage a text action

1. Player selects their character.
2. Player selects IC or OOC.
3. Player types an action.
4. Player optionally creates a dice result.
5. Frontend formats the roll and sends `POST /api/intent`.
6. Frontend adds a pending/staged entry and updates the staged count.

### 5.3 Resolve the scene

1. Player presses `Resolve Scene`.
2. Disable the button and show `Resolving...`.
3. Send `POST /api/resolve`.
4. Add the returned narrative to the narrative stage.
5. Add mechanics separately when the backend returns them.
6. Request `/api/state` again to refresh trackers.
7. Re-enable controls and store the latest narration for replay.

### 5.4 Hold-to-talk, later

For the first release, the button can show `Voice input unavailable` and remain disabled. Later it should have three states: Ready, Recording, and Transcribing. Releasing the button sends audio to the backend, then places the returned transcription into the action field for review before staging.

### 5.5 TTS, later

Use the browser's audio element or Web Speech API for an initial prototype. The replay button must be disabled when no narration exists. The backend can replace this with ElevenLabs/OpenAI audio later without changing the narrative component.

## 6. Error, Loading, and Empty States

These are part of the design, not polish to add at the end.

- Loading: skeleton blocks or concise `Loading session...` labels.
- No narrative: `No scene has been resolved yet.`
- No staged actions: `Stage one or more actions to resolve the scene.`
- Backend unavailable: show the problem, preserve the draft, and offer `Retry`.
- Resolve failure: keep staged actions visible so the player does not lose work.
- Invalid state data: show the character name and `Character data unavailable`; do not render broken bars.
- Long narration: keep the stage scrollable and preserve paragraph breaks.

## 7. Backend Contract

The current server already provides these endpoints.

### `GET /api/state`

Current response shape:

```json
{
  "warlock": { "...": "character data" },
  "luckii": { "...": "character data" },
  "campaign_state": "markdown text",
  "holding_pen": ["warlock", "luckii"]
}
```

### `POST /api/intent`

Request:

```json
{
  "character": "luckii",
  "action_text": "I search the terminal.",
  "dice_result": "[LUCKII ROLLS: 3 Success, 1 Threat]"
}
```

Current success response:

```json
{ "status": "staged", "message": "Luckii added to queue." }
```

### `POST /api/resolve`

Current success response:

```json
{
  "status": "resolved",
  "narrative": "The GM response with state-update data removed."
}
```

### Recommended small contract extension

The HLD requires `[MECHANICS]` callouts, but the current resolve response only returns `narrative`. The backend should eventually return:

```json
{
  "status": "resolved",
  "narrative": "The clean GM narration.",
  "mechanics": ["Luckii recovers 2 Strain", "Warlock takes 1 Wound"],
  "state_updated": true
}
```

Until that exists, the frontend may display the entire clean response as narration, but it must not attempt to parse or apply state updates itself.

## 8. Implementation Plan

### Phase A: Paper and visual prototype

1. Draw the desktop layout on paper or in a simple image editor.
2. Draw the mobile layout separately; do not assume desktop will naturally collapse well.
3. Decide the names, colors, typography, spacing, and result-symbol treatments.
4. Create three states for each important area: normal, loading, and error/empty.
5. Ask the software engineer to review the component names and API assumptions before coding.

Deliverable: one annotated desktop mockup and one annotated mobile mockup.

### Phase B: Static HTML and CSS

1. Replace the placeholder markup in `frontend/index.html` with semantic sections.
2. Create a stylesheet, keeping color and spacing values in CSS custom properties.
3. Build the narrative stage, character console, action composer, and dice tray with sample data.
4. Make the dice tray work visually at desktop and mobile widths.
5. Add keyboard focus styles and labels before adding visual effects.

Deliverable: a clickable-looking static screen that can be reviewed without Python.

### Phase C: Dice tray behavior

1. Represent the six counts in one JavaScript object.
2. Wire plus and minus buttons using `data-result` attributes.
3. Prevent negative values.
4. Generate the human-readable summary from the object.
5. Generate the exact `dice_result` string expected by the backend.
6. Add a clear/reset action.

Deliverable: a tray that can be tested independently of the GM.

### Phase D: Mock-mode application behavior

1. Add a small mock state object based on the files in `state/`.
2. Implement `loadState`, `stageIntent`, and `resolveScene` functions with the same return shapes as the real API.
3. Use a short fake delay for loading and resolving so loading states can be designed.
4. Test empty input, zero dice, multiple dice types, and repeated staging.

Deliverable: a complete rehearsal of the player workflow without a server.

### Phase E: Connected API behavior

1. Replace mock functions with `fetch` calls behind the same three function names.
2. Keep the character object and all state update logic in the response-rendering layer.
3. Refresh state after every successful resolution.
4. Handle network errors without clearing the draft or staged actions.
5. Test using the running FastAPI server.

Deliverable: text actions and dice rolls can travel from the browser to the Python holding pen and back as narration.

### Phase F: Audio and polish

1. Add TTS only after text resolution is reliable.
2. Add the hold-to-talk control only after a transcription endpoint exists.
3. Add model selection when the backend exposes a model setting.
4. Add animations sparingly: entry fade-in, resolving indicator, and tracker update.
5. Playtest with real reading distance, low room lighting, and a phone-sized viewport.

Deliverable: playable MVP with optional audio, not audio-dependent MVP.

## 9. Suggested File Structure

Start small:

```text
frontend/
  index.html       # semantic page structure
  styles.css       # visual system and responsive layout
  app.js           # state, API calls, and event handlers
  mock-data.js     # development-only sample state and responses
```

Do not split every panel into its own file until the page becomes difficult to navigate. A small number of understandable files is friendlier while learning.

## 10. Acceptance Checklist

The frontend MVP is complete when:

- The page loads without a backend in Mock Mode.
- A player can select Warlock or Luckii.
- Wounds and strain show readable `current / threshold` values.
- A player can switch between IC and OOC.
- Empty actions cannot be staged.
- The six dice counters increment, decrement, clear, and serialize correctly.
- A staged action displays its character and roll summary.
- Resolve shows a loading state and then adds narration.
- Connected mode calls the three current API endpoints successfully.
- State is refreshed after resolution rather than guessed by the browser.
- Backend errors preserve user-entered text and explain how to retry.
- The interface is usable with keyboard controls and at a mobile width.
- Raw state-update JSON is never displayed to players.
- TTS and STT are clearly marked unavailable until their backend hooks exist.

## 11. Working Agreement

Luckii owns:

- Information hierarchy.
- Mockups, visual language, layout, CSS, and interaction feel.
- Manual playtesting notes.

The software engineer owns or supports:

- API contract changes.
- FastAPI integration and CORS/network setup.
- Mechanics parsing and state persistence.
- Audio endpoints and deployment details.

Review together at the end of each phase. Keep the interface understandable before making it ornate. The most valuable early question is: can a player glance at the screen, understand the current state, stage an action, and tell what is waiting to be resolved?
