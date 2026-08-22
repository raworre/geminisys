# Geminisys Creator API Review

**Purpose:** Questions, comments, and concerns for the API team before the Creator frontend is mocked and implemented.

**Source reviewed:** `api/creator-api.yaml`, `api/genesys.schema.json`, and the four-phase workflow in `docs/Creator_HLD.md`.

This review is limited to the campaign and character creation flow. It does not cover the separate gameplay endpoints in `api/omni-director-api.yaml`.

## Executive Summary

The current contract is sufficient to prototype the basic chat and finalize requests. It is not yet sufficient to implement the complete HLD flow because it does not define:

- how a finalized campaign or draft character is loaded into the next phase;
- how the completed Crunch-phase character is persisted;
- how Phase 4 receives the finalized character roster and mechanical data;
- whether generation is synchronous or asynchronous; and
- how the frontend receives generated resource identifiers, data, or file links.

The most important request is to define the phase handoffs and persistence contract before frontend implementation begins.

## Blocking Questions

### 1. Define the phase handoffs

The HLD describes this flow:

```text
Campaign chat -> campaign generation -> character chat -> draft character
-> character crunch -> finalized character -> campaign ignition -> final files
```

The OpenAPI contract only exposes chat and finalize commands. Please define how the frontend obtains the result of each phase.

Questions:

- After `campaignFinalize`, how does the frontend load the generated campaign context for Phase 2?
- After `characterFinalize`, how does the frontend load the draft character's `narrative_profile` into Crunch?
- How is the completed Crunch character saved?
- Does Phase 4 receive character data through the campaign chat session automatically, or must the frontend submit a roster or character IDs?
- Is there a dedicated endpoint for each handoff, or should the finalize response include the next resource and its URL?

Suggested response shape:

```json
{
  "status": "created",
  "message": "Draft character generated",
  "campaign_id": "space-bounty",
  "character_id": "warlock",
  "resource": {
    "href": "/api/creator/campaigns/space-bounty/characters/warlock"
  },
  "next": {
    "href": "/api/creator/campaigns/space-bounty/characters/warlock/crunch"
  }
}
```

### 2. Define Crunch persistence

Phase 3 is a major HLD requirement, but `creator-api.yaml` contains no endpoint for saving the mechanically populated character.

Please decide:

- Is Crunch data saved locally by the browser, submitted to the backend, or both?
- Is there a `PUT` or `PATCH` endpoint for a character sheet?
- Is the submitted object the complete `genesys.schema.json` document or a partial update?
- Does the backend calculate derived attributes, or does the frontend submit them?
- Does the backend validate Genesys legality, XP spending, skill ranks, talents, gear, and characteristic limits?
- Can the player save an incomplete draft and resume later?
- What response indicates that the character is eligible for Phase 4?

The frontend should not independently enforce rules that belong to the backend. It can provide immediate form feedback, but the API needs to be authoritative.

### 3. Define character and campaign retrieval

The Creator API has no campaign-list, campaign-detail, character-detail, or roster endpoint. The frontend needs stable resource URLs and response schemas for the objects it displays.

Please provide or explicitly defer endpoints for:

- listing available campaigns;
- loading a generated campaign;
- listing characters for a campaign;
- loading a draft or finalized character;
- loading the Phase 4 character roster; and
- determining whether a character is still a draft or ready for play.

If these resources are intentionally handled by another API, please document that boundary and link to its contract.

### 4. Clarify finalization processing

Both finalize operations return `200`, but their descriptions imply file generation that may take time.

Please confirm:

- Is finalization guaranteed to complete within the request?
- Can the operation return `202 Accepted` with a job ID?
- Can the request be safely retried after a timeout?
- Is finalization idempotent for the same campaign, character, and session IDs?
- What happens if the target file already exists?
- Does the response include generated file paths, download links, resource links, or only a message?
- Can generation partially succeed, such as writing `campaign_setting.md` but failing to write `current_state.md`?

The UI needs a distinct progress, success, and failure state rather than assuming that an HTTP response means all files are available.

### 5. Clarify session lifecycle and ownership

`session_id` is returned by chat and then reused for later chat and finalization requests. Please document its lifecycle.

Questions:

- How long does a session remain valid?
- Is a session tied to a campaign, character, browser, or user?
- Can a session be resumed from another browser?
- Can the frontend explicitly abandon or restart a session?
- Does a session permit multiple concurrent requests?
- What happens if two requests use the same session at once?
- Is the session ID sensitive and therefore unsuitable for display or URL storage?
- Can a session be finalized more than once?

The documented `session-not-found` error should specify whether the frontend can recover by starting a new session or must ask the user to restart the phase.

### 6. Define how Phase 4 identifies characters

The Phase 4 description says the AI reads finished characters' motivations and debts, but `FinalizeCampaignRequest` contains only `session_id` and `campaign_id`.

Please clarify:

- How does the backend know which characters belong to the campaign?
- Are all finalized characters included automatically?
- Can the creator choose a subset of characters?
- Must the frontend send `character_ids` when starting or finalizing Phase 4?
- Are draft characters excluded automatically?
- What happens if no finalized characters exist?

Suggested request addition if selection is required:

```yaml
character_ids:
  type: array
  items:
    type: string
  minItems: 1
```

## Endpoint-Specific Comments

### `POST /creator/campaign/chat`

