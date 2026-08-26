# Figma Guide for Geminisys

**Status:** Working draft
**Applies to:** The Geminisys Creator UI and future Play-phase UI work
**Last reviewed:** 2026-08-23

> This guide teaches the Figma mechanics used by the Geminisys design workflow. It is separate from the project-specific Creation workflow, which defines what the Creator UI needs to do.

## 1. Before You Begin

Figma's dashboard, onboarding screens, and right-panel labels can change over time. Treat the names in this guide as landmarks rather than assuming every label will be identical.

For this project, Figma owns visual intent: layout, typography, color, component appearance, and visual interaction states. The frontend owns behavior, API calls, validation, accessibility implementation, responsive behavior, and performance.

The master catalogue covers the full Geminisys UI. While the project is limited to three free Figma pages, keep the phases organized as pages within one file and use sections to divide the work.

## 2. Vocabulary and Concepts

The detailed beginner glossary is maintained separately in [Luckiis_Beginner_Glossary.md](Luckiis_Beginner_Glossary.md). It defines the Figma, frontend, API, layout, accessibility, and handoff terms used in this guide. Return to it whenever a term is unfamiliar.

## 3. Create the File

1. Go to Figma.com and create or sign in to a free account.
2. If onboarding asks you to create a team, staying in the personal workspace is fine for this private draft. The exact onboarding choices may vary.
3. From the home dashboard, open **Drafts** or the equivalent personal-drafts area.
4. Create a new **Design file**.
5. Rename it `Geminisys_UI_Catalogue`.

Before depending on plugins, libraries, or automated exports, verify the current free-plan limits, sharing permissions, and export options. Keep the file within the available three-page limit for now.

## 4. Understand the Workspace

Figma has three areas you will use constantly:

- **Left navigation and Layers panel:** pages and the hierarchy of elements on the current canvas.
- **Center canvas:** the workspace for frames, components, and screen layouts.
- **Right Properties panel:** dimensions, colors, typography, Auto Layout, component properties, and export settings.

If a control appears in a different location, search Figma's menus or use the right-panel search. Do not redesign the document because a label moved.

## 5. Create and Name the Catalogue Pages

Rename the initial page and add the remaining pages in this order:

- `01 Creator Phase`
- `02 Play Phase`
- `03 Reserve`

Use sections inside the pages to keep the catalogue organized:

- `01 Creator Phase`: `FOUNDATIONS`, `COMPONENTS`, `SANDBOX PITCH`, `CHARACTER CONCEPTS`, `CHARACTER CRUNCH`, `CAMPAIGN IGNITION`, `STATES AND FLOWS`, and `HANDOFF`.
- `02 Play Phase`: leave empty until Play-phase design begins; then add gameplay screens, maps, encounters, character actions, and Play-phase states as sections.
- `03 Reserve`: keep available for a future phase, experiments, archive material, or temporary overflow.

Add a small index at the top of each page and leave visible spacing between sections. When more pages become available, sections can be promoted into dedicated pages without redesigning their contents.

Use clear names for layers and components from the beginning. For example:

- `Button / Primary`
- `Button / Secondary`
- `Input / Chat composer`
- `Banner / Error`

Names become important when finding components and translating the design into HTML and CSS.

## 6. Establish Provisional Foundations

Before building screens, use the `FOUNDATIONS` section on the `01 Creator Phase` page to create a small, clearly labeled set of provisional styles or variables for:

- Shell background.
- Primary text and muted text.
- Accent and attention.
- Information, danger, and success states.
- Spacing values such as 4, 8, 12, 16, 24, and 32.
- Border radius and border color.
- Body and display typography.

The placeholder palette may use `#1E1E2E` for a dark shell and amber for attention. These are starting values, not permanent brand decisions. Prefer Figma Variables or Styles where available, and give them semantic names such as `color/background/shell` and `color/state/attention`. The eventual frontend should mirror those semantic roles with CSS custom properties.

## 7. Essential Shortcuts

Use these shortcuts while building standard interface elements:

