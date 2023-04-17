# Macros

Macros are bits of text expanded by the CLS Renderer to provide dynamic, per card, text. Macros come in three varieties:

 * variable macros like `[card-index]` that simply return a value
 * function macros like `[if| ]` that process arguments, and
 * operator macros that perform special parsing for operators on their argument

## Variable Macros

The variable macros you'll most likely see are column macros, macros that are filled in by the renderer based on the current data rows, and user macros, the macros defined in the `macros` section. Here are some others.

`[]` - the empty macro
Use this macro when you don't want to fill in a value or argument and want to make it clear that the blank space is intentional.

`[row-index]` and `[row-total]`
`[card-index]` and `[card-total]`
`[repeat-index]` and `[repeat-total]`
These macros return numerical statistics about cards

 * `row` refers to the current row of the data. Cards generated from the first row of data will have a `[row-index]` of `1`
 * `card` refers to the specific card. The total number of generated cards is in `[card-total]`
 * `repeat` refers to the repetitions as defined by a repeat column in the data. `[repeat-total]` is the same as the repeat value of a given row. If no repeat column is present in the data `[repeat-index]` and `[repeat-total]` will both be `1`
 * `index` refers to the number of the current card. The second card made from a row will have a `[repeat-index]` of `2`
 * `total` refers to the total number of that category. `[row-total]` is the total number of rows

These are useful for things like generating "24 out of 50" with `[row-index] out of [row-total]` where repeated cards are not counted separately. If the layout is being generated without data, these will have an undefined value, they could be one, they could be blank.

## Function Macros

Function macros can effectively be divided into two categories, value functions and comparison functions.

### Value Functions

Value functions modify and create values.

`[b| STRING]`\
This macro is a shortcut for bolding text with `<b>STRING</b>` in labels.

`[capitalize| STRING]`\
Capitalize `STRING`. This uses a dumb algorithm of making the first letter of any word longer than 4 letters, plus the first letter overall, uppercase.

`[dup| TIMES, STRING]`\
Duplicate `STRING` `TIMES` times. When evaluating `STRING`, the macro `[d]` is set to which duplication this is, eg `[dup| 3, \s[d] times]` will return " 1 times 2 times 3 times". If `TIMES` begins with a `0` then `[d]` will start counting with zero.

`[file| FILENAME]`\
Open the file `FILENAME` and return the text.

`[for-each| LIST, STRING]`\
Evaluate `STRING` once for each item in list. When evaluating `STRING`, the macro `[item]` is set to each item in `LIST` in order. This is useful when paired with the `[args]` macro available to user function macros, eg `[for-each| [args], [item]!\s]`

`[i| STRING]`\
This macro is a shortcut for italicizing text with `<i>STRING</i>` in labels.

`[lower| STRING]`\
Convert the entirety of `STRING` to lowercase.

`[rnd| STOP]`\
`[rnd| START, STOP]`\
Generate a random number from `START` up to and including `STOP`. `START` must be a lower number than `STOP`. 

`[s| STRING]`\
This macro is a shortcut for striking thru text with `<s>STRING</s>` in labels.

`[slice| STRING, START]`\
`[slice| STRING, START, END]`\
Select a sub string from `STRING` starting at `START` and ending with `END`. If `END` is not present then the rest of the string will be selected, if it is present the specified character won't be included. If `START` or `END` begins with a `0` that argument will count the first character as `0` the second as `1` and so on, otherwise the first character is `1`. Negative numbers are also allowed, which are counted from the end of the string, so `-1` is the last character.\
`[slice| LIST, START]`\
`[slice| LIST, START, END]`\
Select a sub list from `LIST`. The `START` and `END` arguments are as above, where `START` is the first item to return.

`[substr| STRING, START, LENGTH]`\
Select a sub string of `STRING`, starting at `START` for `LENGTH`. If `START` begins with a `0` the first character will count as `0` the second as `1` and so on, other wise the first character is `1`. Negative numbers are not allowed.

