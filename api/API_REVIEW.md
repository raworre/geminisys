# Omni-Director API Review

**Purpose:** Questions, comments, and concerns for the API developers.

**Source reviewed:** `api/omni-director-api.yaml`, `api/genesys.schema.json`, and the frontend requirements in `docs/FE_LLD.md`.

This review is about the API contract. It does not prescribe backend implementation details. The frontend needs predictable response shapes and state semantics so that it can render the correct view without guessing game state.

## Decisions Needed

### 1. Confirm the hypermedia shape

The intended API uses hypermedia `_links` for both campaign and character resources, but the current OpenAPI document defines a singular `_link` string on `CampaignSummary` and `CharacterSummary`.

Please confirm the standard shape. For example:

```json
"_links": {
  "self": {
    "href": "/api/campaigns/cyberpunk-heist"
  },
  "characters": {
    "href": "/api/campaigns/cyberpunk-heist/characters"
  }
}
```

Questions:

- Should `_links` be an object keyed by relation names such as `self` and `characters`?
- Should each relation be a plain URL string or an object containing `href`?
- Should the frontend follow these links, or are they informational only?
- Which relations are guaranteed to exist?
- Should the OpenAPI schemas use `_links` consistently for both campaigns and characters?

### 2. Define the four-phase state contract

`GameState.scene_status` lists `INTENT_COLLECTION`, `POOL_ASSIGNMENT`, `ROLL_COLLECTION`, and `RESOLUTION`, but the contract does not fully define what each phase means to a client.

Please document:

- How the server determines that all required intents have been submitted.
- How the participating characters or players are identified.
- What happens when only some players submit an intent.
- Whether an intent can be changed or resubmitted before the phase advances.
- How the server determines which characters must submit rolls.
- What causes each transition, including the transition back to `INTENT_COLLECTION`.
- Whether clients should poll, and what polling interval is reasonable.
- Whether `scene_status` can move backward or skip a phase.

A frontend should be able to render controls from `scene_status` alone without duplicating these rules locally.

### 3. Define the contents of `pending_rolls`

`pending_rolls` is described as a map of character names to required dice pools, but the key format is not formally defined.

Questions:

- Is each key a character ID or character name? Character IDs are preferable because names can change or collide.
- Is an empty object the only representation of no pending rolls?
- Does the pool order have meaning?
- What vocabulary is used for pool entries, for example `Green`, `Yellow`, `Purple`, or another enum?
- Is `reason` always present?
- Can a character have more than one pending roll?
- Does the response indicate whether a roll has already been submitted?

Suggested schema direction:

```json
"pending_rolls": {
  "warlock": {
    "pool": ["Green", "Green", "Purple"],
    "reason": "Ranged (Light) check."
  }
}
```

The OpenAPI description should state whether `warlock` is an ID or a display name.

### 4. Decide whether submitted intents and rolls are part of `GameState`

The current `GameState` exposes the narrative, pending pools, and characters, but not the intents or rolls waiting in the current scene.

This creates a synchronization question for multiple browser windows: after one player submits an intent, how does another client know that the submission was received and which actions are still outstanding?

Please decide whether `GameState` should expose fields such as:

```json
{
  "intents": [
    {
      "character": "warlock",
      "action_text": "I search the terminal.",
      "status": "submitted"
    }
  ],
  "rolls": [
    {
      "character": "warlock",
      "dice_result": "2 Success, 1 Threat",
      "status": "submitted"
    }
  ]
}
```

If these data are intentionally private or omitted, the contract should explain how the client obtains the equivalent readiness information.

### 5. Provide structured narrative and mechanics data

`narrative_log` is currently an array of strings. The frontend requirements call for speaker labels, timestamps, paragraph text, and mechanics callouts attached to GM narration.

Please decide whether to extend the narrative entry shape, for example:

```json
{
  "speaker": "GM",
  "text": "The drone's optics clear.",
  "timestamp": "2026-08-21T18:30:00Z",
  "mechanics": [
    "Warlock takes 1 Wound"
  ]
}
```

Questions:

- Is `speaker` an enum such as `GM`, `WARLOCK`, and `LUCKII`?
- Are mechanics plain strings or structured effects?
- Should mechanics be attached to a narrative entry or returned as a separate collection?
- Does the API return clean narrative text with all `[STATE_UPDATE]` and `[MECHANICS]` markers removed?
- Should the API include an identifier for each narrative entry?

The frontend should receive parsed presentation data. It should not parse raw Gemini output or apply state updates itself.

### 6. Define the result of intent and roll submissions

The intent and roll endpoints return HTTP `202`, but their response bodies are not defined in the OpenAPI responses. A client needs to know whether the request was accepted and what to refresh next.

