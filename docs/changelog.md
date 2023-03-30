# Changelog
This page collects the changes made to CLS Renderer over time

## v1.0
The program has been renamed to CLS Renderer, and briks have been renamed macros.

### added
 - `scale` property on `image` and `image-box` now takes factors with unit `x` in addition to percentages. `scale: 2x` is the same as `scale: 200%`
 - `[switch| ]` macro. The first argument is a test, the rest of the arguments are put into case|result pairs. if test equals a case the result is returned.
 - A new list value type that looks like `(a:b:c:d)` or `:` for an empty list
 - New macros, and alterations to existing macros to make use of this new type
     - `[in| ]` will check if its second argument is a list, and if so will check if the test value is in that list
     - `[slice| ]` will operate on list items, and will return a list, when passed a list instead of a string
     - `[for-each| ]` evaluates a body for each item in a list
     - `[length| ]` returns the length of a list or string
     - `[args]` is available to user function macros to return all arguments passed to the macro as a list
 - "Clear Image Cache" button to the interface.
### changed
 - the `briks` section has been renamed `macros` as the name brik has been replaced by macro
 - the `output` property on export sections has been renamed to `destination`
 - mixed fractions can have their whole number separated from fraction component with a space, a period, or a slash. These three are all valid: `1 1/2` `1.1/2` `1/1/2`
### fixed
 - parsing mixed fractions in the math macros now works as intended
 - using the `[file| ]` macro with a file that doesn't exist/won't open should give a proper error now.
 - using `^` when the parent is layout and bleed is non zero now works as intended
 - there was a rounding error when calculating the full size of a card with bleed greater than 0, it's been fixed

### removed
 - The `[substr| ]` macro has been removed. Use slice instead

## v 0.6
### added
 - composite properties, which take multiple values and pass them off to specific properties. Composite properties are also preferred when available
 - `export` section with subsections that describe how to export to various targets
 - `scale` property to `image` and `image-box` element types to control image size proportionately
 - users can now make function briks. If a user brik uses the briks `[1]`, `[2]`, and so on they'll be filled in by the arguments passed to the brik
### changed
 - properties and other names previously in camelCase, like `fontSize` now use hyphen as in `font-size` and `asset-index`
 - fractional numbers now use a space instead of a decimal point
### removed
 - `name` property on `layout` section
 - dedicated `pdf` section, now merged with new `export` section
### fixed
 - rotating `image-box` elements is less surprising

### note
 - added in 0.5 but not mentioned, a `[rnd| ]` brik


## v 0.5
 - added: `imageBox` element type, which aligns images within its box
 - added: `csv` property to layout that controls what dialect of csv to parse data as
 - changed: unknown properties are no longer errors

## v 0.4
 - added: more units! checkout [Values](../Values/) for how they work
 - added: `[slice| STRING | START | STOP]` takes substring of `STRING` like `[substr| ]` but uses start and stop positions instead of a start position and a length
 - added: support for parenthesis to the math brik, infact the whole thing has been rewritten
 - added: pdf export
 - changed: the `[substring| ]` brik has been renamed to `[substr| ]`
 - changed: the math brik has been changed to `[=| ]` and has different semantics

## v 0.3
 - added: A graphical interface
 - added: elements can now contain other elements
 - added: `defaults` section
 - added: `[s| ]` and `[u| ]` for strike thru and underline respectively
 - changed: `names` section now called `briks`
 - changed: new css style syntax
 - changed: image resizing ruels have been tweaked
 - changed: completed the playing card example and corresponding help page
 - changed: tweaks to the csv dialect
 - fixed: layouts without a `layout` section now emit a helpful error
 - fixed: somehow the `[file| ]` brik wasn't registered properly, it's fixed now

## v 0.2
 - added: templates for layouts
 - added: a new playing card example
 - added: `draw` property on elements that controls if an element gets drawn
 - added: math brik, `[#| ]`, that processes arithmetic
 - added: `[file| ]` brik that loads in the contents of a file
 - changed: syntax is now in a more modern colon-indent style
 - changed: images are now cached when loaded for the first time
 - fixed: single column data sets now work right