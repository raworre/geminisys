# Geminisys Frontend Low-Level Design

**Project:** Geminisys / Omni-Director
**Audience:** Luckii (UI owner), with backend support from Hrothgar (software engineer)
**Status:** MVP implementation specification
**Primary recommendation:** Local web app using HTML, CSS, and JavaScript, served by the Python backend

## 1. Purpose and Scope

This document turns the presentation-layer requirements in the main LLD section 1.D and the dice-tray requirement currently listed as Phase 4, Task 4.4 into an implementable frontend plan.

The frontend is a **dumb client**. It displays information, collects player input, and sends requests. It does not decide whether an action succeeds, calculate Genesys rules, modify character files, or interpret the GM's state changes. Those decisions belong to the Python backend.

The MVP frontend must support:

- A campaign-selection screen shown before any character selection.
- A shared narrative stage showing the GM response and recent actions, intended for a TV or separate monitor.
- A visible mechanics callout attached to a GM response.
- The same player-console UI shown in two windows, one for each player; each window displays the character selected from the active campaign and that character's data.
- A character-selection dropdown populated by the selected campaign.
- Wounds and strain trackers with current and maximum values.
- Text action entry.
- In-character / out-of-character input selection.
- Automatic character identity tagging.
- A six-symbol dice tray with increment/decrement counters.
- Staging an action before resolution.
- A resolve-scene control for the shared session.
- TTS controls represented in the UI, with playback integration added after the MVP.

The MVP is designed for desktop and laptop displays. A mobile layout is explicitly out of scope for now.

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
- The same frontend can be opened in separate browser windows for the narrative display and both player consoles.
- The backend can later coordinate those windows over the local network without requiring a separate UI technology.

The first version should use plain HTML, CSS, and JavaScript. A framework is not required for the MVP. If the interface later becomes difficult to maintain, the existing component boundaries can be migrated to a framework without changing the API contract.

### 2.2 Visual direction

Use a **neutral tabletop interface** rather than a setting-specific visual style or generic green terminal. The interface should feel clear, readable, and tactile, with enough personality to feel like a game table without suggesting that the campaign takes place in space, fantasy, horror, or any other particular setting. Future skins can add those identities without changing the underlying layout or usability.

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

### 2.3 Display roles and layout

The frontend has three display roles. They may use the same codebase, but each window shows a focused view:

1. **Campaign Selector:** the first screen shown when a window has no active campaign.
2. **Narrative Display:** a read-focused shared stage for a TV or separate monitor. It shows the campaign title, GM narration, mechanics callouts, and recent actions. It does not show private player input controls.
3. **Player Console:** one reusable console layout for one player. The same layout is rendered in two windows; only the selected campaign/character data and resulting labels and tracker values differ.

The campaign is selected before the character. Once a campaign is selected, the character dropdown is populated only with characters belonging to that campaign. A player cannot select a character from another campaign.

For the MVP, the display role can be chosen through a setup control or URL parameter, such as `?view=narrative` or `?view=player`. The player view then asks for the campaign and character. The narrative view asks only for the campaign.

Narrative display layout:

```text
+---------------------------------------------------------------+
| Campaign title | connection | model | audio                    |
+-------------------------------+-------------------------------+
|                                                               |
|                     NARRATIVE STAGE                           |
|                     GM narration                             |
|                     Mechanics callouts                        |
|                     Recent actions                            |
|                                                               |
+-------------------------------+-------------------------------+
| Session status | Staged count | Resolve Scene                  |
+---------------------------------------------------------------+
```

Player console layout:

```text
+---------------------------------------+
| Campaign | character | connection     |
+---------------------------------------+
| Character identity and trackers       |
| Wounds / strain / secondary stats     |
+---------------------------------------+
| Action composer                       |
| IC / OOC | text | Stage Action        |
+---------------------------------------+
| Dice tray                             |
| Six result counters | Clear Roll      |
+---------------------------------------+
| Staged actions | Resolve Scene        |
+---------------------------------------+
```

