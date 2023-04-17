# Elements and Properties

## Elements

Elements are the building blocks of a layout. Anything that is seen on a card is an element. These are the available types of elements.

 - `text` - This element renders text onto a card. The font family and color can be changed, text can be colorized and decorated (eg underlined), and structured with a subset of HTML
 - `image` - This element is used to quickly draw an image. Images can be resized.
 - `image-box` - This element is used to draw images within a box according to the elements alignment. A more thorough comparison of `image` and `image-box` is below
 - shapes - there are multiple elements for drawing basic shapes.
     - `rect` - a rectangle, with or without rounded corners.
     - `circle` and `ellipse` - both names are used for the same element. A basic circle or ellipse.
     - `line` - a line.
 - `none` - this element has nothing to draw, but can contain other elements, have a position, and rotate.

## Composite Properties
CLS makes use of two types of properties, single properties which take a single value, and composite properties which take multiple values separated by commas, for example:

 - `keep-ratio: yes` is a single property
 - `font: 1/4in, Impact, red` is a composite property

Composite properties are all made up of single properties, `font` above is made up of `font-size`, `font-family`, and `font-color`. Not all single properties are a part of a composite property, `keep-ratio` for example is only available alone. As a guideline, composite properties are recommended over single properties when available, but sometimes single properties offer better readability when using macros.

Some composite properties will be listed after their separate single properties when the values are different types. When the values are the same type, the composite property will be listed alone and merely state it's a composite property. In these cases the single properties are named for the value names shown in the description, so `size: X, Y` can be broken down into `x` and `y`.

A small number of composite properties can take optional values, such as `scale: SCALE-WIDTH(, SCALE-HEIGHT)`. In these cases the optional value is enclosed in parentheses, and the behavior if omitted will be described in the property listing.

## Common Properties

All elements share these properties.

 - `type: TYPE` - the type of the element, as listed above. This must be a literal value like the values used in the special sections; this means that macros will not be evaluated. Default value is `none`.
 - `position: X, Y` - the position of the element. Default value for both is `0`. Composite property. Allowed values are any of
     - A number with units `px`, `in`, or `mm`, either positive or negative. This positions the element's upper left to its container's upper left. This is considered the standard positioning scheme.
     - A number with units `px`, `in`, or `mm`, and with the sign `^`. This positions the element's lower right to its container's lower right. This and the above type can be combined, eg `position: 1/4in, ^1/4in` would position an element based on it's lower left.
     - A number with unit `%` which positions the element relative to its container in the same direction, eg `x: 50%` will position the left edge of the element in the middle of its container going left-to-right.
     - `center` which centers the element within its container.
 - `size: WIDTH, HEIGHT` - the size of the element. Both `WIDTH` and `HEIGHT` must be present. Default value for both is `1/4in`. Composite property. Allowed values are any of
     - A number with  units `px`, `in`, or `mm`.
     - A number with unit `%`, which sizes the element relative to its container.
 - `angle: ANGLE` - the rotation of the element in degrees, with or without the unit `deg`. Can be positive which rotates clockwise or negative which rotates counter-clockwise. Elements rotate around there center. If a container is rotated, subelements are positioned according to that rotation. Default value is `0deg`.
 - `draw: TOGGLE` - whether to draw this element, also affects any subelements. Default value is `yes`.

## The `text` Element
 
 - `text: TEXT` - the text to display. Default value is `[]`.
 - `font-size: FONT-SIZE` - the size of the text. Default value is `18pt`. Unit is one of `pt`, `px`, `in`, `mm`.
 - `font-family: FONT-FAMILY` - the font family to use. Default value is `Verdana`.
 - `font-color: FONT-COLOR` - the color of the text. Default value is `black`.
 - `font: FONT-SIZE, FONT-FAMILY(, FONT-COLOR)` - this is the composite property for the above three properties.
 - `shrink-font: LENGTH-FONT-SIZE-PAIRS` - a list of pairs that match a length for `text` to a new font size. Pairs are split by `:` colon. `LENGTH` is a number without a unit and `FONT-SIZE` uses the same units as the `font-size` property above. Default value is `()`. See the example below for more information.
 - `h-align: H-ALIGN` - the horizontal alignment of text within the element. Default value is `center`. Allowed values are:
     - `left`
     - `center`
     - `right`
     - `justify`
 - `v-align: V-ALIGN` - the vertical alignment of text within the element. Default value is `top`, allowed values are:
     - `top`
     - `middle`
     - `bottom`
 - `align: V-ALIGN, H-ALIGN` - this is the composite property for the above two single properties.
 - `decoration: DECOS` - decoration options for the text, separated by commas. Default value is `[]`. Values are allowed in any order, and each `DECO` has it's own single property that takes a toggle, allowed values are: 
     - `italic`
     - `bold`
     - `overline`
     - `underline`
     - `line-thru` or `line-through`

### HTML subset

