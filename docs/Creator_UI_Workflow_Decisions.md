# Creator Workflow Decisions

**Status:** Working decision log
**Last reviewed:** 2026-08-22

This file records decisions and unresolved questions for the Geminisys Creator workflow. It is intentionally separate from the workflow brief so the brief can remain readable while the project direction changes.

**Terminology:** In this log, **Creator** means the UI for the entire **Creation phase**. The Creation phase is the complete campaign and character creation process, made up of multiple Creation stages. The **Play phase** begins when the campaign starts and the created characters are in use.

## Decided

### Initial product scope

**Decision:** Creation phase first; Play phase later.

**Why:** Creation produces the campaign and characters; Play begins afterward when those characters are in use and gameplay actions occur. The two major phases have different workflows and should not be mixed.

### First artifact

**Decision:** Create a project-specific Figma and frontend workflow brief.

**Why:** This preserves design intent and implementation context before coding.

### Frontend direction

**Decision:** Use plain HTML, CSS, and JavaScript.

**Why:** This matches the existing repository and avoids framework setup before the flow is validated.

### Prototype mode

**Decision:** Build and review mock mode before connected mode.

**Why:** The flow can be evaluated without depending on incomplete AI or backend behavior.

### Figma setup

**Decision:** Assume a new free-plan catalogue for now.

**Why:** No existing Figma constraints have been supplied. Plan and plugin limits will be verified before relying on automation.

### Responsive scope

**Decision:** Start with desktop and laptop layouts.

**Why:** This matches the current Creator and gameplay planning. Mobile targets have not yet been defined.

### Authority boundary

**Decision:** The backend owns AI, legality, XP, persistence, and generated files. The frontend owns presentation and data binding.

**Why:** This prevents the browser from duplicating domain rules or mutating project state directly.

### Figma backup boundary

**Decision:** Figma cloud and version history are the active design source. Local `.fig` backups are recovery copies only, and the backend must not read from the backup folder.

**Why:** Design files express visual intent; they are not campaign state, character data, API configuration, or runtime input. Any future design-token or asset import must be an explicit, validated handoff pipeline.

## Open Questions

- What are the exact response schemas for Creator crunch operations?
- How does each Creation stage hand off data to the next stage?
- How is a completed Crunch sheet persisted and retrieved?
- Are generation operations synchronous or job-based?
- What are the retry and idempotency rules for finalization?
- How long do sessions live, and how are expiration and concurrent requests handled?
- How does the Campaign Ignition stage receive and validate the finalized character roster?
- How are draft and finalized character states represented?
- What artifact links or stable resource IDs does the backend return?
- Which desktop/laptop resolutions must be treated as acceptance targets?
- What Figma plan, plugin, and export constraints apply?

## Change Protocol

When a decision changes:

1. Update the relevant decision entry.
2. Add the previous direction and the reason for changing it under a dated entry below.
3. Update `docs/Creator_Frontend_Workflow.md` only after the new direction is agreed. Update `docs/Figma_Beginner_Guide.md` only when the general Figma instructions change.
4. Review affected API mappings, screens, and verification steps.

## Change History

_No changes recorded yet._
