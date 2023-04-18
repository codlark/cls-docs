# Special Sections

The special sections control how the CLS Renderer operates, these are:

 - `layout` - which holds the settings for the overall layout of the cards and settings for how to interpret values.
 - `macros` - which holds user defined macros.
 - `defaults` - which holds default values for element properties.
 - `data` - which holds the data table used to generate cards.

## The `layout` Section

The `layout` section follows the standard property-value format.

 - `size: WIDTH, HEIGHT` - size of the card. Default value is `1in` for both values. Unit can be one of `px`, `in`, or `mm`.
 - `bleed: BLEED-WIDTH(, BLEED-HEIGHT)` - bleed area for the card. Bleed refers to the area that is printed but not seen in a final copy. Unit can be one of `px`, `in`, or `mm`. Default value is `0, 0`
 - `dpi: DPI` - dots (pixels) per inch used when converting inches and millimeters to pixels. Default value is `300`. No units are used for this number.
 - `template: LAYOUT-PATH` - another layout to load in as a template. All properties and sections from the template will be overwritten by this layout. Any elements in the template will be drawn first before any elements defined by this layout.
 - `data: FILE-PATH` - external data table to use, instead of the `data` section. Default value is `[]` which uses the `data` section.
 - `csv: DIALECT` - dialect of csv to use for parsing the data table. Default value is `CLS`. Can be one of: 
     - `CLS` - the native dialect used by CLS, as described in [Syntax](./Syntax.md), which works well for hand written data.
     - `excel` - the dialect exported by spread sheet programs like Microsoft Excel and Google Sheets. This is a strict dialect and only recommended when using CSV data exported by another program.

## The `macros` Section

The `macros` section uses a unique syntax to define user macros, which return their defined value. User macros can either be variables or functions. For example:

    macros {
        blueish-gray = #8080aa
        the = THE [lower| [1] ]
    }

Which can be used as

    some-element {
        ...
        text: [the| [card-name] ]
        font-color: [blueish-gray]

    }

When making functions the arguments passed to the macro are reachable by number as the macros `[1]`, `[2]`, `[3]` and so on. Also available to a function ares:
 
 - `[arg-total]` - the number of arguments passed to the macro
 - `[args]` - all the arguments passed to the macro as a list

## The `defaults` Section

The defaults section defines default values for element properties, and as such looks like an element section with property: value format. The `defaults` section can feature any property an element can, such as `size`, `text`, or `scale` except `type`. When using shortcut properties in defaults, individual values can be changed in later elements, for example: 

    defaults {
        line: 0.1in, magenta
    }
    ...
    box {
        type: rect
        line-width: 50px
        line-style: dots
    }

The element named `box` will have a line that's 50px wide, dotted, and magenta.

## The `data` Section

The `data` section contains the data table, and uses CSV syntax. An alternate data table can be provided with the `data` property of the `layout` section. The dialect used to parse the data table is defined by the `csv` property of the `layout` section.