The two player consoles are independent instances of the same UI, showing different selected-character data within the same campaign. The narrative display is also independent, but all three views must refresh when a scene is resolved. Responsive mobile behavior is not required for the MVP; use stable desktop dimensions and test common laptop and TV resolutions instead.

#### Narrative display waiting state

While the campaign is being selected, or while the selected campaign has no resolved scene yet, the narrative display should show a simple title state rather than an empty panel. It can include:

- The `GEMINISYS` title.
- The selected campaign name, when one is available.
- A quiet status message such as `Awaiting campaign selection` or `Awaiting first scene`.
- A persistent connection status such as `Connected`, `Connecting`, `Mock Mode`, or `Offline`.

For the MVP, this should be a polished static composition. After the campaign-selection, staging, resolution, and synchronization flows are reliable, an optional simple ambient animation may be added to this title state. Examples include a slow background texture shift, a restrained light movement, or a gentle title reveal. It should remain low-motion, nonessential, and easy to disable so it does not distract from the game or create accessibility problems.

### 2.4 Future theme support

The frontend should remain open to themed skins, but skin creation is not an MVP feature. This does require one small implementation decision now: put colors, fonts, borders, spacing, and major visual effects behind CSS custom properties rather than scattering literal values through the stylesheet.

The functional color scheme is a permanent accessibility and usability layer. The colors for healthy status, wounds, strain, staged attention, and other connection or state indicators must not change between themes. A skin may change decorative colors, textures, typography, borders, and atmosphere, but it must not override or repurpose functional color tokens.

For example:

```css
:root {
  --color-background: #10151b;
  --color-text: #f4ead8;
  --color-accent: #e7aa45;
  --color-attention: #e7aa45;
  --color-healthy: #72b85a;
  --color-wounds: #d46a5f;
  --color-strain: #5fc4d4;
}
```

Token roles:

- `--color-attention` is the protected functional amber used for staged actions, pending decisions, or other states that require notice.
- `--color-accent` is the general visual highlight used for interactive focus, selected controls, links, or branding. It may share the attention color initially, but it must not be used for functional state when a theme is allowed to change it.

A future theme can load a second theme class without changing the HTML structure or JavaScript, but it must leave the functional tokens above unchanged. Keep the semantic meanings and exact functional colors stable across every skin so players can rely on them and so color-based information remains accessible. Do not build a theme picker until the base interface has been playtested.

## 3. Frontend Components

### 3.1 App shell (the browser window's shared frame)

“App shell” means the persistent outer frame of the frontend window: the header, status area, page background, and the region into which the current view is rendered. It is essentially the window's reusable structure, not a separate operating-system window or a special framework.

Responsibilities:

- Load campaign choices on startup.
- Load characters only after a campaign has been selected.
- Render the correct display role: campaign selector, narrative display, or player console.
- Track whether the app is in mock or connected mode.
- Display connection/loading/error status.
- Route data into child components.
- Never modify state files directly.

Suggested DOM regions for the focused views:

- `#app-header`
- `#campaign-selector`
- `#narrative-stage`
- `#character-console`
- `#action-composer`
- `#dice-tray`
- `#session-footer`

### 3.2 Header

Displays:

- `GEMINISYS` and current campaign name.
- Active character selector on player consoles only.
- Backend status: Connecting, Connected, Mock Mode, or Error.
- Model label: Flash or Pro. The control may be display-only until model selection exists in the backend.
- TTS toggle and replay-last-narration button.

The header is informational and should not compete visually with the narrative.

#### Header menu

The header should include a small menu for secondary actions. Keep immediate gameplay actions such as `Stage Action` and `Resolve Scene` visible on the page rather than hiding them in this menu.

MVP menu options:

- **Change Campaign:** return to campaign selection and clear the current window's selected character. The shared campaign session should not be deleted or reset by this action.
- **Audio:** access TTS on/off and replay-last-narration controls.
- **Connection Status:** show the current connection state and provide `Retry` when the backend is unavailable.
- **Reset View:** restore this window's view and local UI preferences without changing campaign or character data.

