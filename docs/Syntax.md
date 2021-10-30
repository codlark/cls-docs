# Syntax
This page is meant as a thorough, technical explanation of the syntax, parsing, and card generation of brikWork. It is not meant to be a learning tool, rather a reference in the even that something doesn't act as expected.

## Top Level Syntax

The 'top level' refers to the first layer of sections in a layout, where the special sections are defined.

Sections are a name followed by contents contained within curly braces.

    layout {

    }

Section names can contain white space, but it's not recommended. This form is a 'section definition'. The top level of the file can only contain section definitions.

## Whitespace

Whitespace refers to non visible characters, in the context of brikWork this means spaces and tabs. White space is ignored on boundaries, but left intact within names and values. in the following example, ignored whitespace is left blank, while non-ignored whitespace is marked with `•`.

    briks {
        my•name = my•name•is•[ some•column ]
    }
    this•section { draw : no }

## Property Syntax

All sections except for the `briks` section and the `data` section use 'property syntax'. Properties are a name followed by a colon, text, then a terminus, which is one of a new line, a semicolon, or the end of a section.
    
    image {
        scale: 50%; keep-ratio: yes
        source: img.png}

Some properties are 'composite properties' and some are 'single properties'. Single properties only take a single value and the entirety of text between the colon and the terminus becomes the value. Composite properties take multiple values. The text between the colon and the terminus is divided by commas into separate pieces of text when the property is seen by the parser when the layout is first loaded. Attempting to use a single brik to fill multiple values will result in errors.

Properties do not need to be indented within a section, this is merely a convention to make layouts easier to read.

## Subsections

A subsection is a section definition contained within another section.  Only the `export` special section and element sections can contain subsections.

## Definition Syntax

Definition syntax is only allowed within the `briks` special section, and is used to name and define briks. Brik definitions are a name followed by a an equals, text, then a terminus, much like property syntax.

    briks {
        some-color = #343390
        another color = #769870
    }

Names can contain whitespace.

## Data Syntax

The `data` special section uses a common format called comma separated value, or CSV for short. CSV is an old format and as such there are multiple dialects. brikWork recognizes both it's own dialect optimized for writing data for layout files by hand, and the "excel" dialect used by spreadsheet applications that is meant for programmatic generation and consumption. This document will only describe the former.

The contents of the `data` special section is called the 'data'. Rows are split into rows on newline characters and there is no way to change this behavior.
The top row of the data is a row of 'headers', these will become the names of column briks by which the text of the data can be reached. If there are any blank headers they will be ignored. If a row does not provide text for every column, the unspecified columns will be given blank text. 

    color left, color center,, color right
    red, blue, yellow
    black, , white
    , purple
    orange, green

This example creates three column briks, `[color left]`, `[color center]`, and `[color right]`, and the following four rows.

 - "red", "blue", and "yellow"
 - "black",  "", and "white"
 - "",  "purple", and ""
 - "orange",  "green", and ""

Each row will generate a single card. And for each card, the column briks will resolve to their respective text.

## Brik Syntax

Briks are the namesake of brikWork, and come in two varieties, variable briks that return text, and function briks take 'arguments' to return a computed text. Briks are a name surrounded by square brackets. In function briks a vertical bar is used to separate the name from the arguments, and the arguments from each other

    some-element {
        draw: [in| [repeat-index] | 1| 2| 4| 6]
    }

By convention, spaces are not put around names, but are put around arguments, with the exception of numbers, where a space is only put before literal numbers.

## Comments
A comment is a line of text that is ignored by the parser. Comments must be on their own line and their first non whitespace character must be a pound.

    #this is a comment

Comments can appear in any section.

## Text and Values

Anything provided to property is considered text until it gets processed at card generation time. Text is turned into a value, depending on how a given property processes this text, each time a card is generated. There are two kinds of values, generated values and literal values.

A generated value is any text that contains briks. This includes column briks. Any briks found are resolved into text. If the text contains briks after this, those briks are resolved. This is repeated until there are no more briks found in the text. The text is then treated as a literal value.