- `F`: create a Frame.
- `T`: create Text.
- `R`: create a Rectangle.
- `Shift + A`: add Auto Layout to the current selection.
- `Ctrl + Alt + K` on Windows or `Cmd + Option + K` on Mac: create a Component.
- `Spacebar + click and drag`: pan around the canvas.

Shortcuts can be changed by the operating system, browser, or Figma settings. If one does not work, use the corresponding toolbar or menu command and continue.

## 8. Create the First Main Component

Use the `COMPONENTS` section on the `01 Creator Phase` page for this exercise:

1. Press `T`, click the canvas, and type `CONTINUE TO CRUNCH`.
2. Use a readable placeholder font at approximately 14px. Inter or Roboto is acceptable for the exercise; choose and document the final type family during the Foundations pass.
3. Select the text layer and press `Shift + A`. This creates an Auto Layout frame around the text. Make sure the frame, not only the text, is selected for the next steps.
4. Add the temporary dark shell fill `#1E1E2E`.
5. Set horizontal padding to 16px and vertical padding to 8px.
6. Set the frame's width to **Hug contents** so the button grows when its label changes.
7. Set the corner radius to 6px or less.
8. Select the Auto Layout frame and choose **Create component**, or press `Ctrl + Alt + K` on Windows.
9. Rename the resulting main component `Button / Primary`.

Figma's current term is **main component**. An **instance** is a linked copy used in a screen. Keep the label generic enough to support actions such as **Save Draft**, **Retry**, and **Finalize Campaign**.

## 9. Add Component States

Do not make a separate unrelated button for every state. Create variants or component properties for the states the Creator needs:

- Default.
- Hover.
- Focused.
- Disabled.
- Loading.
- Error or blocked, where appropriate.

Name variants with properties such as `State=Default` and `State=Disabled`. Use text and icon changes as well as color so state is not communicated by color alone. Keep loading and disabled states visibly distinct and make sure the label still fits.

## 10. Place a Linked Instance on Screen Frames

1. Open the `01 Creator Phase` page and go to the appropriate screen section.
2. Create at least two desktop frames: `1440 x 900` for a laptop and `1920 x 1080` for a larger display. Add more target sizes only when the project decides they are required.
3. Insert an instance of `Button / Primary` from the Assets panel or the component's instance action. This makes the main-component relationship explicit. Copy and paste within the same file can also work, but the Assets workflow is easier to verify.
4. Place the instance in the appropriate Creator screen.
5. Return to the main component and change its temporary background fill or padding.
6. Confirm that the linked instance updates. If it does not, check that you inserted an instance rather than a detached copy and that the instance has no conflicting override.

Do not detach an instance merely to make a one-off visual change. Prefer a variant, component property, or intentional instance override so the relationship remains useful.

## 11. Make a Small Prototype and Checkpoint

Connect the button to a second frame in Prototype mode and use Present to click through it. This is only a visual flow check; it does not replace frontend routing or API behavior.

Before creating the full component library, confirm:

- The main component is named and easy to find.
- An instance updates when the main component changes.
- A longer label does not overflow the button.
- Disabled and loading states are distinguishable without relying on color.
- The button is usable at both laptop and large-display frame sizes.
- The design uses provisional token names rather than scattered hard-coded decisions.

## 12. Auto Layout Rules of Thumb

Use Auto Layout for ordinary interface structures such as buttons, form rows, chat messages, lists, and stacked panels. Use nested Auto Layout frames when a component has more than one direction of layout.

Learn these sizing choices:

- **Hug contents:** the frame grows around its contents; useful for buttons and tags.
- **Fill container:** a child expands to use available space; useful for inputs and full-width controls.
- **Fixed:** the dimension stays fixed; use deliberately for stable control heights or icon buttons.
- **Minimum and maximum dimensions:** prevent content from becoming unusably small or excessively wide.

Do not force Auto Layout onto future maps, canvas overlays, fog of war, or other spatial controls. Those surfaces need different layout and rendering techniques.

## 13. Backup and Restore

### What the backup is for

The Figma backup is for recovering design work and preserving important milestones. It is not a runtime data source for Geminisys.

