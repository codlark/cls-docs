# Chapter 2

In chapter 1 we looked at a simple layout for a set of cards for Werewolf. This chapter will continue working on those cards.

## The Rect Element

brikWork offers some limited elements for drawing shapes. We'll be looking at `rect` but there's also `circle` and `line`. Shapes are great for placeholders until you get final graphics, simple layouts, or colorizing transparent images. The color of the shape and the line used to draw the shapes are also fairly flexible, check out the section on [Element Shapes](../Elements-and-Properties/#the-shape-elements) for more.

So, let's look at a simple border.

    role-border {
        type: rect
        position: center, .5in
        size: 1.5in, .25in
        corner-radius: .1in
    }

Pretty easy! We give it the same geometry as the role so it fits it, and the `corner-radius` property rounds the corners slightly. Just put this after the role section and let's take a look

<img src="../img/border-test.png">

Well that's not right at all! The problem is brikWork is doing what it was told to do. Elements are drawn in the order they're seen in the layout. `rect` elements have a white fill by default. Because we put the elements in the wrong order by putting this after the "role" element it drew over the text. oops.

There are a few ways to fix this. First is to rearrange the elements. We could set the `fill-color` property of "role-border" element to `transparent` so it wouldn't have any fill. Or we could make the border contain the text.

    role-border {
        type: rect
        position: center, .5in
        size: 1.5in, .25in
        corner-radius: .1in
        role {
            type: text
            size: 100%, 100%
            font: 36pt, Palatino Linotype
            font-color: [if| [eq| [role] | werewolf ] | [dark-red] | black ]
            align: center, middle
            text: [capitalize| [role] ]
        }
    }