# Figma Practical Learning Guide

**Status:** Working draft
**Applies to:** Learning the Figma skills needed for the Geminisys UI catalogue
**Companion document:** <u>[Figma_Guide.md](Figma_Guide.md)</u>

> This is a hands-on workbook, not a test. Move slowly, repeat steps, and stop at any checkpoint. The goal is to build a reliable mental picture of Figma one small object at a time.

## Guide Map

- <u>[Part I: Tools and Index](#part-i-tools-and-index)</u>: sections 1-4 explain the overall map and the basic Figma objects.
- <u>[Part II: Practice Workbook](#part-ii-practice-workbook)</u>: section 5 onward teaches the skills through small exercises.

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
5. Continue only when the current <span style="color: #e0b341;"><strong>object</strong></span> makes sense.

Figma can look like a crowded workbench. That does not mean you are doing anything wrong. Zoom in, hide panels if needed, and work on one <span style="color: #e0b341;"><strong>object</strong></span> at a time.

## 2. The Big Picture

Think of Figma as one restaurant while it is being planned and prepared. The <span style="color: #e0b341;"><strong>file</strong></span> is the whole restaurant, <span style="color: #e0b341;"><strong>pages</strong></span> are departments, <span style="color: #e0b341;"><strong>sections</strong></span> are labeled stations, <span style="color: #e0b341;"><strong>frames</strong></span> are <span style="color: #198754;"><strong>food trays</strong></span>, and the <span style="color: #e0b341;"><strong>objects</strong></span> inside them are <span style="color: #198754;"><strong>ingredients</strong></span>. Reusable <span style="color: #e0b341;"><strong>components</strong></span> are house <span style="color: #198754;"><strong>recipes</strong></span>, <span style="color: #e0b341;"><strong>variables</strong></span> are labeled <span style="color: #198754;"><strong>ingredient bins</strong></span>, and prototypes are a customer-service walkthrough.

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

When you feel lost, locate the relevant Figma <span style="color: #e0b341;"><strong>object</strong></span> on this map first: <span style="color: #e0b341;"><strong>file</strong></span>, <span style="color: #e0b341;"><strong>page</strong></span>, <span style="color: #e0b341;"><strong>section</strong></span>, <span style="color: #e0b341;"><strong>frame</strong></span>, or <span style="color: #e0b341;"><strong>layer</strong></span>.

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

- <span style="color: #e0b341;"><strong>Pages</strong></span> are major work areas in one Figma <span style="color: #e0b341;"><strong>file</strong></span>.
- <span style="color: #e0b341;"><strong>Layers</strong></span> are the individual <span style="color: #e0b341;"><strong>objects</strong></span> in the current <span style="color: #e0b341;"><strong>page</strong></span>.
- The **canvas** is the open work surface where <span style="color: #e0b341;"><strong>objects</strong></span> are placed.
- The **Properties panel** changes the selected <span style="color: #e0b341;"><strong>object</strong></span>'s size, position, color, text, and other settings.

### Anchor: one restaurant

In the restaurant analogy, a <span style="color: #e0b341;"><strong>file</strong></span> is the whole restaurant, a <span style="color: #e0b341;"><strong>page</strong></span> is a department, a <span style="color: #e0b341;"><strong>section</strong></span> is a station, a <span style="color: #e0b341;"><strong>frame</strong></span> is a <span style="color: #198754;"><strong>food tray</strong></span>, and <span style="color: #e0b341;"><strong>layers</strong></span> are <span style="color: #198754;"><strong>ingredients</strong></span> on that tray.

This is one consistent visual map, not a claim that every Figma object behaves exactly like a physical restaurant object.

### One order, from building to object

```text
RESTAURANT       DEPARTMENT       STATION          FOOD TRAY        OBJECT
File             Page              Section          Frame            Layer
Geminisys        Creator Phase     Components      Button frame     Text
```

The words to the right are smaller parts inside the words to the left. A button's text is an <span style="color: #e0b341;"><strong>object</strong></span> on its <span style="color: #198754;"><strong>food tray</strong></span>; the <span style="color: #198754;"><strong>food tray</strong></span> is inside a station; the station is on a department page. In this guide, <span style="color: #e0b341;"><strong>object</strong></span> is the Figma term, and <span style="color: #198754;"><strong>ingredient</strong></span> is the food analogy equivalent.

**Vocabulary key:** <span style="color: #e0b341;"><strong>Amber</strong></span> marks Figma terms. <span style="color: #198754;"><strong>Green</strong></span> marks food analogy equivalents. The words remain written out so the distinction does not depend on color alone.

## 4. The Smallest Useful Vocabulary

### File

A <span style="color: #e0b341;"><strong>file</strong></span> is the complete Figma document. For Geminisys, the <span style="color: #e0b341;"><strong>file</strong></span> is `Geminisys_UI_Catalogue`.

**Food analogy:** the restaurant building and its recipe binder.

### Page

A <span style="color: #e0b341;"><strong>page</strong></span> is a large workspace inside the <span style="color: #e0b341;"><strong>file</strong></span>. Geminisys currently uses:

- `01 Creator Phase`
- `02 Play Phase`
- `03 Reserve`

**Food analogy:** a restaurant department, such as the prep kitchen or dining room.

### Section

A <span style="color: #e0b341;"><strong>section</strong></span> groups related work on a <span style="color: #e0b341;"><strong>page</strong></span>. For example, the `01 Creator Phase` page can contain `FOUNDATIONS`, `COMPONENTS`, and `SANDBOX PITCH` sections.

**Food analogy:** a labeled station, such as the sauce or dessert station.

### Layer

A <span style="color: #e0b341;"><strong>layer</strong></span> is one <span style="color: #e0b341;"><strong>object</strong></span> in the layer list: text, a shape, an image, a <span style="color: #e0b341;"><strong>frame</strong></span>, or a <span style="color: #e0b341;"><strong>component</strong></span>.

**Food analogy:** one ingredient or prepared dish.

### Frame

A <span style="color: #e0b341;"><strong>frame</strong></span> is a <span style="color: #e0b341;"><strong>container</strong></span> with boundaries. It can represent a screen, a panel, a button, or a smaller layout area.

**Food analogy:** a food tray. Objects can be placed inside it.

### Component

A <span style="color: #e0b341;"><strong>component</strong></span> is a reusable <span style="color: #e0b341;"><strong>object</strong></span> with a source definition. A button <span style="color: #e0b341;"><strong>component</strong></span> lets you make consistent button copies without rebuilding each one from scratch.

**Food analogy:** the restaurant's standard recipe.

### Instance

An <span style="color: #e0b341;"><strong>instance</strong></span> is a linked copy of a <span style="color: #e0b341;"><strong>component</strong></span>. It can usually have local changes, such as a different button label, while still receiving structural updates from the <span style="color: #e0b341;"><strong>component</strong></span>.

**Food analogy:** one serving made from the recipe.

### Variant

A <span style="color: #e0b341;"><strong>variant</strong></span> is a related version of a <span style="color: #e0b341;"><strong>component</strong></span>, such as a button's default, focused, disabled, or loading state.

**Food analogy:** one dish's states, such as preparing, ready, unavailable, or sold out.

## Part II: Practice Workbook

## 5. First Practice: Make a Shape

### Goal

Select, move, resize, and recolor one rectangle.

### Anchor

This is like placing one <span style="color: #198754;"><strong>ingredient</strong></span> or plate on a clean prep counter. Nothing else needs to be understood yet.

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

You can identify which <span style="color: #e0b341;"><strong>object</strong></span> is selected, move it, resize it, and change its fill color.

## 6. Second Practice: Make a Label

### Goal

Create text and place it near a shape.

### Anchor

This is like writing a menu label or station sign. The text is an <span style="color: #e0b341;"><strong>object</strong></span>, just as the rectangle is an <span style="color: #e0b341;"><strong>object</strong></span>.

### Steps

1. Press `T` for Text.
2. Click on the canvas.
3. Type `CONTINUE TO CRUNCH`.
4. Select the text <span style="color: #e0b341;"><strong>object</strong></span>.
5. Use the right panel to change its font size.
6. Drag the text near the rectangle.
7. Select the text and rectangle together by holding `Shift` while clicking both.

### Checkpoint

The Layers panel shows separate <span style="color: #e0b341;"><strong>objects</strong></span> for the rectangle and the text. Selecting one does not automatically select the other.

## 7. Containers: Put Objects on a Food Tray

### Goal

Understand that a frame can contain other layers.

### Anchor

A <span style="color: #198754;"><strong>food tray</strong></span> holds several <span style="color: #198754;"><strong>ingredients</strong></span> while they move together. In Figma terms, the <span style="color: #e0b341;"><strong>frame</strong></span> is the parent <span style="color: #e0b341;"><strong>object</strong></span> and the text and rectangle are child <span style="color: #e0b341;"><strong>objects</strong></span>, also shown as child <span style="color: #e0b341;"><strong>layers</strong></span> in the Layers panel.

### Steps

1. Press `F` for Frame.
2. Draw a frame larger than your text and rectangle.
3. Move the rectangle and text into the frame area.
4. In the Layers panel, inspect which <span style="color: #e0b341;"><strong>objects</strong></span> are nested under the <span style="color: #e0b341;"><strong>frame</strong></span>.
5. Select the <span style="color: #e0b341;"><strong>frame</strong></span> and move it.

### Checkpoint

You can see the difference between moving the <span style="color: #e0b341;"><strong>frame</strong></span> (the parent <span style="color: #e0b341;"><strong>object</strong></span>), which moves its child <span style="color: #e0b341;"><strong>objects</strong></span> with it, and moving one child <span style="color: #e0b341;"><strong>object</strong></span> inside the <span style="color: #e0b341;"><strong>frame</strong></span>, which leaves the other child <span style="color: #e0b341;"><strong>object</strong></span> in place.

```text
FRAME / FOOD TRAY
+--------------------------------+
|  TEXT / LABEL                  |
|  RECTANGLE / PLATE             |
+--------------------------------+

Move the frame: both child objects travel together.
Move one child object: the other child object stays where it is.
```

### If it looks wrong

- If the <span style="color: #e0b341;"><strong>object</strong></span> goes behind something, check the <span style="color: #e0b341;"><strong>layer</strong></span> order in the Layers panel.
- If the <span style="color: #e0b341;"><strong>object</strong></span> is not inside the <span style="color: #e0b341;"><strong>frame</strong></span>, drag its <span style="color: #e0b341;"><strong>layer</strong></span> underneath the <span style="color: #e0b341;"><strong>frame</strong></span> in the Layers panel.
- If you select the wrong thing, click an empty part of the canvas and try again.

## 8. A Practical Translation Table

| Figma idea | Familiar anchor | Geminisys example |
| --- | --- | --- |
| <span style="color: #e0b341;"><strong>File</strong></span> | <span style="color: #198754;"><strong>Whole building or binder</strong></span> | `Geminisys_UI_Catalogue` |
| <span style="color: #e0b341;"><strong>Page</strong></span> | <span style="color: #198754;"><strong>Restaurant department</strong></span> | `01 Creator Phase` |
| <span style="color: #e0b341;"><strong>Section</strong></span> | <span style="color: #198754;"><strong>Labeled kitchen station</strong></span> | `COMPONENTS` |
| <span style="color: #e0b341;"><strong>Frame</strong></span> | <span style="color: #198754;"><strong>Food tray</strong></span> | A screen or button boundary |
| <span style="color: #e0b341;"><strong>Layer</strong></span> | <span style="color: #198754;"><strong>One ingredient on the food tray</strong></span> | Text, icon, or shape |
| <span style="color: #e0b341;"><strong>Component</strong></span> | <span style="color: #198754;"><strong>Standard recipe or mold</strong></span> | Primary button definition |
| <span style="color: #e0b341;"><strong>Instance</strong></span> | <span style="color: #198754;"><strong>Prepared copy from the recipe</strong></span> | Button used on a screen |
| <span style="color: #e0b341;"><strong>Variant</strong></span> | <span style="color: #198754;"><strong>Different operating state</strong></span> | Disabled button |
| <span style="color: #e0b341;"><strong>Variable</strong></span> | <span style="color: #198754;"><strong>Labeled ingredient bin</strong></span> | Shell background color |
| <span style="color: #e0b341;"><strong>Style</strong></span> | <span style="color: #198754;"><strong>Saved appearance recipe</strong></span> | Body text formatting |

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

A <span style="color: #e0b341;"><strong>variable</strong></span> is a named place to store a value that you expect to reuse. The value might be a color, spacing amount, number, or text value, depending on the variable type Figma supports.

### Anchor: labeled ingredient bins

Imagine preparing the same sauce for ten dishes. If one labeled <span style="color: #198754;"><strong>ingredient bin</strong></span> stores the approved sauce recipe or quantity, changing that source gives you one place to update later.

A Figma <span style="color: #e0b341;"><strong>variable</strong></span> works similarly:

```text
color/background/shell = #1E1E2E
```

Several <span style="color: #e0b341;"><strong>objects</strong></span> can use that <span style="color: #e0b341;"><strong>variable</strong></span>. If the shell color changes, you can update the <span style="color: #e0b341;"><strong>variable</strong></span> instead of hunting through every <span style="color: #e0b341;"><strong>object</strong></span>.

```text
INGREDIENT BIN
color/background/shell = #1E1E2E
		  |
		  +--> screen food tray
		  +--> button food tray
		  +--> chat panel food tray
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

1. Find the <span style="color: #e0b341;"><strong>Variables</strong></span> area in Figma's current interface.
2. Create a color <span style="color: #e0b341;"><strong>variable</strong></span> named `color/background/shell`.
3. Give it a temporary color.
4. Apply it to a frame's fill if Figma offers that control in your current plan.
5. Change the variable's color.
6. Check whether the frame updates.

### Checkpoint

You understand the relationship: the <span style="color: #e0b341;"><strong>variable</strong></span> is the labeled source value, and the <span style="color: #e0b341;"><strong>frame</strong></span> is one user of that value.

### If variables are unavailable

Do not stop your project. Write the intended token name beside the design and use a temporary color style or fill. The important first step is learning which values should be shared.

## 10. Styles: Saved Appearance Recipes

A <span style="color: #e0b341;"><strong>style</strong></span> is a saved appearance recipe. It can describe a color or text formatting, depending on what Figma supports in the current interface.

### Food analogy: the restaurant recipe card

A <span style="color: #e0b341;"><strong>variable</strong></span> is like one labeled <span style="color: #198754;"><strong>ingredient bin</strong></span>. A <span style="color: #e0b341;"><strong>style</strong></span> is the complete <span style="color: #198754;"><strong>recipe card</strong></span> saying how the finished dish should look, such as its font, size, weight, line spacing, and color.

Use a <span style="color: #e0b341;"><strong>style</strong></span> when you want a whole appearance recipe to stay consistent. Use a <span style="color: #e0b341;"><strong>variable</strong></span> when you mainly want one reusable value.

```text
VARIABLE                         STYLE
One labeled ingredient            Complete recipe card
"shell color"                     "body text appearance"
	|                                  |
	+--> reused by many ingredients   +--> reused by many labels
```

### Semantic naming

```text
Text style: typography/body
Color style: color/state/danger
Spacing variable: spacing/16
```

These names tell you where the value belongs and what job it performs.

## 11. Auto Layout: A Self-Arranging Food Tray

### The plain-language idea

<span style="color: #e0b341;"><strong>Auto Layout</strong></span> makes a <span style="color: #e0b341;"><strong>frame</strong></span> arrange its children according to rules. It is useful when text length or the number of <span style="color: #e0b341;"><strong>objects</strong></span> may change.

### Anchor: a food tray with adjustable dividers

A normal <span style="color: #198754;"><strong>food tray</strong></span> does not automatically make room when you add a larger plate. An adjustable <span style="color: #198754;"><strong>food tray</strong></span> can expand, keep spacing even, and maintain padding. <span style="color: #e0b341;"><strong>Auto Layout</strong></span> is the adjustable food tray.

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

- **Hug contents:** grow around the <span style="color: #e0b341;"><strong>objects</strong></span> inside. Like a <span style="color: #198754;"><strong>food tray</strong></span> sized to its <span style="color: #198754;"><strong>ingredients</strong></span>.
- **Fill container:** expand to use available room. Like an <span style="color: #198754;"><strong>ingredient</strong></span> filling the available space on a serving shelf.
- **Fixed:** stay at a deliberate size. Like a standard button height or icon tile.

## 12. Components and States

### Goal

Turn the button into a reusable <span style="color: #e0b341;"><strong>component</strong></span> and describe its states.

### Food analogy: the house recipe

If a restaurant prepares the same dish many times, it keeps a house <span style="color: #198754;"><strong>recipe</strong></span>. If the <span style="color: #198754;"><strong>recipe</strong></span> changes, future servings follow the new <span style="color: #198754;"><strong>recipe</strong></span>. A <span style="color: #e0b341;"><strong>component</strong></span> serves a similar purpose for interface <span style="color: #e0b341;"><strong>objects</strong></span>.

### Steps

1. Select the Auto Layout button <span style="color: #e0b341;"><strong>frame</strong></span>.
2. Choose **Create component**, or press `Ctrl+Alt+K` on Windows.
3. Rename it `Button / Primary`.
4. Create or define related states: Default, Hover, Focused, Disabled, and Loading.
5. Keep text or icon changes in addition to color changes where appropriate.
6. Insert a linked <span style="color: #e0b341;"><strong>instance</strong></span> from the Assets panel into a screen section.

### Checkpoint

You can point to the reusable source <span style="color: #e0b341;"><strong>component</strong></span> and the linked <span style="color: #e0b341;"><strong>instance</strong></span> placed in a screen.

### Important distinction

A <span style="color: #e0b341;"><strong>component</strong></span> is the reusable definition. An <span style="color: #e0b341;"><strong>instance</strong></span> is the copy used in a screen. A detached copy no longer receives updates from the <span style="color: #e0b341;"><strong>component</strong></span>, so detaching should be unusual and intentional.

```text
HOUSE RECIPE                    SERVINGS
Button / Primary  ----------->  screen button 1
	   |                         screen button 2
	   +-- update recipe         screen button 3
		   updates linked servings
```

## 13. Screens and Prototypes

### Frame as screen

A screen <span style="color: #e0b341;"><strong>frame</strong></span> is a bounded drawing of a possible application viewport. Create desktop practice <span style="color: #e0b341;"><strong>frames</strong></span> at `1440 x 900` and `1920 x 1080` when following the Geminisys guide.

### Prototype as demonstration

Prototype connections show how someone could move from one <span style="color: #e0b341;"><strong>frame</strong></span> to another. They are like a customer-service walkthrough from ordering to receiving a dish.

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

Look in the Layers panel and select the named <span style="color: #e0b341;"><strong>layer</strong></span> there. You may be clicking a child <span style="color: #e0b341;"><strong>object</strong></span> when you need its <span style="color: #e0b341;"><strong>frame</strong></span>, or an overlapping <span style="color: #e0b341;"><strong>object</strong></span> may be in front.

### “The text disappeared.”

Check the text color, layer order, and whether the text is inside a frame with clipping enabled. Use the Layers panel to select it directly.

### “The button is too small.”

Check whether its <span style="color: #e0b341;"><strong>frame</strong></span> is set to **Hug contents**, whether the text is clipped, and whether padding is large enough.

### “The object moved unexpectedly.”

Undo once with `Ctrl+Z`, then inspect which <span style="color: #e0b341;"><strong>layer</strong></span> is selected. You may have moved a <span style="color: #e0b341;"><strong>frame</strong></span>, a child <span style="color: #e0b341;"><strong>layer</strong></span>, or several selected <span style="color: #e0b341;"><strong>objects</strong></span> together.

### “The copied object does not update.”

Check whether it is an <span style="color: #e0b341;"><strong>instance</strong></span> linked to the <span style="color: #e0b341;"><strong>component</strong></span>. If it is a detached copy, it will not receive <span style="color: #e0b341;"><strong>component</strong></span> changes.

### “Everything feels visually overwhelming.”

Zoom in, close or collapse panels, work inside one named section, and select only one object at a time. Use the Layers panel as your map instead of scanning the entire canvas.

### “I do not know what to do next.”

Return to the last checkpoint. If the result is not visible, undo the last action and repeat only that action. Do not restart the whole file.

## 15. Learning Checkpoints

Pause after each milestone:

- [ ] I can identify a <span style="color: #e0b341;"><strong>page</strong></span>, <span style="color: #e0b341;"><strong>section</strong></span>, <span style="color: #e0b341;"><strong>frame</strong></span>, and <span style="color: #e0b341;"><strong>layer</strong></span>.
- [ ] I can make and edit a rectangle and a text label.
- [ ] I can find a selected object's properties in the right panel.
- [ ] I can place <span style="color: #e0b341;"><strong>objects</strong></span> inside a <span style="color: #e0b341;"><strong>frame</strong></span>.
- [ ] I understand a <span style="color: #e0b341;"><strong>variable</strong></span> as a reusable named value.
- [ ] I understand a <span style="color: #e0b341;"><strong>style</strong></span> as a saved appearance recipe.
- [ ] I can make a button that grows around its label.
- [ ] I understand the difference between a <span style="color: #e0b341;"><strong>component</strong></span> and an <span style="color: #e0b341;"><strong>instance</strong></span>.
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

- <u>[Figma_Guide.md](Figma_Guide.md)</u>: project overview, catalogue organization, foundations, components, backup, and handoff.
- <u>[Luckiis_Beginner_Glossary.md](Luckiis_Beginner_Glossary.md)</u>: concise definitions for Figma, frontend, API, layout, accessibility, and handoff terms.
- <u>[Creator_Frontend_Workflow.md](Creator_Frontend_Workflow.md)</u>: Creation-stage screens, states, API boundaries, and frontend behavior.
