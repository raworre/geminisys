# Geminisys Creator: Figma and Frontend Workflow

**Status:** Working draft
**Scope:** Creator-first design and frontend planning
**Last reviewed:** 2026-08-22

> This document is a project-specific working draft. It preserves the current direction while design, API, and product questions are still open. Do not treat it as an implementation contract until the open decisions are resolved.

## 1. Purpose

Define a practical handoff from Figma to the Geminisys Campaign and Character Creator. Figma owns visual intent and interaction presentation. The frontend owns behavior, state, accessibility, responsive behavior, API integration, and performance. The backend remains authoritative for AI output, Genesys legality, XP calculations, persistence, and generated files.

The immediate product track is the Creator. The gameplay VTT described in `docs/FE_LLD.md` is a later, separate track and should not be mixed into the first Creator catalogue.

## 2. Current Product Context

Geminisys is a local-first Genesys VTT project. The Creator is intended to generate:

- `campaign_setting.md`
- `current_state.md`
- `character.json`

The current frontend direction is a plain local web app using HTML, CSS, and JavaScript. No frontend framework or build system is currently configured. The Creator should begin in mock mode so its flow can be reviewed without a running AI or backend implementation.

The Creator flow has four phases:

1. **Sandbox Pitch:** Socratic campaign and setting chat.
2. **Character Concepts:** Socratic character chat producing a narrative draft.
3. **Character Crunch:** Player-controlled mechanical character building with optional guided advice.
4. **Campaign Ignition:** Campaign chat uses finalized characters to create the opening plot and campaign files.

## 3. Contract Gate

Before connected frontend work is considered complete, the backend team must clarify the following items. The UI may show provisional or unavailable states, but it must not invent production behavior for these gaps.

- Exact response shapes for crunch initialization, buy, refund, finish, and generated resources.
- How campaign and character data move between Creator phases.
- How the completed Crunch sheet is persisted and retrieved.
- Whether finalization is synchronous or asynchronous, including progress, retry, and idempotency behavior.
- Session lifetime, ownership, expiration, concurrency, and recovery.
- How Phase 4 receives the finalized character roster.
- Draft versus finalized character status.
- Field-level validation and authoritative XP/legal-purchase errors.
- Generated artifact links or stable resource identifiers.

The current Creator API surface is documented in `api/creator-api.yaml` and includes:

- `GET /api/rules/skills`
- `GET /api/rules/talents`
- `POST /api/creator/campaign/chat`
- `POST /api/creator/campaign/finalize`
- `POST /api/creator/character/chat`
- `POST /api/creator/character/save`
- `POST /api/creator/character/finalize`
- `POST /api/creator/character/crunch/start`
- `GET /api/creator/character/crunch/{campaign_id}/{character_id}`
- `PATCH /api/creator/character/crunch/buy`
- `PATCH /api/creator/character/crunch/refund`
- `POST /api/creator/character/crunch/finish`

The API review in `api/creator-api_review.md` is the active list of contract questions.

## 4. Figma Catalogue

Create one new catalogue file, assuming a free plan until plan and plugin limits are verified. Use these pages:

- `00 Read Me`: scope, ownership, status, open questions, and links to API/schema documents.
- `01 Foundations`: semantic color, typography, spacing, borders, focus, motion, and accessibility tokens.
- `02 Components`: reusable components and variants.
- `03 Creator Screens`: the four phase screens and completed-result views.
- `04 States and Flows`: loading, empty, disabled, validation, retry, unsaved changes, and failure flows.
- `05 Handoff Exports`: annotated frames, asset exports, endpoint mappings, and implementation notes.
- `99 Archive`: superseded explorations and rejected directions.

Keep the gameplay VTT out of this first catalogue. Add it later as a separate page or file once the Creator contract and workflow are stable.

## 5. Figma Setup Walkthrough

This is the practical first-session setup for creating the catalogue. The names below align the original VTT tutorial with the Creator-first catalogue defined above.

### Step 1: Create the file

1. Go to Figma.com and create a free account.
2. When prompted to create a team, select **Skip** to remain in the personal workspace.
3. From the home dashboard, select **Drafts**.
4. Select **+ Design file**.
5. Rename the file to `Geminisys_Creator_UI_Catalogue`.

Verify the free-plan limits, sharing permissions, export options, and any plugin requirements before relying on automation. `VTT_Master_UI_Catalogue` remains a reasonable alternative if the catalogue later expands to include the gameplay VTT.