- Please state whether the first message must omit `session_id`, or whether `null` is also accepted.
- Define maximum message length and handling of blank or whitespace-only messages.
- Does the response include a campaign draft or only natural-language text?
- Is `is_complete` an AI suggestion or a backend-validated readiness state?
- Can `is_complete` change back to `false` after the user continues the conversation?
- Should the response include a conversation turn ID or message history?
- What errors represent provider timeout, rate limit, content rejection, or malformed AI output?

### `POST /creator/character/chat`

- How does the character chat receive the selected campaign context?
- Is `campaign_id` intentionally absent from `ChatRequest` because it is encoded in the session?
- If so, how is the session associated with a campaign?
- Does the response expose a structured draft narrative profile, or must the frontend wait for finalization?
- Can one session create more than one character?
- How are shared relationships between multiple character sessions represented?

### `POST /creator/campaign/finalize`

- Confirm that `campaign_id` is a new slug rather than an existing campaign ID.
- Define allowed slug characters, length, case normalization, and reserved names.
- Define the conflict response when the slug already exists.
- Return stable links or identifiers for both generated files/resources.
- State whether the generated `current_state.md` contains an opening scene or only initial state metadata.

### `POST /creator/character/finalize`

- Confirm that `campaign_id` must refer to a campaign already generated by `campaignFinalize`.
- Define the conflict response when `character_id` already exists.
- Confirm whether the generated file contains only `narrative_profile` or also identity fields such as `character_name`.
- Define how a character draft is distinguished from a Crunch-complete character.
- Return the generated character resource or a link to retrieve it.

## Response Schema Concerns

### `ChatResponse`

The response currently contains `session_id`, `response`, and `is_complete`. Please consider adding:

- `phase` or `assistant_role` so the frontend can confirm the session context;
- a message or turn ID;
- an optional structured draft or summary;
- a server timestamp; and
- links to the active session or next operation.

Please also define whether `response` is always clean display text. The frontend should not parse hidden control markers, JSON, or file-generation instructions from AI text.

### `SuccessResponse`

`status` and `message` are too generic for reliable UI transitions. Please consider a shared operation response containing:

- a stable machine-readable `status` enum;
- the operation or job ID;
- resource identifiers;
- resource links;
- generated artifact links; and
- an optional `next_step`.

### `Problem`

Please make the error fields and media type consistent across all operations. In particular:

- Is `status` an integer rather than a general number?
- Is `type` always a URI, including the `urn:geminisys:error:*` values?
- Which fields are required?
- Is `instance` a request ID, resource URI, or both?
- Does the response include a machine-readable error code separate from `title`?
- Can validation errors identify the offending field?

Suggested validation detail:

```json
{
  "type": "urn:geminisys:error:validation",
  "status": 400,
  "title": "Invalid character sheet",
  "detail": "Available XP cannot be negative.",
  "errors": [
    {
      "field": "experience.available",
      "code": "minimum",
      "message": "Must be greater than or equal to 0."
    }
  ]
}
```

## Validation and Domain Rules

Please document validation for:

- campaign and character slug format;
- message length and content limits;
- duplicate or conflicting sessions;
- whether AI completion is required before finalization;
- whether character finalization requires an existing campaign;
- required fields in the narrative profile;
- required fields in a completed character sheet;
- characteristic bounds of 1 through 6;
- skill rank bounds of 0 through 5;
- talent tier bounds of 0 through 5;
- nonnegative derived attributes and inventory quantities; and
- XP budget and spending rules.

The API should reject invalid sheets with field-level errors. A frontend-only validation layer is useful for usability but cannot replace server-side validation.

## Security and Operational Questions

The OpenAPI document currently declares `security: []`. Please confirm whether this is intentional for local-only use.

Also clarify:

- whether session IDs or generated content should be treated as private;
- whether chat content is logged or sent to an external AI provider;
- whether rate limits or request size limits apply;
- whether CORS is configured for the local frontend origin; and
- whether the API exposes correlation IDs for troubleshooting failed generation.

## Recommended Priorities

1. Define the resource and persistence contract for Crunch and phase handoffs.
2. Define how Phase 4 identifies and loads finalized characters.
3. Clarify finalization job behavior, idempotency, conflicts, and generated artifact access.
4. Document session lifecycle, association, expiration, and recovery.
5. Add complete response schemas and stable machine-readable error codes.
6. Document slug, message, character-sheet, and XP validation rules.
7. Add retrieval/list endpoints or document the API boundary where they already exist.
8. Add optional UX improvements such as structured draft summaries and progress metadata.

## Frontend Assumptions Until Resolved

- The frontend retains `session_id` for the active phase and sends it on subsequent chat and finalize requests.
- `is_complete` is displayed as an AI readiness suggestion, not treated as proof that finalization will succeed.
- Finalization errors preserve the user's current context and allow retry.
- The frontend will not parse raw AI control markers or modify generated files directly.
- Crunch fields can be mocked locally, but production persistence requires an API decision.
- Phase 4 character selection can be mocked for visual design but cannot be implemented reliably until roster access is defined.
- Generated files can be shown as completed artifacts, but preview/download buttons should remain provisional until links or endpoints are specified.

## Requested API-Team Response

Please respond with:

1. Which blocking questions are already answered by existing backend behavior.
2. Which answers require OpenAPI changes.
3. Which missing endpoints belong in the Creator API versus another API.
4. Whether the frontend should design around synchronous finalization or an asynchronous job model.
5. The expected delivery order for the contract changes.