Please document a response schema, even if the response remains minimal. For example:

```json
{
  "message": "Intent successfully queued",
  "scene_status": "INTENT_COLLECTION",
  "_links": {
    "campaign": {
      "href": "/api/campaigns/cyberpunk-heist"
    }
  }
}
```

Questions:

- Does `202 Accepted` mean the submission was stored, or only that processing started?
- Is the returned status the status before or after accepting the submission?
- Should the client always follow a campaign link or poll the campaign resource after success?
- Is an idempotency key needed so retrying a timed-out request does not duplicate a submission?

### 7. Define input identity and ownership

`PlayerIntent.character` and `PlayerRoll.character` are strings, but the contract does not say whether they contain a character ID or display name.

Please standardize this. Character IDs are preferable for requests because display names are not guaranteed to be unique or stable.

Questions:

- Should the request field be named `character_id` instead of `character`?
- How is a player or browser console identified, if that is needed?
- Is character selection merely local to a browser, or does the API reserve characters for players?
- If reservation is required, should the API add claim and release operations?
- If reservation is not required, should the contract explicitly say that multiple clients may select the same character?

### 8. Separate input mode from action text

The frontend requirements include IC/OOC input, but `PlayerIntent` only contains `character` and `action_text`.

Prepending `[OOC]` to the text is a fragile convention because it mixes presentation metadata with player content. Please decide whether to add an explicit field:

```json
"mode": "ic"
```

with an enum such as `ic` and `ooc`.

If OOC input is out of scope for the current API, the OpenAPI description should say so and the frontend should label the control as unavailable or provisional.

## Contract Concerns

### Required fields and validation

The component schemas define properties, but most fields do not explicitly declare `required` lists. Please confirm which fields are mandatory for `CampaignSummary`, `CharacterSummary`, `GameState`, `PendingRoll`, and the character schema.

Also consider documenting constraints for:

- Empty or whitespace-only `action_text`.
- Maximum action length.
- Empty `dice_result` values.
- Allowed dice-result vocabulary and formatting.
- Whether duplicate intent or roll submissions are rejected or replace earlier submissions.

### Error responses

The endpoints document general `400`, `401`, and some `404` responses, but not the expected state-related failures.

Please document status codes and `Problem` bodies for at least:

- Campaign not found.
- Character not found in the campaign.
- Intent submitted during the wrong phase.
- Roll submitted during the wrong phase.
- Roll submitted for a character without a pending pool.
- Duplicate or conflicting submission.
- Malformed or empty request data.
- Backend processing failure during pool assignment or resolution.

The frontend needs stable error information so it can preserve the user's draft and offer a useful retry path.

### Character schema reference

The character endpoint currently references the external schema as:

```yaml
$ref: genesys.schema.json
```

Please confirm that this is valid for the OpenAPI tooling being used. If the schema is intended to be a component reference, it may need to be imported or referenced with a valid JSON Pointer, such as a separately defined component schema.

The frontend also needs the contract to clarify that optional character fields may be absent. The required tracker paths are:

- `derived_attributes.wounds.current`
- `derived_attributes.wounds.threshold`
- `derived_attributes.strain.current`
- `derived_attributes.strain.threshold`

### Campaign metadata

`CampaignSummary` currently exposes only an ID and hypermedia links. That is technically sufficient for navigation, but not sufficient for a useful campaign-selection screen.

Please decide whether to add optional metadata such as:

```json
{
  "id": "cyberpunk-heist",
  "name": "The Liminal Zone",
  "description": "A darkly comic corporate survival campaign"
}
```

If metadata is intentionally deferred, the frontend will use the campaign ID as its visible label.

## Recommended Contract Priorities

1. Standardize `_links` and document its relation format.
2. Define `GameState` phase semantics and `pending_rolls` identifiers.
3. Document response schemas for the `202` intent and roll operations.
4. Define structured narrative and mechanics data before frontend parsing is built.
5. Standardize character IDs in both request bodies and response maps.
6. Document state-specific errors and validation rules.
7. Decide whether pending intents and rolls are visible in `GameState`.
8. Add optional campaign display metadata when convenient.

## Frontend Assumptions Until These Questions Are Resolved

- The frontend treats `scene_status` as authoritative and does not calculate phase transitions.
- The frontend uses campaign and character hypermedia `_links` when following resources.
- The frontend does not parse `[STATE_UPDATE]` or `[MECHANICS]` markers.
- The frontend preserves drafts and dice counts when a submission fails.
- The frontend treats character selection as local unless the API adds an explicit reservation contract.
- The frontend uses campaign IDs as labels when no campaign name is supplied.