Future option:

- **Change Character:** keep this available as a later option for player consoles if the use case grows to require switching characters during a session. It is not required for the current MVP workflow.

The menu should be available on all display roles, but it should show only options that make sense for the current window. For example, a narrative display should not show player-character actions.

### 3.3 Campaign selector

The campaign selector is the first workflow step. It should show available campaigns as a simple list or dropdown with the campaign name and a brief description when available.

Behavior:

- No character dropdown is shown until a campaign is selected.
- Selecting a campaign stores its stable campaign ID, not only its display name.
- The player view then requests or receives the characters for that campaign, including each character's availability.
- While a player is choosing, refresh the character list periodically at a modest interval, such as every 5 seconds, or when the dropdown receives focus. This is lightweight enough for the selection screen and avoids requiring real-time infrastructure for the MVP.
- When a player selects a character, send a backend claim request before entering the console. The backend must atomically reserve that character for the current player-console/session so two players cannot claim the same character at the same time.
- A character already claimed by the other player is disabled in the dropdown and labeled `Unavailable` or `In use`.
- If a claim fails because the other player selected it first, refresh the list and ask the player to choose another available character without losing the rest of their setup.
- Claims should have a short session lease or heartbeat so a disconnected or closed player console does not leave a character unavailable forever. An explicit release from `Change Campaign` should still happen when possible.
- The narrative view enters the shared stage after campaign selection.
- A `Change Campaign` control returns to this screen, releases the current character claim, and clears the selected character for that window. It must not delete or reset campaign data.

### 3.4 Narrative stage

Responsibilities:

- Render a chronological list of entries.
- Distinguish player actions from GM narration.
- Keep the newest entry visible after a successful resolution.
- Render mechanics as a separate, high-contrast callout under the relevant narration.
- Render the title/waiting state when there is no active scene to display.

An entry should have:

- Speaker label: `GM`, `WARLOCK`, or `LUCKII`.
- Optional timestamp.
- Main text.
- Optional mechanics list.

Do not show raw `[STATE_UPDATE: ...]` data in the UI. The backend interceptor owns that operation and returns clean presentation data.

### 3.5 Character console

This is a reusable player-console component, not a separate Warlock screen and Luckii screen. Render it twice with the selected character record as its data input. Do not create character-specific markup or layouts unless a future gameplay requirement genuinely differs between characters.

Displays the selected character's:

- Name and player identity.
- Wounds as `current / threshold`.
- Strain as `current / threshold`.
- Soak value and defense as small secondary statistics.
- Optional compact inventory summary.

The character dropdown belongs here, above the character name. It is populated from the selected campaign and is independent in each player-console window. The two players may therefore choose different characters while remaining in the same campaign.

Tracker behavior:

- Wounds fill from green through amber to coral as current value approaches threshold.
- Strain uses cyan.
- The numeric value is always visible above or inside the bar.
- Values must not be editable in the player console. They are refreshed from `/api/state` after resolution.

### 3.6 Action composer

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

### 3.7 Dice tray

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

### 3.8 Staged-actions area and footer

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
  displayRole: "campaign-selector" | "narrative" | "player",
  campaigns: [],
  selectedCampaignId: null,
  availableCharacters: [],
  activeCharacterId: null,
  playerConsoleId: null,
  characterClaimStatus: "unclaimed" | "claiming" | "claimed" | "unavailable",
  characters: {},
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

Each browser window stores its display role, selected campaign ID, and, for a player console, selected character ID. These selections are window-specific UI state. The campaign itself and the character files remain backend state.

## 5. Interaction Flows

### 5.1 Boot and campaign selection

1. Render the app shell immediately with a loading status.
2. Request the available campaigns.
3. Show the campaign selector unless a valid campaign ID was supplied for a previously configured window.
4. After campaign selection, request the selected campaign's characters.
5. Narrative view enters the narrative display; player view shows the character dropdown.
6. While the player is choosing, refresh the character list periodically or on dropdown focus.
7. After character selection, claim the character through the backend before requesting state and populating that player's console.
8. If a claim fails, refresh the list and keep the player on character selection.
9. If a request fails, switch to Mock Mode or show a clear retry control, depending on the selected development mode.

