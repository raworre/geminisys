# Luckii's Beginner Glossary

**Status:** Working draft
**Applies to:** The Geminisys Creator UI and future Play-phase UI work
**Last reviewed:** 2026-08-23

> This glossary explains the Figma, frontend, API, layout, accessibility, and handoff terms used in the Geminisys design documents. You do not need to memorize everything; return here whenever a word is unfamiliar.

## Index

Use this as a quick reference. The glossary is arranged in learning order, with the most frequently encountered groups first.

- [Software and Interface Terms](#software-and-interface-terms): UI, frontend, backend, API, and source of truth.
- [Figma File Structure](#figma-file-structure): catalogue pages, frames, and layers.
- [Reusable Components](#reusable-components): component libraries, main components, instances, variants, Assets, overrides, and detached copies.
- [Visual System and Layout](#visual-system-and-layout): foundations, Variables, Styles, Auto Layout, and responsive behavior.
- [Review and Handoff Terms](#review-and-handoff-terms): accessibility, exports, prototypes, handoff, and handoff notes.

For a specific word, use your browser's page search (`Ctrl + F` on Windows) and search for the term.

## Software and Interface Terms

The groups in this glossary are ordered from the terms you are likely to encounter most often to the terms you will use later during review and handoff.

### UI

**UI** means **user interface**: the visible controls and information a person uses, such as buttons, text fields, menus, labels, and panels. The Creator UI is the part of Geminisys the user sees and interacts with.

### Frontend and backend

The **frontend** is the part of an application that runs in the user's browser or device. It displays screens, accepts input, and responds to interaction. The **backend** is the server-side part that stores data, applies domain rules, talks to AI services, and generates files. Figma designs the appearance of the frontend; it does not replace either part.

### API

An **API**, or application programming interface, is an agreed way for software parts to communicate. In Geminisys, the frontend will use API requests to ask the backend to chat, save drafts, perform Crunch actions, and generate campaign files.

### Source of truth

A **source of truth** is the place that owns a particular kind of information. In this workflow, Figma is the visual source of truth, the frontend is the behavior and presentation-state source of truth, and the backend is the domain-data source of truth. If two sources disagree, the owner of that kind of information should decide which one is correct.

## Figma File Structure

### Catalogue pages

**Catalogue pages** are the named sections in the left sidebar of one Figma file. They organize the work but do not automatically affect the finished application. While the project is limited to three free pages, the Geminisys master catalogue uses `01 Creator Phase`, `02 Play Phase`, and `03 Reserve`. Use Figma sections within those pages for foundations, components, Creator screens, states and flows, handoff exports, and archived explorations.

### Frame

A **frame** is a Figma container that holds other layers. A frame can represent a screen, a panel, a form, or a component. It can have its own size, background, layout, and prototype connections. A screen frame is a design representation of a possible application viewport, not the actual browser window.

### Layer

A **layer** is one item in a Figma design's hierarchy, such as text, a rectangle, an icon, a frame, a component, or an instance. The Layers panel shows how items are nested inside one another. Layer order can affect what appears in front of or behind other items.

## Reusable Components

### Component library

A **component library** is the collection of reusable UI building blocks, such as buttons, inputs, banners, chat messages, and phase indicators. In this project, the library is kept in the `COMPONENTS` section of the `01 Creator Phase` page. A **component-library milestone** is a meaningful checkpoint, such as finishing the first button, completing the form controls, or completing the shared Creator shell. Make a backup and review the library at these checkpoints.

### Main components

A **main component** is the source definition of a reusable design element. It controls the structure and default appearance. Figma used to be described in some tutorials as having a "master component"; **main component** is the current term to use.

### Instances

An **instance** is a linked copy of a main component placed in a screen. It receives changes made to the main component while allowing limited, intentional overrides such as changing its text label. Do not detach an instance just to make a one-off change; use a variant, component property, or documented override when possible.

### Variants

**Variants** are related versions of one component grouped together. A button might have `State=Default`, `State=Hover`, `State=Focused`, `State=Disabled`, and `State=Loading` variants. Variants keep related states together so they are easier to find and maintain.

### Assets panel

The **Assets panel** is the part of Figma's interface where reusable components and libraries can be found and inserted. Insert a component from Assets when you want a linked instance. This is different from drawing a new copy from scratch.

### Override

An **override** is an intentional change made to an instance without changing its main component. Changing a button instance's label from `CONTINUE` to `SAVE DRAFT` is a simple example. Keep overrides limited and deliberate so important changes can still be made in the main component.

### Detached copy

A **detached copy** is an instance that has been disconnected from its main component. It can be edited freely, but it no longer receives updates from the main component. Detach only when the element genuinely needs to become an independent design; do not use detaching as the normal way to customize a screen.

## Visual System and Layout

### Foundations

**Foundations** are the basic visual rules that the rest of the design reuses. They include colors, typography, spacing, borders, corner radii, focus states, and motion rules. Foundations are sometimes called a **design system foundation** or **design tokens**.

### Variables and styles

**Variables** are reusable values that can change or have different modes, such as a color, spacing value, or number. **Styles** are reusable formatting definitions, commonly for text, fills, strokes, and effects. Both help keep a design consistent. Use semantic names such as `color/background/shell` instead of names based only on a temporary color, such as `dark-purple`.

For this project, Variables or Styles are the Figma-side equivalents of CSS custom properties. They are related concepts, not an automatic export: the frontend still needs deliberate CSS values and behavior.

### Auto Layout

**Auto Layout** is Figma's system for arranging items so they respond to content and spacing changes. It is similar in purpose to layout rules in CSS. It is useful for buttons, form rows, chat messages, lists, and stacked panels because items can be added, removed, or resized without manually repositioning everything.

### Responsive behavior

**Responsive behavior** describes how a layout adapts when the available space or content changes. Examples include a panel becoming wider, a button growing to fit a longer label, or a two-column layout becoming one column. Figma can demonstrate some of this through frames and Auto Layout, but the frontend must implement the actual browser behavior.

## Review and Handoff Terms

### Accessibility

**Accessibility** means designing and implementing the interface so people with different abilities can use it. In this project that includes readable contrast, visible keyboard focus, labels for controls, clear errors, sensible text sizing, and alternatives to information conveyed only by color or motion.

### Export

An **export** is a file produced from Figma, such as a PNG, SVG, or other asset format. Exported assets are copies for a specific implementation need. They are not the full editable design file and should not be confused with a backup.

### Prototype mode and Present

**Prototype mode** is Figma's tool for connecting frames into a clickable demonstration. **Present** opens that demonstration so someone can try it. A Figma prototype can show the intended path through a screen, but it does not perform real authentication, API calls, validation, persistence, or backend processing.

### Prototype links

**Prototype links** connect frames in Figma's Prototype mode so you can click through a visual flow using Present. They demonstrate navigation or interaction for review, but they are not application routing, API calls, validation, or backend behavior. The frontend must implement those separately.

### Handoff

**Handoff** is the process of giving an approved design to the person implementing it. A Figma handoff should explain what the screen looks like, what states exist, what changes when content grows, and what behavior belongs in code. It is more than sending a screenshot or a Figma link.

### Handoff notes

**Handoff notes** are the implementation details attached to an approved frame or component. They should record the target frame size, component and variant names, token names, interactive states, accessibility intent, responsive behavior, and any API or state dependency. For Creator screens, link the relevant decision or workflow information rather than hiding it in a comment that only exists in Figma.