Use these sources in this order:

1. **Figma cloud file:** the active working design source.
2. **Figma Version History:** recovery of earlier saved versions within Figma.
3. **Local `.fig` snapshots:** offline or disaster-recovery copies.
4. **Exported assets:** only the images, icons, or other files the frontend actually needs.

Do not treat screenshots, exported assets, or a local `.fig` file as a replacement for the live Figma file. They do not preserve all of the same editing relationships, component links, variables, or prototype connections.

### Recommended backup location

Keep local snapshots outside the application runtime folders. A practical repository-adjacent location is:

```text
geminisys-design-backups/
	figma/
		Geminisys_UI_Catalogue_YYYY-MM-DD_short-description.fig
		README.md
```

Replace `YYYY-MM-DD_short-description` with the actual snapshot date and a brief description when you create this backup location.

Do not place backups in `campaigns/`, `backend/`, or any folder the server scans for campaign state or generated files. If a backup is stored inside the repository, confirm that it is intentionally tracked and understand that `.fig` files may be large binary files. Never commit credentials, tokens, private links, or exported user data with a design backup.

### Manual backup routine

Make a snapshot at these points:

- After the catalogue pages and foundations are established.
- After a major component-library milestone.
- Before a substantial visual redesign.
- Before sharing a handoff for frontend implementation.
- At the end of a productive design session when the work would be painful to recreate.

For each snapshot:

1. Confirm the Figma cloud file has finished saving.
2. Add a named version in Figma Version History, such as `Creation shell and token pass`.
3. Use Figma's file menu to save or download a local copy, such as **Save local copy** or the current equivalent.
4. Store the `.fig` file using this filename pattern:

	 ```text
	 Geminisys_UI_Catalogue_YYYY-MM-DD_short-description.fig
	 ```

5. Record the snapshot date, Figma file URL or identifier, major changes, and any known limitations in the backup README or the project decision log.
6. Open the local file once, if practical, to confirm that it is readable and is the intended snapshot.

Figma's menu wording and local-copy availability can vary by plan and product version. If a local `.fig` export is unavailable, rely on Figma Version History and duplicate the file in Figma as a named milestone. Do not substitute a screenshot unless you only need a visual reference.

### Restore procedure

If the live file is damaged or important work is lost:

1. Check Figma Version History first and restore or duplicate the correct named version.
2. If necessary, open the newest suitable local `.fig` snapshot in Figma.
3. Rename the restored file with a clear `restored-YYYY-MM-DD` suffix until it has been reviewed.
4. Check the catalogue pages, Variables or Styles, main components, variants, instances, prototype links, and handoff notes.
5. Make the restored file the active working file only after the review is complete.
6. Create a new backup snapshot after restoration.

### Backend and frontend boundary

The backend should **not pull from the Figma backup folder**. Figma files describe visual intent; they are not campaign state, character data, API configuration, or production runtime input. The backend should consume its own documented API inputs and project data files, not scan `.fig` files or exported design folders.

The frontend should implement the approved design using HTML, CSS, and JavaScript. Exported assets may be copied into a deliberate frontend asset location when needed, but that is a controlled handoff step, not an automatic backup-folder dependency.

If the project later wants automated design-token or asset synchronization, define a separate, explicit import pipeline with a chosen source file, schema, validation, generated-output folder, and review step. That pipeline should read an approved export or Figma API response, never an arbitrary backup folder, and it should never allow design files to overwrite campaign or character state.

## 14. Handoff Basics

For each approved screen or component, record:

- Frame name and target size.
- Component and variant names.
- Typography, color, spacing, and border tokens.
- Interactive states.
- Accessibility intent, including focus and error presentation.
- Responsive behavior that the frontend must implement.
- Any API or state dependency, linked from the Creation workflow document.

Export only assets that the frontend actually needs. Use clear filenames and confirm the required format before exporting. Do not export screenshots as a substitute for a real HTML/CSS implementation.

The Figma catalogue is a source of visual truth, not a replacement for the frontend implementation or backend contract.