### 5.2 Stage a text action

1. Player selects a campaign if one is not already active.
2. Player selects their character from the campaign's character dropdown.
3. Player selects IC or OOC.
4. Player types an action.
5. Player optionally creates a dice result.
6. Frontend formats the roll and sends `POST /api/intent` with the campaign and character IDs when supported.
7. Frontend adds a pending/staged entry and updates the staged count.

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
- No narrative: show the narrative display title state with `Awaiting first scene` rather than an empty panel.
- No staged actions: `Stage one or more actions to resolve the scene.`
- Backend unavailable: show the problem, preserve the draft, and offer `Retry`.
- Resolve failure: keep staged actions visible so the player does not lose work.
- Invalid state data: show the character name and `Character data unavailable`; do not render broken bars.
- Long narration: keep the stage scrollable and preserve paragraph breaks.

## 7. Backend Contract

The current server provides `/api/state`, `/api/intent`, and `/api/resolve`. Campaign selection requires the two additional endpoints described first below.

### `GET /api/campaigns`

This endpoint is needed for the campaign-first startup flow. Recommended response:

```json
{
  "campaigns": [
    {
      "id": "campaign-001",
      "name": "The Example Campaign",
      "description": "Optional short description"
    }
  ]
}
```

### `GET /api/campaigns/{campaign_id}/characters`

This endpoint is needed to populate the character dropdown after campaign selection. Recommended response:

```json
{
  "campaign_id": "campaign-001",
  "characters": [
    { "id": "luckii", "name": "Luckii", "available": true },
    { "id": "warlock", "name": "Warlock", "available": false }
  ]
}
```

### `POST /api/campaigns/{campaign_id}/claims`

Recommended request and response for reserving a character:

```json
{
  "player_console_id": "player-console-1",
  "character_id": "luckii"
}
```

```json
{
  "status": "claimed",
  "campaign_id": "campaign-001",
  "character_id": "luckii"
}
```

If the character is already claimed, return a conflict response such as HTTP `409` with `status: "unavailable"`. The frontend then refreshes the character list rather than assuming the claim succeeded.

### `DELETE /api/campaigns/{campaign_id}/claims/{character_id}`

Release the current player's claim when they choose `Change Campaign`, close the player-console session, or otherwise leave character setup. The backend should verify the `player_console_id` before releasing a claim.

### `GET /api/state`

The current server returns global state and does not yet accept a campaign ID. Recommended future shape:

```json
{
  "campaign_id": "campaign-001",
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
  "campaign_id": "campaign-001",
  "character": "luckii",
  "action_text": "I search the terminal.",
  "dice_result": "[LUCKII ROLLS: 3 Success, 1 Threat]"
}
```

Current success response:

```json
{ "status": "staged", "message": "Luckii added to queue." }
```

The existing server does not yet define campaign IDs. Until campaign storage is implemented, the mock mode can use the existing `warlock.json` and `luckii.json` files as the first campaign. Hrothgar should decide whether campaigns become folders, a registry file, or database records before connected campaign selection is implemented.

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

1. Draw the campaign selector, narrative display, and player console separately on paper or in a simple image editor.
2. Decide which information belongs on the TV and which belongs only on player consoles.
3. Decide the names, colors, typography, spacing, and result-symbol treatments.
4. Create three states for each important area: normal, loading, and error/empty.
5. Ask Hrothgar to review the component names and API assumptions before coding.

Deliverable: one annotated mockup for each display role.

### Phase B: Static HTML and CSS

1. Replace the placeholder markup in `frontend/index.html` with semantic sections.
2. Create a stylesheet, keeping color and spacing values in CSS custom properties.
3. Build the header menu with its MVP options and appropriate display-role filtering.
4. Build the narrative stage, character console, action composer, and dice tray with sample data.
5. Make the three views work at common laptop and TV resolutions.
6. Add keyboard focus styles and labels before adding visual effects.