Because CLS Renderer uses Qt for rendering cards, a subset of HTML is provided for `text` elements, such as:
 
 - `<b>` bold text, also usable thru the `[b| ]` macro which wraps it's argument in `<b> </b>` tags
 - `<i>` italic text, also usable thru the `[i| ]` macro which wraps it's argument in `<i> </i>` tags
 - `<font>` allows you to change the font family in the middle of a label
 - `<img>` places images in the text. When used in conjunction with user macros this is a convenient way to add icons to text

These are only some of the tags available, for a fuller explanation of these and more valid HTML, visit the Qt docs for the [Supported HTML Subset](https://doc.qt.io/qt-6/richtext-html-subset.html)

### `shrink-font` example

The `shrink-font` property is used to create a "shrink to fit" effect. When the text is longer than a given length, the font size is changed to match. Take the example below for a card effect box from a trading card game.

    font-size: 11pt
    shrink-font: (200: 9pt, 300: 7.5pt)
    text: [card effect column from data]

In this example, most cards will have a font size of 11pt, but if the length of an effect (minus HTML) is equal to or greater than 200 characters, the font size will be set to 9pt, and similarly with 300 characters and 7.5pt. So if the length of an effect is 256 characters, the font size would be 9pt. These sizes are check in the order they appear in.


## The Image Elements
There are two image element types, `image` and `image-box`, which are suited to different use cases. They both share these properties.

 - `source: SOURCE-PATH` - the image file to load. Most common file types are recognized, but png is recommended because it's a lossless format. Default value is `[]`, no image.
 - `keep-ratio: TOGGLE` - whether to keep the image's original aspect ratio when resizing the image. Default value is `yes`.
 - `scale: SCALE-WIDTH(, SCALE-HEIGHT)` - amount to scale image by. Unit one of `%` or `x`. Composite property. Default value is `0` which means no scaling takes place. If `SCALE-HEIGHT` is left off `SCALE-WIDTH` is used for both directions.
     - Values with unit `%` are percentages, where `100%` is full size, `50%` is half size, `200%` is double and so on.
     - Values with unit `x` are factors, where `1x` is full size, `.5x` is half size, `2x` is double and so on. This from is useful for scaling an images based on dpi, eg a 600 dpi images on a 300dpi card might use a scale value of `300/600x`

The `image` type is intended for cases where the same image will be used on every card, or where every image is the same size. This type sets the default size to `0, 0`. The final size to render an image is found with the series of checks below.
 1. If the size is left at the default, and `scale` is left at default, the image is drawn at full size. This is the default behavior.
 2. If the size is left at default and `scale` is provided, the image is scaled based on the provided value and according to `keep-ratio` when drawn.
 3. If the size is specified in only one direction the image is scaled based on that direction while maintaining the aspect ratio when drawn.
 4. If both width and height are specified, the image is scaled to that size according to `keep-ratio` when drawn.

The `image-box` type is intended for cases when images are different sizes, and provides the property:

 - `align: H-ALIGN(, V-ALIGN)` - this property takes the same values as the `align` property above. Default value is `center, middle`.

The `image-box` type uses a different drawing process than `image`
 
 1. If `scale` is provided then the images will be scaled according to `keep-ratio`.
 2. If the image is larger than the element size, it will be scaled to fit according to `keep-ratio`
 3. The image is  located within the size of the element based on the `align` property and drawn.


## The Shape Elements
CLS provides basic shapes. While mainly intended to assist in development of layouts, these may also be used, for example, to provide borders in more simple layouts, or to colorize transparent images.

All shapes share the following properties:

 - `line-width: LINE-WIDTH` - the width of the line used to draw the shape. Unit is one of `px`, `in`, `mm`. Default value is `0.01in`.
 - `line-color: LINE-COLOR` - the color of the line. Default is `black`.
 - `line-style: LINE-STYLE` - the style of the line. Default is `solid`. Allowed values are:
     - `solid`
     - `dots`
     - `dash`
 - `line: LINE-WIDTH, LINE-COLOR(, LINE-STYLE)` - this is the composite property for the above 3 properties.
 - `fill-color: FILL-COLOR` - the color on the inside of a shape. Default value is `white`.

The `rect` type has one additional property:

 - `corner-radius: X-CORNER-RADIUS(, Y-CORNER-RADIUS)` - this property controls the rounding of the corners of a rectangle. Unit is one of `px`, `in`, or `mm`. Composite property. Default value is `0, 0` which is no rounding. If `Y-CORNER-RADIUS` is left off `X-CORNER-RADIUS` is used for both directions.

The `circle` and `ellipse` types have one additional property:

 - `diameter: WIDTH(, HEIGHT)` - this property is the same as `size` except that if `HEIGHT` is not provided `WIDTH` will be used for both dimensions.

The `line` type cannot be rotated or given a size, and has two additional properties:

 - `start: X, Y` - this property is the same as `position`.
 - `end: X2, Y2` - this property defines the end point of the line. Allowed values are the same as for `position`. Composite property. Default value is `1/4in, 1/4in`, which is also the default for `size`.
