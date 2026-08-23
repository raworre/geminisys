# Creator Workflow Decisions

**Status:** Working decision log
**Last reviewed:** 2026-08-22

This file records decisions and unresolved questions for the Geminisys Creator workflow. It is intentionally separate from the workflow brief so the brief can remain readable while the project direction changes.

## Decided

| Topic | Decision | Rationale |
|---|---|---|
| Initial product scope | Creator first; gameplay VTT later | The Creator has a distinct four-phase workflow and should not be mixed with the gameplay state machine. |
| First artifact | Project-specific Figma and frontend workflow brief | Preserve design intent and implementation context before coding. |
| Frontend direction | Plain HTML, CSS, and JavaScript | Matches the existing repository and avoids framework setup before the flow is validated. |
| Prototype mode | Mock mode before connected mode | Allows review without depending on incomplete AI/backend behavior. |
| Figma setup | New free-plan catalogue assumed | No existing Figma constraints have been supplied; verify plan and plugin limits before automation. |
| Responsive scope | Desktop and laptop first | Matches the current Creator and gameplay planning; mobile targets are not yet defined. |
| Authority boundary | Backend owns AI, legality, XP, persistence, and generated files; frontend owns presentation and data binding | Prevents the browser from duplicating domain rules or mutating project state directly. |

## Open Questions

- What are the exact response schemas for Creator crunch operations?
- How does each finalized phase hand off data to the next phase?
- How is a completed Crunch sheet persisted and retrieved?
- Are generation operations synchronous or job-based?
- What are the retry and idempotency rules for finalization?
- How long do sessions live, and how are expiration and concurrent requests handled?
- How does Phase 4 receive and validate the finalized character roster?
- How are draft and finalized character states represented?
- What artifact links or stable resource IDs does the backend return?
- Which desktop/laptop resolutions must be treated as acceptance targets?
- What Figma plan, plugin, and export constraints apply?

## Change Protocol

When a decision changes:

1. Update the decision table.
2. Add the previous direction and the reason for changing it under a dated entry below.
3. Update `docs/Creator_Figma_and_Frontend_Workflow.md` only after the new direction is agreed.
4. Review affected API mappings, screens, and verification steps.

## Change History

_No changes recorded yet._