Deliverable: clickable-looking static screens that can be reviewed without Python.

### Phase C: Dice tray behavior

1. Represent the six counts in one JavaScript object.
2. Wire plus and minus buttons using `data-result` attributes.
3. Prevent negative values.
4. Generate the human-readable summary from the object.
5. Generate the exact `dice_result` string expected by the backend.
6. Add a clear/reset action.

Deliverable: a tray that can be tested independently of the GM.

### Phase D: Mock-mode application behavior

1. Add mock campaign data and assign the existing character files to the first campaign.
2. Implement `loadCampaigns`, `loadCharacters`, `loadState`, `stageIntent`, and `resolveScene` functions with the same return shapes as the real API.
3. Use a short fake delay for campaign loading, character loading, and resolving so loading states can be designed.
4. Test campaign selection before character selection, empty input, zero dice, multiple dice types, and repeated staging.

Deliverable: a complete rehearsal of the player workflow without a server.

### Phase E: Connected API behavior

1. Replace mock functions with `fetch` calls behind the same function names.
2. Add campaign ID, character ID, player-console ID, and claim/release requests where the backend supports them.
2. Keep the character object and all state update logic in the response-rendering layer.
3. Refresh state after every successful resolution.
4. Handle network errors without clearing the draft or staged actions.
6. Test two player consoles claiming different characters, refreshing availability, handling a `409` conflict, releasing a claim, and reclaiming it.
7. Test three browser windows together: one narrative display and two player consoles.
8. Test using the running FastAPI server.

Deliverable: text actions and dice rolls can travel from the browser to the Python holding pen and back as narration.

### Phase F: Audio and polish

1. Add TTS only after text resolution is reliable.
2. Add the hold-to-talk control only after a transcription endpoint exists.
3. Add model selection when the backend exposes a model setting.
4. Add animations sparingly: entry fade-in, resolving indicator, and tracker update.
5. Playtest with real reading distance, low room lighting, and the actual TV and laptop resolutions.

The title-screen animation is optional polish. Do not begin it until the static waiting state and the full campaign-to-resolution workflow are working.

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
- A campaign must be selected before its characters are shown.
- A player can select a character from the selected campaign.
- The header menu provides Change Campaign without deleting campaign data.
- The narrative display can run without exposing player input controls.
- The narrative display shows a title/waiting state instead of a blank panel before the first scene.
- Two player consoles can select different characters in the same campaign.
- Wounds and strain show readable `current / threshold` values.
- A player can switch between IC and OOC.
- Empty actions cannot be staged.
- The six dice counters increment, decrement, clear, and serialize correctly.
- A staged action displays its character and roll summary.
- Resolve shows a loading state and then adds narration.
- Connected mode calls the three current API endpoints successfully.
- State is refreshed after resolution rather than guessed by the browser.
- Backend errors preserve user-entered text and explain how to retry.
- The interface is usable with keyboard controls at common laptop and TV resolutions.
- Raw state-update JSON is never displayed to players.
- The visual system uses CSS custom properties so future skins can change decorative appearance without changing semantic UI behavior or any protected functional colors.
- TTS and STT are clearly marked unavailable until their backend hooks exist.
- Any title-screen animation is optional, low-motion, and does not block core gameplay.

## 11. Working Agreement

Luckii owns:

- Information hierarchy.
- Mockups, visual language, layout, CSS, and interaction feel.
- Manual playtesting notes for all three display roles.

Hrothgar owns or supports:

- API contract changes.
- FastAPI integration and CORS/network setup.
- Mechanics parsing and state persistence.
- Audio endpoints and deployment details.

Before connected campaign selection is built, Hrothgar should confirm the campaign data model and the IDs used for campaigns and characters.

Review together at the end of each phase. Keep the interface understandable before making it ornate. The most valuable early question is: can a player glance at the screen, understand the current state, stage an action, and tell what is waiting to be resolved?