```{admonition} Examples
:class: tip

    Because `[slice| ]` and `[substr| ]` are so similar and so flexible, examples for both are located on  [this page](./Selecting-Strings.md).
```

`[u| STRING]`\
This macro is a shortcut for underlining text with `<u>STRING</u>` in labels.

`[upper| STRING]`\
Convert the entirety of `STRING` to uppercase.


### Comparison Functions

Comparison functions manage compare values and return a toggle for the `[if| ]` macro, which is also described here

`[eq| LEFT, RIGHT]`\
Test if `LEFT` and `RIGHT` are equal. The arguments can be any type of value.

`[if| TEST, TRUE]`\
`[if| TEST, TRUE, FALSE]`\
Returns either `TRUE` or `FALSE` depending on `TEST`, which must evaluate to a toggle. When the first character of `TEST` is `?` the rest of the argument will be given to the comparison macro for evaluation. The `FALSE` argument is optional, and omitting it is the same as using `[]` as `FALSE`.

`[in| VALUE, ARGS...]`\
This macro takes any number of arguments. Test to see if `VALUE` is equal to any of `ARGS`.\
`[in| VALUE, LIST]`\
Test to see if `VALUE` is in `LIST`. If more arguments are provided this macro will operate as above.



`[ne| LEFT, RIGHT]`\
Test if `LEFT` and `RIGHT` are not equal. The arguments can be any type of value.

`[switch| TEST, CASE, MATCH...]`\
`[switch| TEST, CASE, MATCH..., default, DEFAULT-MATCH]`\
This macro takes any number of `CASE,  MATCH` pairs. Test to see if `TEST` is equal to any `CASE` and return the corresponding `MATCH`. If `CASE` is a list then this this macro check to see if `TEST` is in `CASE`. If the last case is `default` and `TEST` does not match any `CASE` then `DEFAULT-MATCH` will be returned.

Say you're using `[repeat-index]` to make numbered cards but you want some numbers to be drawn differently

    [switch| [repeat-index], 10, X, (6, 9), [u|[repeat-index]], default, [repeat-index]]

This would return `A` if the value is `1`, underline the value if it's `6` or `9`, or else return the unchanged repeat index.


## Operator Macros

Operator macros scan their argument for operators, special characters that the macro gives special meaning.

`[?| VALUE ]` - the comparison macro\
The comparison macro performs numeric comparison. `VALUE` is evaluated for a single comparison operator with either side being the operands, if either operand is not a number parsing will stop with an error. Units are ignored so `3in`,  `3mm`, and `3%` are all treated the same as `3`.
Valid comparison operators are:

 * `==` - equal to
 * `!=` - not equal to
 * `>` - greater than
 * `>=` - greater than or equal to
 * `<` - less than
 * `<=` - less than or equal to

When the first character of `TEST` of an `[if| ]` is `?` the rest of the argument will be given to this macro for evaluation.

    [if|? [card-index] == [card-total], Last card!, Still waiting...]

This would evaluate to "Last card!" on the last card and "Still waiting..." on every other card.

`[=| VALUE ]` - the math macro\
The math macro performs arithmetic. `VALUE` can contain any number of operators and they will be processed according to order of operations. If any operand is not a number parsing will stop with an error. Units are ignored like the comparison macro above. Operators and numbers must be separated with spaces, as in `1 + 2` but not `1+2`.
Accepted operators are:

 * `+` - addition
 * `-` - subtraction
 * `*` - multiplication
 * `/` - division
 * `%` - modulus, the remainder of division
 * `(` and `)` - grouping

To provide an example:

    [=| [card-index] / [card-total] * 100]

This would give `[card-index]` as a percent, for example the 21st card of 34 would be "61.76". We can use this to draw a progress bar as in

    bar-holder {
        width: 2in
        ...
        bar {
            type: line
            ...
            x: 0
            x2: [=| [card-index] / [card-total] * 100]%
        }
    }

The element `bar-holder` holds how long the bar can grow to, and `bar` is the actual progress bar. The same example above would get us a bar that's about an inch and a quarter long.