### Step 2: Learn the workspace

Figma has three main work areas:

- **Left navigation and Layers panel:** pages and every element on the current canvas.
- **Center canvas:** the infinite workspace for frames, components, and screen layouts.
- **Right Properties panel:** dimensions, colors, typography, Auto Layout, and export settings.

### Step 3: Create the catalogue pages

Rename the initial page and add the remaining pages in this order:

- `00 Read Me`
- `01 Foundations`
- `02 Components`
- `03 Creator Screens`
- `04 States and Flows`
- `05 Handoff Exports`
- `99 Archive`

The simpler tutorial names map as follows: **Design System & Tokens** to `01 Foundations`, **Master Components** to `02 Components`, **Screen Mockups** to `03 Creator Screens`, **Asset Export Board** to `05 Handoff Exports`, and **Visual History** to `99 Archive`.

### Step 4: Essential shortcuts

Use these six shortcuts while building standard interface elements:

- `F`: create a Frame.
- `T`: create Text.
- `R`: create a Rectangle.
- `Shift + A`: apply Auto Layout to the selection.
- `Ctrl + Alt + K` on Windows or `Cmd + Option + K` on Mac: create a Component.
- `Spacebar + click and drag`: pan around the canvas.

### Step 5: Create the first reusable button

Use the `02 Components` page for the exercise:

1. Press `T`, click the canvas, and type `CONTINUE TO CRUNCH`.
2. Use a bold, readable placeholder font at approximately 14px. Inter or Roboto is acceptable for this first exercise; choose and document the final type family during the Foundations pass.
3. With the text selected, press `Shift + A` to wrap it in an Auto Layout frame.
4. Add a temporary dark shell fill such as `#1E1E2E`.
5. Set horizontal padding to 16px and vertical padding to 8px.
6. Set the corner radius to 6px or less.
7. Select the frame and choose **Create Component**, or press `Ctrl + Alt + K` on Windows.

The button is now a reusable component. Keep its label and state behavior generic so it can later support actions such as **Save Draft**, **Retry**, or **Finalize Campaign**. The final palette may change; use semantic token names rather than treating this placeholder fill as permanent.

### Step 6: Place and update an instance

1. Open `03 Creator Screens`.
2. Press `F` and create a desktop frame, such as 1920 x 1080, for an initial screen mockup.
3. Return to `02 Components`, copy the button component, and paste an instance into the screen frame.
4. Return to the main component and change its temporary background fill, for example to the provisional amber attention color.
5. Confirm that the instance on `03 Creator Screens` updates automatically.

This demonstrates the intended Figma workflow: shared visual decisions are made in the component source, while screen mockups use instances. Keep behavior, validation, API calls, and responsive rules in the frontend handoff annotations rather than attempting to encode them only in Figma.

## 6. Visual Foundations

Use a neutral tabletop direction rather than a setting-specific skin. The interface should feel tactile and game-oriented while remaining readable for long chat sessions and dense character forms.

Recommended starting language:

- Near-black blue-gray application shell.
- Warm ivory narrative and form text.
- Amber for attention, pending, or unsaved states.
- Cyan for information and secondary status.
- Coral/red for validation danger or blocked actions.
- Muted green for confirmed or healthy states.
- Small square corners or a maximum 6px radius.
- A display face for labels and a highly readable text face for chat and explanations.

Use semantic CSS custom-property names for color, type, spacing, border, and motion values. Functional meanings must also be communicated through text, labels, position, or icon shape; color must never be the only signal. Future skins may change decoration but must not repurpose functional status colors.

Define and test:

- Keyboard-visible focus states.
- Contrast for chat, controls, helper text, and status messages.
- Reduced-motion behavior.
- Long-message wrapping and scroll behavior.
- Disabled, loading, and error affordances.
- Stable dimensions for controls so dynamic content does not shift layouts.

## 7. Component Set

Build ordinary UI components with Auto Layout and variants. Do not force Auto Layout onto spatial or canvas-based surfaces; no map or canvas surface is part of the Creator MVP.

Core components:

- App shell and header.
- Four-step phase indicator.
- Chat transcript and message composer.
- Session/status banner.
- Completion gate and confirmation dialog.
- Campaign slug and metadata fields.
- Character identity and narrative-profile summary.
- Guided/Veteran mode toggle.
- Crunch characteristic, skill, and talent controls.
- XP ledger and remaining-budget indicator.
- Upgrade and refund controls.
- Field validation and API problem message.
- Save, continue, retry, and finalize actions.
- Loading/progress, success, failure, and unavailable states.
- Unsaved-change warning.

