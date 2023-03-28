# Glossary
The CLS Renderer has many moving parts and it's important to keep consistent names for things to not get too confused.

Argument
:   a value passed to a function macro.

Card
:   The final rendered object made by the generator, does not need to be an actual card. This could also be a token or board, a character sheet, or something not from the table top game space like a letter or mailer, or a sprite used by a video game.

Card Layout Script
:   The name of the programming language used by the CLS Renderer

CLS Renderer
:   The app that turns a layout file into cards

Container
:   An element that contains another element, or the layout if a given element has no container. The phrase "element container" is used to specify the first case.

Compiling
:   The process of turning elements as described by the user into object usable by the renderer

Data
:   The CSV based based data that is used to fill in and customize specific elements of a layout.

Element
:   A portion of a Layout, for example an image.

Expand
:   To process a value into one that contains no macros or escapes.

Layout
:   A template for making Assets. A layout contains data about itself, as well as a number of elements.

Layout File
:    A file containing a layout written in CLS.

Macro
:   A piece of text like `[asset-index]` that returns another piece of text. These are like the variables and functions of programming languages.

Property
:   A changeable feature of a layout or element, for example `width` or `angle`.

Rendering
:   The process of drawing elements onto a card.

Value
:   The assigned contents of a property. In `width: 1in` the `1in` is a value.
:   The term value is also used when referring to the data, where it refers to the specific values available as column macros.
 