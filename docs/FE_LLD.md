# Geminisys Frontend Low-Level Design

**Project:** Geminisys / Omni-Director
**Audience:** Luckii (UI owner), with backend support from Hrothgar (software engineer)
**Status:** MVP implementation specification
**Primary recommendation:** Local web app using HTML, CSS, and JavaScript, served by the Python backend

## 1. Purpose and Scope

This document turns the presentation-layer requirements in the backend LLD and the current OpenAPI contract into an implementable frontend plan.

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
- A phase-aware session view for intent collection, pool assignment, roll collection, and resolution.
- TTS controls represented in the UI, with playback integration added after the MVP.

The MVP is designed for desktop and laptop displays. A mobile layout is explicitly out of scope for now.

The frontend should work in two modes:

1. **Mock mode:** uses local sample data and fake responses so the interface can be designed and tested without a running backend.
2. **Connected mode:** calls the FastAPI endpoints described in section 7. The OpenAPI document is authoritative when this document and an older example disagree.

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

The campaign is selected before the character. Once a campaign is selected, the character dropdown is populated from that campaign's `GameState.characters` collection. A player cannot select a character from another campaign. The current backend does not expose character claims, availability, or a separate character-list endpoint; those are future extensions.

For the MVP, the display role can be chosen through a setup control or an optional client-side URL parameter, such as `?view=narrative` or `?view=player`; this parameter is not part of the API contract. The player view selects a campaign, fetches `GET /api/campaigns/{campaign_id}`, then selects a character and fetches `GET /api/campaigns/{campaign_id}/characters/{character_id}`. The narrative view selects only a campaign. The selected campaign ID is the only campaign value the client should persist; the current API does not provide a campaign display name or description.

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
| Scene phase | Pending submissions | Connection                  |
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
| Pending actions and rolls | Phase status        |
+---------------------------------------+
```

The two player consoles are independent instances of the same UI, showing different selected-character data within the same campaign. The narrative display is also independent, but all three views must poll the campaign endpoint and react to its `scene_status`; there is no resolve endpoint or real-time subscription in the current contract. Responsive mobile behavior is not required for the MVP; use stable desktop dimensions and test common laptop and TV resolutions instead.

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
- Model label: show `Flash`/`Pro` only when the backend exposes model metadata; otherwise show an unavailable state.
- TTS toggle and replay-last-narration button.

The header is informational and should not compete visually with the narrative.

#### Header menu

The header should include a small menu for secondary actions. Keep immediate gameplay actions such as `Stage Action` and the phase-appropriate submission control visible on the page rather than hiding them in this menu.

MVP menu options:

- **Change Campaign:** return to campaign selection and clear the current window's selected character. The shared campaign session should not be deleted or reset by this action.
- **Audio:** access TTS on/off and replay-last-narration controls.
- **Connection Status:** show the current connection state and provide `Retry` when the backend is unavailable.
- **Reset View:** restore this window's view and local UI preferences without changing campaign or character data.

Future options:

- **Change Character:** keep this available as a later option for player consoles if the use case grows to require switching characters during a session. It is not required for the current MVP workflow.
- **Claim/release character:** add only when the backend exposes the claim contract described in the backend LLD.

The menu should be available on all display roles, but it should show only options that make sense for the current window. For example, a narrative display should not show player-character actions.

### 3.3 Campaign selector

The campaign selector is the first workflow step. It should show available campaigns as a simple list or dropdown. The current `CampaignSummary` contains only `id` and the hypermedia `_link`, so the UI should use the ID as the fallback label and must not require a name or description. The client may follow the supplied link when loading the campaign resource.

Behavior:

- No character dropdown is shown until a campaign is selected.
- Selecting a campaign stores its stable campaign ID, not only a display label.
- The player view requests `GET /api/campaigns/{campaign_id}` and populates the character selector from `GameState.characters`.
- Character summaries currently contain `id`, `name`, and the hypermedia `_link`; they do not contain an availability flag. The client may follow the supplied link to load the full character resource.
- Refresh the campaign state on a modest polling interval, such as every 5 seconds, and after submitting an intent or roll.
- Character selection is currently a local window choice. Do not send a claim request because no claim endpoint exists in the current API.
- The narrative view enters the shared stage after campaign selection.
- A `Change Campaign` control returns to this screen and clears the selected character for that window. It must not delete or reset campaign data.

### 3.4 Narrative stage

Responsibilities:

- Render a chronological list of entries.
- Distinguish player actions from GM narration.
- Keep the newest entry visible after a successful resolution.
- Render mechanics as a separate, high-contrast callout under the relevant narration when the backend provides mechanics data.
- Render the title/waiting state when there is no active scene to display.
- Render the backend's `scene_status` and pending dice pools so players know which submission is expected.

The current API returns `narrative_log` as an array of strings rather than structured entries. Until the backend adds speaker, timestamp, and mechanics fields, render each string as a narrative entry without inferring its speaker. A mechanics callout remains a future backend response capability.

An entry may eventually have:

- Speaker label: `GM`, `WARLOCK`, or `LUCKII`.
- Optional timestamp.
- Main text.
- Optional mechanics list.

Do not show raw `[STATE_UPDATE: ...]` data in the UI. The backend interceptor owns that operation. The current backend does not yet return a separate mechanics collection, so the frontend must not parse mechanics or state-update blocks itself.

### 3.5 Character console

This is a reusable player-console component, not a separate Warlock screen and Luckii screen. Render it twice with the selected character record as its data input. Do not create character-specific markup or layouts unless a future gameplay requirement genuinely differs between characters.

Displays the selected character's:

- `character_name`, `player_name`, archetype, and career when present.
- Wounds as `current / threshold`.
- Strain as `current / threshold`.
- Soak value and defense as small secondary statistics.
- Optional compact inventory summary from the character sheet.

The character dropdown belongs here, above the character name. It is populated from the selected campaign and is independent in each player-console window. The two players may therefore choose different characters while remaining in the same campaign.

Tracker behavior:

- Wounds fill from green through amber to coral as current value approaches threshold.
- Strain uses cyan.
- The numeric value is always visible above or inside the bar.
- Values must not be editable in the player console. They are refreshed from `GET /api/campaigns/{campaign_id}` and, when needed, `GET /api/campaigns/{campaign_id}/characters/{character_id}` after the backend advances the scene.

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
- OOC mode is a frontend presentation choice for now. Since `PlayerIntent` has no mode field, the client may prepend `[OOC]` to `action_text` but must treat that convention as temporary.
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

When the player submits a roll, the serialized result is:

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
- Current phase and submission status.

There is no `Resolve Scene` endpoint in the current API. The backend advances the four-phase loop when the required intents and rolls have been received. The UI should therefore show the current phase and disable controls that do not apply to that phase:

- `INTENT_COLLECTION`: show the action composer and submit `POST /api/campaigns/{campaign_id}/intents`.
- `POOL_ASSIGNMENT`: show a waiting state while the backend prepares pools.
- `ROLL_COLLECTION`: show `pending_rolls` and the dice tray; submit `POST /api/campaigns/{campaign_id}/rolls`.
- `RESOLUTION`: show a resolving state and poll until the backend returns to `INTENT_COLLECTION`.

## 4. Client State Model

The browser maintains presentation state only:

```js
{
  mode: "mock" | "connected",
  connection: "loading" | "connected" | "error",
  displayRole: "campaign-selector" | "narrative" | "player",
  campaigns: [],
  selectedCampaignId: null,
  campaignCharacters: [],
  activeCharacterId: null,
  playerConsoleId: null,
  characters: {},
  sceneStatus: "INTENT_COLLECTION",
  narrativeLog: [],
  pendingRolls: {},
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

The backend remains the source of truth for character data and campaign state. After an intent or roll submission, the frontend must fetch `GET /api/campaigns/{campaign_id}` again rather than trying to predict phase changes, pending pools, or character values.

Each browser window stores its display role, selected campaign ID, and, for a player console, selected character ID. These selections are window-specific UI state. The campaign itself and the character files remain backend state.

## 5. Interaction Flows

### 5.1 Boot and campaign selection

1. Render the app shell immediately with a loading status.
2. Request `GET /api/campaigns`; the response is an array of `CampaignSummary` objects.
3. Show the campaign selector unless a valid campaign ID was supplied for a previously configured window.
4. After campaign selection, request `GET /api/campaigns/{campaign_id}` and use its `characters` array.
5. Narrative view enters the narrative display; player view shows the character dropdown.
6. Refresh campaign state periodically or after a submission.
7. After character selection, request `GET /api/campaigns/{campaign_id}/characters/{character_id}` and populate that player's console.
8. If a request fails, preserve the selection and show a clear retry control.

### 5.2 Stage a text action

1. Player selects a campaign if one is not already active.
2. Player selects their character from the campaign's character dropdown.
3. Player selects IC or OOC.
4. Player types an action.
5. Player optionally creates a dice result.
6. Send `POST /api/campaigns/{campaign_id}/intents` with `character` and `action_text`.
7. On the `202` response, refresh campaign state and show the submitted action as local pending UI until the backend exposes structured action entries.

### 5.3 Submit a roll and follow resolution

1. Wait for `scene_status` to become `ROLL_COLLECTION`.
2. Show each character's `pending_rolls` pool and reason.
3. Player enters the physical result in the dice tray.
4. Send `POST /api/campaigns/{campaign_id}/rolls` with `character` and `dice_result`.
5. Refresh campaign state after the `202` response.
6. During `RESOLUTION`, show a resolving state and continue polling.
7. When the backend returns to `INTENT_COLLECTION`, render the updated `narrative_log` and refresh character sheets.

### 5.4 Hold-to-talk, later

For the first release, the button can show `Voice input unavailable` and remain disabled. Later it should have three states: Ready, Recording, and Transcribing. Releasing the button sends audio to the backend, then places the returned transcription into the action field for review before staging.

### 5.5 TTS, later

Use the browser's audio element or Web Speech API for an initial prototype. The replay button must be disabled when no narration exists. The backend can replace this with ElevenLabs/OpenAI audio later without changing the narrative component.

## 6. Error, Loading, and Empty States

These are part of the design, not polish to add at the end.

- Loading: skeleton blocks or concise `Loading session...` labels.
- No narrative: show the narrative display title state with `Awaiting first scene` rather than an empty panel.
- No pending submission: show the action required by the current `scene_status`.
- Backend unavailable: show the problem, preserve the draft, and offer `Retry`.
- Intent or roll failure: retain the draft or dice counts and show a recoverable error.
- Invalid state data: show the character name and `Character data unavailable`; do not render broken bars.
- Long narration: keep the stage scrollable and preserve paragraph breaks.

## 7. Backend Contract

The OpenAPI document at `api/omni-director-api.yaml` is the source of truth. The current backend is campaign-scoped and exposes four operations used by the frontend. Campaign and character summaries include hypermedia `_link` fields; the frontend may use those links instead of reconstructing resource URLs, while treating the documented path parameters as the canonical route shape. Its state-machine and Gemini behavior are still scaffolding: `GET` currently reports `INTENT_COLLECTION`, while intent and roll handlers acknowledge requests without advancing state or returning narrative results. The frontend should implement the contract and show the resulting waiting states without inventing those transitions locally.

### `GET /api/campaigns`

Returns an array of `CampaignSummary` objects. Each object currently contains:

```json
{
  "id": "cyberpunk-heist",
  "_link": "http://localhost:8000/api/campaigns/cyberpunk-heist"
}
```

The campaign directory is the current persistence boundary. The UI should use `id` as the label until campaign metadata is added.

### `GET /api/campaigns/{campaign_id}`

Returns the current `GameState`:

```json
{
  "scene_status": "INTENT_COLLECTION",
  "narrative_log": ["..."],
  "pending_rolls": {},
  "characters": [
    {
      "id": "warlock",
      "name": "Warlock",
      "_link": "http://localhost:8000/api/campaigns/cyberpunk-heist/characters/warlock"
    }
  ]
}
```

The frontend should poll this endpoint for synchronization. `scene_status` is an enum with `INTENT_COLLECTION`, `POOL_ASSIGNMENT`, `ROLL_COLLECTION`, and `RESOLUTION`. `pending_rolls` maps character IDs or names to a pool and reason.

### `GET /api/campaigns/{campaign_id}/characters/{character_id}`

Returns a full `GenesysCharacterSheet` validated against `api/genesys.schema.json`. The UI should read wounds and strain from `derived_attributes.wounds` and `derived_attributes.strain`, and should not assume that optional fields such as inventory, weapons, talents, or narrative profile are present.

### `POST /api/campaigns/{campaign_id}/intents`

Request:

```json
{
  "character": "Warlock",
  "action_text": "I vault the table and shoot the bounty hunter."
}
```

The response is HTTP `202` with a `MessageResponse`:

```json
{ "message": "Intent successfully queued" }
```

The current `PlayerIntent` schema has no dice-result or input-mode field. Dice are submitted separately during roll collection, and any OOC prefix is a temporary frontend convention.

### `POST /api/campaigns/{campaign_id}/rolls`

Request:

```json
{
  "character": "Warlock",
  "dice_result": "2 Success, 1 Threat"
}
```

The response is HTTP `202` with:

```json
{ "message": "Roll successfully queued" }
```

There is currently no legacy `/api/state`, `/api/intent`, or `/api/resolve` endpoint, nor a separate character-list, claim, or release endpoint. The frontend must not depend on those routes. A shared `Resolve Scene` button is not part of the current workflow; the backend state machine is intended to advance after the required submissions are received.

Future contract extensions may add structured narrative entries, mechanics callouts, claim leases, campaign metadata, OOC mode, and an explicit resolution response. Those additions should be reflected here only after they are added to the OpenAPI contract.

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
2. Implement `loadCampaigns`, `loadCampaignState`, `loadCharacter`, `submitIntent`, and `submitRoll` functions with the same return shapes as the real API.
3. Use a short fake delay for campaign loading, character loading, and phase transitions so loading states can be designed.
4. Test campaign selection before character selection, empty input, zero dice, multiple dice types, repeated intent submission, and roll submission.

Deliverable: a complete rehearsal of the player workflow without a server.

### Phase E: Connected API behavior

1. Replace mock functions with `fetch` calls behind the same function names.
2. Keep campaign and character IDs in the client and use each resource's hypermedia `_link` when following campaign or character resources; do not assume display metadata beyond the fields in the summaries.
3. Keep the character object and all state update logic in the response-rendering layer.
4. Poll campaign state after every successful intent or roll and while the backend is in `POOL_ASSIGNMENT` or `RESOLUTION`.
5. Handle network errors without clearing the draft or dice counts.
6. Test two player consoles selecting different characters, submitting intents, observing pending pools, and submitting rolls.
7. Test three browser windows together: one narrative display and two player consoles.
8. Test using the running FastAPI server.

Deliverable: text actions and dice rolls can travel from the browser to the campaign-scoped FastAPI endpoints, with phase and state updates displayed when the backend implementation is complete.

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
- Each `scene_status` renders the correct controls and waiting state.
- Connected mode calls the current campaign, character, intent, and roll endpoints successfully.
- State is refreshed after intent and roll submissions rather than guessed by the browser.
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

Before connected campaign selection is built, Hrothgar should confirm the campaign display metadata and whether character claims are needed. The current implementation uses campaign folders and the character file stems (`warlock` and `luckii`) as IDs.

Review together at the end of each phase. Keep the interface understandable before making it ornate. The most valuable early question is: can a player glance at the screen, understand the current state, stage an action, and tell what is waiting to be resolved?
