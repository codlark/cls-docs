# Undocumented Features

This page is meant to document features that are otherwise undocumented. The features on this page aren't great ideas, in fact a couple might be bad ideas, but I implemented them and I don't want to get rid of them. Nothing here is going to be documented very well, use at your own risk.

## text properties

`decoration` can be used to turn things off, not just on.
 - `no-italic`
 - `no-bold`
 - `no-underline`
 - `no-overline`
 - `no-line-thru` or `no-line-through`
 - `no-word-wrap`

That last one controls word wrap, and there is an associated `word-wrap` property. I don't know why you'd turn off word wrap tho.

## shape properties

 - `line-cap` - the cap on the end of a `line` element, one of `flat`, `square`, or `round`. the last two extend past the end of the line by half its width.

 - `line-join` - the corner shape for `rect`s with no rounding. one of `miter`, `bevel`, or`round`. really there's no use for this.

 These two can also go at the end of the `line` property in that order

There are also a couple extra line styles, `dot-dash` and `dash-dot`.

## pdf properties

- `center-in-page: TOGGLE` - if false, the cards are aligned to the left edge. you probably don't want this.

## macros

Macro syntax allows either a comma of vertical bar in any position. Technically the use of a vertical bar after a function name and a comma elsewhere is only a convention, not a rule.

`[/| VALUE ]` - the expansion macro
The expansion macro processes and expands escapes. Normally this is the last step of evaluating a value but this macro lets you do it early. As an example, you can use the expansion macro to dynamically generate macro names.

    [/| \[ [someMacro] \] ]

Because values are evaluated until there are no more macros, this would end up evaluating a macro with the name of whatever is in `[someMacro]`. Or for a more complex example

    [for-each| (red, blue, yellow), [/| \[ [item]-icon \] ] ]

This will return `[ red-icon ][ blue-icon ][ yellow-icon ]`, then these macros would be evaluated.

*[CLS]: Card Layout Script