Each component should have variants for normal, hover/focus, disabled, loading, success, validation error, and unavailable states where applicable.

## 8. Screen Inventory

Design desktop-first screens for:

### Shared states

- Initial loading.
- Backend unavailable with retry.
- Session expired with recovery path.
- Unsaved changes.
- Operation in progress.
- Operation succeeded.
- Operation failed without losing user input.

### Phase 1: Sandbox Pitch

- Empty campaign chat.
- Active conversation.
- Completion suggestion or completion gate.
- Campaign slug and finalize confirmation.
- Campaign generation progress, success, and failure.

### Phase 2: Character Concepts

- Character chat with campaign context.
- Active character conversation.
- Narrative draft review.
- Draft save progress, success, and failure.
- Transition into Crunch when the backend confirms the draft.

### Phase 3: Character Crunch

- Crunch initialization and sheet loading.
- Narrative profile alongside mechanical sheet.
- Guided-advice mode.
- Veteran/manual mode.
- Characteristic, skill, and talent editing.
- XP spent and remaining states.
- Successful purchase and refund.
- Insufficient XP, invalid upgrade, and field validation errors.
- Unsaved changes and draft reload.
- Finish eligibility confirmation and completion result.

### Phase 4: Campaign Ignition

- Campaign chat with finalized character context.
- Character roster or roster-unavailable state.
- Opening-hook review.
- Campaign finalization confirmation.
- Artifact generation progress, success, failure, retry, and completed result.

## 9. Behavioral Handoff Rules

Annotate each interactive component and screen with:

- Owning client state.
- API operation and request payload.
- Response fields required to continue.
- Server-authoritative validation rules.
- Whether an update is optimistic or confirmed by the server.
- Retry behavior and preserved fields.
- Session ID, campaign ID, and character ID handling.
- Keyboard and screen-reader semantics.
- Navigation guards for incomplete or unsaved work.

The browser may retain presentation state and session/resource identifiers. It must not calculate final XP legality, mutate character files, parse hidden AI control markers, or guess whether generation succeeded.

## 10. Frontend Implementation Sequence

Keep the prototype small and framework-free:

```text
frontend/
  index.html       # semantic Creator shell
  styles.css       # tokens and layout
  app.js           # client state, rendering, and event handlers
  mock-data.js     # sample responses and fake delays
```

Build in this order:

1. Semantic shell and phase navigation.
2. Mock chat for Phases 1, 2, and 4.
3. Mock draft save and Crunch sheet.
4. Mock buy/refund, validation, XP feedback, and finish.
5. Mock final campaign generation and artifact result.
6. Connected `fetch` adapters behind the same function names.
7. Contract-specific loading, error, retry, and recovery behavior.

Store session IDs and resource IDs in client state. Render returned sheets and operation results from server responses. Preserve chat drafts, form edits, and pending operations when requests fail.

Do not add a framework during this planning cycle. Reconsider only if the plain implementation becomes difficult to maintain after the mock flow is validated.

## 11. Verification Checklist

- All four Creator phases have normal, loading, empty, disabled, validation, and failure states where relevant.
- Every interactive action has a documented endpoint, payload, response dependency, and retry path.
- Mock mode completes campaign chat, character chat, draft save, Crunch buy/refund, Crunch finish, and campaign ignition.
- Session IDs survive multiple messages and phase transitions.
- Character sheets use `api/genesys.schema.json` for field structure while backend validation remains authoritative.
- Failed requests preserve user-entered chat, form, and slug values.
- Keyboard-only navigation and visible focus work throughout.
- Text remains readable at common desktop and laptop widths.
- Reduced-motion preferences are respected.
- Connected tests distinguish missing backend implementation from frontend defects.
- Gameplay VTT screens, mobile-first layouts, WebSockets, map/canvas rendering, theme switching, STT, and TTS remain outside the first Creator deliverable.

## 12. Ownership

**Design/frontend owner:** information hierarchy, mockups, visual language, layout, CSS, interaction feel, accessibility presentation, and manual playtesting.

**Backend owner/support:** API contract, session and persistence semantics, FastAPI integration, server validation, AI generation, artifact creation, and network setup.

Review this document and the Figma catalogue together at the end of each phase. Keep the current open questions visible until the API contract resolves them.
