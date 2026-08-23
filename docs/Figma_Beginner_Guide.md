# Figma Beginner Guide for Geminisys

**Status:** Working draft
**Applies to:** The Geminisys Creator UI and future Play-phase UI work
**Last reviewed:** 2026-08-23

> This guide teaches the Figma mechanics used by the Geminisys design workflow. It is separate from the project-specific Creation workflow, which defines what the Creator UI needs to do.

## 1. Before You Begin

Figma's dashboard, onboarding screens, and right-panel labels can change over time. Treat the names in this guide as landmarks rather than assuming every label will be identical.

For this project, Figma owns visual intent: layout, typography, color, component appearance, and visual interaction states. The frontend owns behavior, API calls, validation, accessibility implementation, responsive behavior, and performance.

The first catalogue is for the Creator UI, which covers the entire Creation phase. Do not add Play-phase screens until that work is intentionally started.

## 2. Create the File

1. Go to Figma.com and create or sign in to a free account.
2. If onboarding asks you to create a team, staying in the personal workspace is fine for this private draft. The exact onboarding choices may vary.
3. From the home dashboard, open **Drafts** or the equivalent personal-drafts area.
4. Create a new **Design file**.
5. Rename it `Geminisys_Creator_UI_Catalogue`.

Before depending on plugins, libraries, or automated exports, verify the current free-plan limits, sharing permissions, and export options. `VTT_Master_UI_Catalogue` can be used later if the Play phase joins this catalogue.

## 3. Understand the Workspace

Figma has three areas you will use constantly:

- **Left navigation and Layers panel:** pages and the hierarchy of elements on the current canvas.
- **Center canvas:** the workspace for frames, components, and screen layouts.
- **Right Properties panel:** dimensions, colors, typography, Auto Layout, component properties, and export settings.

If a control appears in a different location, search Figma's menus or use the right-panel search. Do not redesign the document because a label moved.

## 4. Create and Name the Catalogue Pages

Rename the initial page and add the remaining pages in this order:

- `00 Read Me`
- `01 Foundations`
- `02 Components`
- `03 Creator Screens`
- `04 States and Flows`
- `05 Handoff Exports`
- `99 Archive`

Use clear names for layers and components from the beginning. For example:

- `Button / Primary`
- `Button / Secondary`
- `Input / Chat composer`
- `Banner / Error`

Names become important when finding components and translating the design into HTML and CSS.

## 5. Establish Provisional Foundations

Before building screens, use `01 Foundations` to create a small, clearly labeled set of provisional styles or variables for:

- Shell background.
- Primary text and muted text.
- Accent and attention.
- Information, danger, and success states.
- Spacing values such as 4, 8, 12, 16, 24, and 32.
- Border radius and border color.
- Body and display typography.

The placeholder palette may use `#1E1E2E` for a dark shell and amber for attention. These are starting values, not permanent brand decisions. Prefer Figma Variables or Styles where available, and give them semantic names such as `color/background/shell` and `color/state/attention`. The eventual frontend should mirror those semantic roles with CSS custom properties.

## 6. Essential Shortcuts

Use these shortcuts while building standard interface elements:

- `F`: create a Frame.
- `T`: create Text.
- `R`: create a Rectangle.
- `Shift + A`: add Auto Layout to the current selection.
- `Ctrl + Alt + K` on Windows or `Cmd + Option + K` on Mac: create a Component.
- `Spacebar + click and drag`: pan around the canvas.

Shortcuts can be changed by the operating system, browser, or Figma settings. If one does not work, use the corresponding toolbar or menu command and continue.

## 7. Create the First Main Component

Use the `02 Components` page for this exercise:

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

## 8. Add Component States

Do not make a separate unrelated button for every state. Create variants or component properties for the states the Creator needs:

- Default.
- Hover.
- Focused.
- Disabled.
- Loading.
- Error or blocked, where appropriate.

Name variants with properties such as `State=Default` and `State=Disabled`. Use text and icon changes as well as color so state is not communicated by color alone. Keep loading and disabled states visibly distinct and make sure the label still fits.

## 9. Place a Linked Instance on Screen Frames

1. Open `03 Creator Screens`.
2. Create at least two desktop frames: `1440 x 900` for a laptop and `1920 x 1080` for a larger display. Add more target sizes only when the project decides they are required.
3. Insert an instance of `Button / Primary` from the Assets panel or the component's instance action. This makes the main-component relationship explicit. Copy and paste within the same file can also work, but the Assets workflow is easier to verify.
4. Place the instance in the appropriate Creator screen.
5. Return to the main component and change its temporary background fill or padding.
6. Confirm that the linked instance updates. If it does not, check that you inserted an instance rather than a detached copy and that the instance has no conflicting override.

Do not detach an instance merely to make a one-off visual change. Prefer a variant, component property, or intentional instance override so the relationship remains useful.

## 10. Make a Small Prototype and Checkpoint

Connect the button to a second frame in Prototype mode and use Present to click through it. This is only a visual flow check; it does not replace frontend routing or API behavior.

Before creating the full component library, confirm:

- The main component is named and easy to find.
- An instance updates when the main component changes.
- A longer label does not overflow the button.
- Disabled and loading states are distinguishable without relying on color.
- The button is usable at both laptop and large-display frame sizes.
- The design uses provisional token names rather than scattered hard-coded decisions.

## 11. Auto Layout Rules of Thumb

Use Auto Layout for ordinary interface structures such as buttons, form rows, chat messages, lists, and stacked panels. Use nested Auto Layout frames when a component has more than one direction of layout.

Learn these sizing choices:

- **Hug contents:** the frame grows around its contents; useful for buttons and tags.
- **Fill container:** a child expands to use available space; useful for inputs and full-width controls.
- **Fixed:** the dimension stays fixed; use deliberately for stable control heights or icon buttons.
- **Minimum and maximum dimensions:** prevent content from becoming unusably small or excessively wide.

Do not force Auto Layout onto future maps, canvas overlays, fog of war, or other spatial controls. Those surfaces need different layout and rendering techniques.

## 12. Handoff Basics

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