A literal value is text that does not contain briks. This includes special values such as the `center` used by the `position` property. properties belonging to special sections only take literal values, as does the `type` property of elements.

## Number Syntax

Numbers in brikWork are made up of:

 - a sign
 - an integer portion
 - either 
     - a decimal point
     - a decimal portion
 - or
     - a space or decimal point
     - a fractional portion
 - a unit

A sign is one of `+`, `-`, or `^`. If no sign is given the sign of `+` is used. Only some properties and briks allow negative numbers with the sign `-`. The sign `^` is only allowed with the `position` property.

The integer and decimal portions are made up of the digits `0` thru `9`; hexadecimal numbers are not allowed. The decimal point and decimal portion are not required for whole numbers. The integer portion is not needed for numbers between 1 and 0 or numbers between 0 and -1.

The fractional portion is made up of a `/` with digits on either side. If a number is just a fractional portion is does not need a decimal point.

The allowed units are listed in the property description, with the first listed unit being the default unit used if the number does not have a unit. 

Spaces are not allowed in numbers. Examples of numbers include

    0
    1.2in
    44%
    -4.4
    5
    5.5
    5 1/2
    .5
    1/2

When numbers are used as arguments to a brik, be it the math brik, the slice brik, or any other, units are ignored, and may even be an error.

    [if|? 1mm == 1in | will always be true | this is never seen on a card ]

## Toggle Syntax

A toggle is a value that is either true or false, on or off. Multiple values are allowed for each direction to better suit the property. True values are

 - `true`
 - `yes`
 - `on`

False values are:

 - `false`
 - `no`
 - `off`

## Color Syntax

Colors use the standard hex code format, a pound sign with 6 or 8 hexadecimal numbers after, in the order transparency, red, green, blue, such as `#ff454545` or `#808000`. A collection of named colors are also available, with names taken from the [SVG color keyword names](https://www.w3.org/TR/SVG11/types.html#ColorKeywords) with the addition of `transparent` which is a fully transparent color.

## Strings

Any value that is not a number, a toggle, or a color is a string, this includes file paths and fixed values such as `italic` or `dots`. String values are the only place escapes are processed. A blank string can be indicated with the blank brik `[]`.

### Escapes

An escape is a sequence of characters used to indicate that some part of the escape is nor parsed as normal. brikWork uses a common method of using the backslash to prevent the parser from seeing the next character.

    text: I might\; or I might not.

In this example the first semicolon is escaped and the value for the `text` property is "I might; or I might not." Four characters are treated specially when they are escaped.

Escape | Meaning | Escape | Meaning
------ | ------- | ------ | -------
`\n` | a new line | `\s` | a space
`\t` | a tab | `\\` | a literal backslash

Every other character is left alone and passed along without transformation. This includes the semicolon above and the various separators and delimiters described elsewhere. Escapes are transformed after the whitespace is stripped from a value, so a single `\s` would create a value of " ". This can be used to put whitespace at the edge of a value.

When using the brikWork dialect of CSV escape syntax can be used to include a comma in a value.

### File Paths
A file path is a path to a file or folder in the file system. Properties that take paths have their value marked with `-PATH` in their description. Because brikWork uses the same character as Windows uses as a file path separator, the forward slash is also allowed as a file path separator by brikWork, and will be converted as appropriate.

    source: imgages/backgrounds/[type].png

# Generation

Generation is the process of turning a parsed layout into cards. If no data is present, only one card will be generated, and the index and total briks will all resolve to `1` or `[]`.

If there is data present, each row will generate at least one card. If the data contains a column named repeat that column must only contain numbers, positive only and no unit, and each row will generate as many cards as specified by the repeat value.

For each row, each element of the layout is processed. For each element, each property text is turned into a value, then that element is drawn to the card. Cards sit in a buffer until they are exported. Errors in parsing the file, turning text into values, or trying to use values to draw elements, will cause an error to be reported to the user. 