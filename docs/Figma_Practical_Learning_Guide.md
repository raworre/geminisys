# Figma Practical Learning Guide

**Status:** Working draft
**Applies to:** Learning the Figma skills needed for the Geminisys UI catalogue
**Companion document:** [Figma_Guide.md](Figma_Guide.md)

> This is a hands-on workbook, not a test. Move slowly, repeat steps, and stop at any checkpoint. The goal is to build a reliable mental picture of Figma one small object at a time.

## Guide Map

- [Part I: Tools and Index](#part-i-tools-and-index): sections 1-4 explain the overall map and the basic Figma objects.
- [Part II: Practice Workbook](#part-ii-practice-workbook): section 5 onward teaches the skills through small exercises.

You can read Part I first, then jump directly to the practice section when you are ready to make something.

## Part I: Tools and Index

## 1. How to Use This Guide

The project overview explains what the Geminisys catalogue should contain. This guide explains how to operate Figma well enough to build it.

Each lesson has four parts:

- **Goal:** the one thing you are practicing.
- **Anchor:** a familiar idea that gives the new term somewhere to attach.
- **Steps:** short actions to perform in Figma.
- **Checkpoint:** what success should look like before continuing.

You do not need to memorize Figma vocabulary first. Use a term when an action needs it, then return to the explanation later.

### A comfortable learning rhythm

1. Read only one lesson.
2. Perform the steps in a blank area of your file.
3. Compare what you see with the checkpoint.
4. Pause, take a screenshot, or write one sentence about what happened.
5. Continue only when the current object makes sense.

Figma can look like a crowded workbench. That does not mean you are doing anything wrong. Zoom in, hide panels if needed, and work on one object at a time.

## 2. The Big Picture

Think of Figma as one restaurant while it is being planned and prepared. The file is the whole restaurant, pages are departments, sections are labeled stations, frames are trays or service areas, and the objects inside them are the items being prepared. Reusable components are house recipes, variables are labeled ingredient bins, and prototypes are a customer-service walkthrough.

Figma creates the visual plan. It does not become the finished website or application by itself. The frontend later implements behavior, accessibility, API calls, and responsive rules.

### The restaurant map

```text
Geminisys_UI_Catalogue = THE WHOLE RESTAURANT
|
+-- 01 Creator Phase = one department
|   |
|   +-- SECTION: FOUNDATIONS = ingredients and house standards
|   +-- SECTION: COMPONENTS  = repeatable recipes
|   +-- SECTION: SANDBOX PITCH = one service area
|   +-- SECTION: STATES       = preparing, ready, blocked, or unavailable
|   +-- SECTION: HANDOFF      = notes for the team serving the finished dish
|
+-- 02 Play Phase = another department, used later
|
+-- 03 Reserve = clean space for future work
```

When you feel lost, locate the object on this map first: whole restaurant, department, station, tray, or item.

### What is Sandbox Pitch?

`Sandbox Pitch` is the first Creation-stage service area in Geminisys. It is where a person and the AI explore a campaign idea through conversation before the campaign is finalized.

```text
IDEA                          CAMPAIGN PROPOSAL              FINAL CAMPAIGN
"I want a heist story"  -->   chat, questions, and choices  -->  confirmed setting
							  happen here
```

The name has two parts:

- **Sandbox:** a contained place where ideas can be tried, adjusted, or discarded without pretending they are final.
- **Pitch:** the developing proposal for what the campaign could be, including its premise, tone, and important choices.

### Restaurant anchor

Imagine a guest speaking with the chef before placing a large custom order. They describe the kind of meal they want, the chef asks clarifying questions, and both sides adjust the plan. The order is not ready yet; it is being shaped.

That conversation is the Sandbox Pitch. In the UI, it may include an empty campaign chat, an active conversation, a completion suggestion, a campaign slug, a finalization confirmation, and campaign-generation progress.

The Sandbox Pitch is not the Play phase. It is also not the final campaign file. It is the Creation stage that helps turn a loose idea into a confirmed campaign proposal.

## 3. Your First Orientation

### What you are looking at

```text
+----------------------+-----------------------------+----------------------+
| LEFT                 | CENTER                      | RIGHT                |
| Pages and Layers     | Canvas                      | Properties           |
| "What exists?"       | "What am I making?"         | "How is it set up?"  |
+----------------------+-----------------------------+----------------------+
```

- **Pages** are major work areas in one Figma file.
- **Layers** are the individual objects in the current page.
- The **canvas** is the open work surface where objects are placed.
- The **Properties panel** changes the selected object's size, position, color, text, and other settings.

### Anchor: one restaurant

A file is the whole restaurant. A page is a department. A section is a clearly marked station inside that department. A frame is a tray, counter, or service area. Layers are the individual ingredients, labels, or prepared items on that surface.

This is one consistent visual map, not a claim that every Figma object behaves exactly like a physical restaurant object.

### One order, from building to item

```text
RESTAURANT       DEPARTMENT       STATION          TRAY             ITEM
File             Page              Section          Frame            Layer
Geminisys        Creator Phase     Components      Button frame     Text
```

The words to the right are smaller parts inside the words to the left. A button's text is an item on its tray; the tray is inside a station; the station is on a department page.

## 4. The Smallest Useful Vocabulary

### File

A **file** is the complete Figma document. For Geminisys, the file is `Geminisys_UI_Catalogue`.

**Anchor:** the restaurant building and its complete recipe binder.

### Page

A **page** is a large workspace inside the file. Geminisys currently uses:

- `01 Creator Phase`
- `02 Play Phase`
- `03 Reserve`

**Anchor:** a restaurant department, such as the prep kitchen, dining room, or service counter.

### Section

A **section** groups related work on a page. For example, the `01 Creator Phase` page can contain `FOUNDATIONS`, `COMPONENTS`, and `SANDBOX PITCH` sections.

**Anchor:** a labeled station, such as the sauce station or dessert station.

### Layer

A **layer** is one object in the layer list: text, a shape, an image, a frame, or a component.

**Anchor:** one ingredient, label, plate, or prepared item.

### Frame

A **frame** is a container with boundaries. It can represent a screen, a panel, a button, or a smaller layout area.

**Anchor:** a tray, serving plate, or counter area. Objects can be placed inside it.

### Component

A **component** is a reusable object with a source definition. A button component lets you make consistent button copies without rebuilding each one from scratch.

**Anchor:** the restaurant's standard recipe for a dish.

### Instance

An **instance** is a linked copy of a component. It can usually have local changes, such as a different button label, while still receiving structural updates from the component.

**Anchor:** one prepared serving made from the standard recipe.

### Variant

A **variant** is a related version of a component, such as a button's default, focused, disabled, or loading state.

**Anchor:** one dish's different service states, such as preparing, ready, unavailable, or sold out.

## Part II: Practice Workbook

## 5. First Practice: Make a Shape

### Goal

Select, move, resize, and recolor one rectangle.

### Anchor

This is like placing one ingredient or plate on a clean prep counter. Nothing else needs to be understood yet.

### Steps

1. Create a blank area on a page.
2. Press `R` for Rectangle.
3. Click and drag on the canvas to draw a rectangle.
4. Click the rectangle to select it.
5. Drag it to a new position.
6. Drag a corner to resize it.
7. Use the fill control in the right panel to choose a different color.
8. Press `Ctrl+Z` if an action goes somewhere unexpected.

### Checkpoint

You can identify which object is selected, move it, resize it, and change its fill color.

## 6. Second Practice: Make a Label

### Goal

Create text and place it near a shape.

### Anchor

This is like writing a menu label or station sign. The text is an object, just as the rectangle is an object.

### Steps

1. Press `T` for Text.
2. Click on the canvas.
3. Type `CONTINUE TO CRUNCH`.
4. Select the text object.
5. Use the right panel to change its font size.
6. Drag the text near the rectangle.
7. Select the text and rectangle together by holding `Shift` while clicking both.

### Checkpoint

The Layers panel shows separate objects for the rectangle and the text. Selecting one does not automatically select the other.

## 7. Containers: Put Objects on a Tray

### Goal

Understand that a frame can contain other layers.

### Anchor

A tray holds several items while they move together. A frame can hold text and shapes in a similar organizational way.

### Steps

1. Press `F` for Frame.
2. Draw a frame larger than your text and rectangle.
3. Move the rectangle and text into the frame area.
4. In the Layers panel, inspect which objects are nested under the frame.
5. Select the frame and move it.

### Checkpoint

You can see the difference between moving the frame and moving one object inside the frame.

```text
FRAME / TRAY
+--------------------------------+
|  TEXT / LABEL                  |
|  RECTANGLE / PLATE             |
+--------------------------------+

Move the tray: both items travel together.
Move one item: the other item stays where it is.
```

### If it looks wrong

- If the object goes behind something, check the layer order in the Layers panel.
- If the object is not inside the frame, drag its layer underneath the frame in the Layers panel.
- If you select the wrong thing, click an empty part of the canvas and try again.

## 8. A Practical Translation Table

| Figma idea | Familiar anchor | Geminisys example |
| --- | --- | --- |
| File | Whole building or binder | `Geminisys_UI_Catalogue` |
| Page | Restaurant department | `01 Creator Phase` |
| Section | Labeled kitchen station | `COMPONENTS` |
| Frame | Tray or work surface | A screen or button boundary |
| Layer | One item on the tray | Text, icon, or shape |
| Component | Standard recipe or mold | Primary button definition |
| Instance | Prepared copy from the recipe | Button used on a screen |
| Variant | Different operating state | Disabled button |
| Variable | Labeled ingredient bin | Shell background color |
| Style | Saved appearance recipe | Body text formatting |

### The same map, zoomed in

```text
01 Creator Phase
    |
    +-- COMPONENTS station
	    |
	    +-- Button / Primary recipe
		    |
		    +-- Default serving
		    +-- Disabled serving
		    +-- Loading serving
```

This is why organization matters: you should be able to follow the path from the department to the station to the recipe to the state.

## 9. Variables: Labeled Bins for Reusable Values

### The plain-language idea

A **variable** is a named place to store a value that you expect to reuse. The value might be a color, spacing amount, number, or text value, depending on the variable type Figma supports.

### Anchor: labeled ingredient bins

Imagine preparing the same sauce for ten dishes. If one labeled ingredient bin stores the approved sauce recipe or quantity, changing that source gives you one place to update later.

A Figma variable works similarly:

```text
color/background/shell = #1E1E2E
```

Several objects can use that variable. If the shell color changes, you can update the variable instead of hunting through every object.

```text
INGREDIENT BIN
color/background/shell = #1E1E2E
		  |
		  +--> screen tray
		  +--> button tray
		  +--> chat panel tray
```

### Why the name is semantic

A semantic name describes the job of a value, not only its current appearance.

```text
Useful:  color/background/shell
Useful:  color/state/attention
Less useful: dark-blue
Less useful: yellow-orange
```

The color may change during design. The job usually remains recognizable.

### Tiny practice

1. Find the Variables area in Figma's current interface.
2. Create a color variable named `color/background/shell`.
3. Give it a temporary color.
4. Apply it to a frame's fill if Figma offers that control in your current plan.
5. Change the variable's color.
6. Check whether the frame updates.

### Checkpoint

You understand the relationship: the variable is the labeled source value, and the frame is one user of that value.

### If variables are unavailable

Do not stop your project. Write the intended token name beside the design and use a temporary color style or fill. The important first step is learning which values should be shared.

## 10. Styles: Saved Appearance Recipes

A **style** is a saved appearance recipe. It can describe a color or text formatting, depending on what Figma supports in the current interface.

### Anchor: the restaurant recipe card

A variable is like one labeled ingredient bin. A style is the complete recipe card saying how the finished item should look, such as its font, size, weight, line spacing, and color.

Use a style when you want a whole appearance recipe to stay consistent. Use a variable when you mainly want one reusable value.

```text
VARIABLE                         STYLE
One labeled ingredient            Complete recipe card
"shell color"                     "body text appearance"
	|                                  |
	+--> reused by many items         +--> reused by many labels
```

### Semantic naming

```text
Text style: typography/body
Color style: color/state/danger
Spacing variable: spacing/16
```

These names tell you where the value belongs and what job it performs.

## 11. Auto Layout: A Self-Arranging Tray

### The plain-language idea

**Auto Layout** makes a frame arrange its children according to rules. It is useful when text length or the number of items may change.

### Anchor: a tray with adjustable dividers

A normal serving tray does not automatically make room when you add a larger plate. An adjustable tray can expand, keep spacing even, and maintain padding. Auto Layout is the adjustable tray.

### Button exercise

1. Create the text `CONTINUE TO CRUNCH`.
2. Select the text.
3. Press `Shift+A` to add Auto Layout around it.
4. Set horizontal padding to 16px and vertical padding to 8px.
5. Give the frame a temporary fill color.
6. Change the frame width setting to **Hug contents**.
7. Replace the text with `SAVE DRAFT`.
8. Replace it again with `FINALIZE CAMPAIGN`.

### Checkpoint

The button grows around its label instead of cutting off the longer text. Padding remains visible around the text.

```text
SHORT ORDER                    LONG ORDER
+------------------+           +--------------------------+
|   SAVE DRAFT     |           |   FINALIZE CAMPAIGN      |
+------------------+           +--------------------------+
	same padding around the words
```

### Common sizing words

- **Hug contents:** grow around the items inside. Like a tray sized to its contents.
- **Fill container:** expand to use available room. Like a shelf item filling the open shelf width.
- **Fixed:** stay at a deliberate size. Like a standard button height or icon tile.

## 12. Components and States

### Goal

Turn the button into a reusable component and describe its states.

### Anchor: the house recipe

If a restaurant prepares the same dish many times, it keeps a house recipe. If the recipe changes, future servings follow the new recipe. A component serves a similar purpose for interface objects.

### Steps

1. Select the Auto Layout button frame.
2. Choose **Create component**, or press `Ctrl+Alt+K` on Windows.
3. Rename it `Button / Primary`.
4. Create or define related states: Default, Hover, Focused, Disabled, and Loading.
5. Keep text or icon changes in addition to color changes where appropriate.
6. Insert a linked instance from the Assets panel into a screen section.

### Checkpoint

You can point to the reusable source component and the linked copy placed in a screen.

### Important distinction

A component is the reusable definition. An instance is the copy used in a screen. A detached copy no longer receives updates from the component, so detaching should be unusual and intentional.

```text
HOUSE RECIPE                    SERVINGS
Button / Primary  ----------->  screen button 1
	   |                         screen button 2
	   +-- update recipe         screen button 3
		   updates linked servings
```

## 13. Screens and Prototypes

### Frame as screen

A screen frame is a bounded drawing of a possible application viewport. Create desktop practice frames at `1440 x 900` and `1920 x 1080` when following the Geminisys guide.

### Prototype as demonstration

Prototype connections show how someone could move from one frame to another. They are like a customer-service walkthrough from ordering to receiving a dish.

A prototype connection does not implement frontend routing, API calls, validation, or persistence. It demonstrates the intended visual path.

```text
[ORDER SCREEN] --click button--> [CONFIRMATION SCREEN]
	   |                                  |
   customer starts                    customer sees result
```

### Tiny practice

1. Make two screen frames.
2. Put a button instance in the first frame.
3. Open Prototype mode.
4. Connect the button to the second frame.
5. Use Present to click through the connection.

### Checkpoint

You can explain the difference between showing a path in Figma and building the real behavior in the frontend.

## 14. Troubleshooting by Symptom

### “I cannot select the thing I want.”

Look in the Layers panel and select the named layer there. You may be clicking a child object when you need its frame, or an overlapping object may be in front.

### “The text disappeared.”

Check the text color, layer order, and whether the text is inside a frame with clipping enabled. Use the Layers panel to select it directly.

### “The button is too small.”

Check whether its frame is set to **Hug contents**, whether the text is clipped, and whether padding is large enough.

### “The object moved unexpectedly.”

Undo once with `Ctrl+Z`, then inspect which layer is selected. You may have moved a frame, a child layer, or several selected objects together.

### “The copied object does not update.”

Check whether it is an instance linked to the component. If it is a detached copy, it will not receive component changes.

### “Everything feels visually overwhelming.”

Zoom in, close or collapse panels, work inside one named section, and select only one object at a time. Use the Layers panel as your map instead of scanning the entire canvas.

### “I do not know what to do next.”

Return to the last checkpoint. If the result is not visible, undo the last action and repeat only that action. Do not restart the whole file.

## 15. Learning Checkpoints

Pause after each milestone:

- [ ] I can identify a page, section, frame, and layer.
- [ ] I can make and edit a rectangle and a text label.
- [ ] I can find a selected object's properties in the right panel.
- [ ] I can place objects inside a frame.
- [ ] I understand a variable as a reusable named value.
- [ ] I understand a style as a saved appearance recipe.
- [ ] I can make a button that grows around its label.
- [ ] I understand the difference between a component and an instance.
- [ ] I can describe default, focused, disabled, and loading states.
- [ ] I can make a simple prototype connection.
- [ ] I can tell which decisions belong to Figma and which belong to the frontend.

## 16. A First Geminisys Practice Session

When you are ready to connect the skills to the real catalogue, use this order:

1. Open `Geminisys_UI_Catalogue`.
2. Open the `01 Creator Phase` page.
3. Create or find the `COMPONENTS` section.
4. Make one primary button.
5. Make one text input or chat composer.
6. Make a small `SANDBOX PITCH` screen frame.
7. Place linked component instances in that screen.
8. Add one loading state and one validation-error state.
9. Write down any behavior that belongs to the frontend rather than Figma.
10. Stop and back up the file after the checkpoint.

The target is not a finished catalogue in one sitting. The target is one understandable, reusable piece at a time.

## 17. Related Documents

- [Figma_Guide.md](Figma_Guide.md): project overview, catalogue organization, foundations, components, backup, and handoff.
- [Luckiis_Beginner_Glossary.md](Luckiis_Beginner_Glossary.md): concise definitions for Figma, frontend, API, layout, accessibility, and handoff terms.
- [Creator_Frontend_Workflow.md](Creator_Frontend_Workflow.md): Creation-stage screens, states, API boundaries, and frontend behavior.
