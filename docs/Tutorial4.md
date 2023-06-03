# Example - Making a Card Game
There are several card makers that specialize in Magic the Gathering cards so there's little need to show you how to make MtG cards with CLS. On the other hand, MtG cards feature many things that people put in their own card games, like complex costs, inline images, and flavor text. So let's take a look at "Alchemy the Collecting", a game that totally isn't Magic the Gathering.

```{image} "./img/Stone wall.png"
```
```{image} "./img/Bees.png"
```

These cards were thrown together for this example with stock are for the main image.

## Data

Let's look at the data, which will help the rest of the layout make sense.

```
data {
title, frame, art, cost, type, effect, flavor
Stone Wall, earth, stone-wall.jpg, (any, earth), Continuous, Pay [text-icon| any]: On your opponent's next turn you may prevent one spell of that type from taking affect., These walls have held off so many invaders\, I swear you can hear them say no if you get close.
Bees, air, bees.jpg, (air, air), [], Gain 3\, 1/1 Air element Bee tokens, Not the Bees!
}
```

That's a lot of columns! We don't have to look at every one, but a couple stand outs:
 - `cost` is a list where each value is an icon name
 - `type` can be marked empty with `[]`
 - we have a macro, `[text-icon| ]` to put costs into the effect

## Special Sections

```
layout {
    template: euro-poker-deck.cls
}

macros {
    icon = <img source="img/[1]-small.png"/>
    text-icon = <img source="img/[1]-small.png" width="37" height="37"/>
}

defaults {
    font-family: Cambria
    align: left, top
}

```

The only thing we define in `layout` is a template. This particular template is from the templates for The Game Crafter, their Euro Poker Deck is the same size as MtG cards. `macros` defines two functions, both turn a cost icon name into the actual image as an image tag for text, one of which defines a small size for text. Lastly `defaults` defines some features for all the text we have.

## The Frame
```
bleed-zone {
    frame {
        type: image
        source: img/[frame]-bg.png
    }
}
```

The frame refers to the colored border around the card. In this case, where The Game Crafter expects full bleed, we use the template's `bleed-zone` element to position it. Remember, elements defined in a template keep all their properties unless you change any of them. The frame in this case also includes the boarders around the card title and text, just because it's easier to place them that way.

## Title and Cost
For reference, everything else is a child of the `safe-zone` element of the template.
```
top-bar {
    size: 100%, .25in
    title {
        type: text
        text: [title]
        x: .1in
        font-size: .2in
    }
    cost {
        type: text
        text: [for-each| [cost], [icon| [item]]\s\s]
        align: right, middle
    }
}
```

Really the only thing that might raise an eyebrow here is the `cost` element. We use a `text` element because it's an easy way to hold an arbitrary number of images, and we can adjust the alignment as needed. We could even insert newlines in between the images to make a vertical cost. We also see a use of the `[for-each| ]` function and it's helper the `[item]` variable that returns the current value of the list.

## The Art
```
img {
    type: image
    source: art/[art]
    position: 0.05in, .25in
}
```
Nothing to see here, move along.

## Type and Card Text
```
type {
    type: text
    position: 0, 2in
    size: 100%, .25in
    font-size: 10pt
    align: center, top
    text: Spell [if| [ne| [type], []], - [type]]
    
}
card-text {
    position: .1in, 2.15in
    size: 2.13in, 1in
    
    effect {
        
        type: text
        size: 100%, 100%
        font-size: 9pt
        text: [effect]
    }
    flavor {
        type: text
        size: 100%, 100%
        font-size: 8pt
        align: left, bottom
        text: [i| [flavor]]
    }
}
```
Because these are all spells of various types, we know to put "Spell" in `type`, however if there's a subtype we also want a hyphen and that subtype. `effect` and `flavor` take up the same space, and are separated with their alignment, much like the top bar above.

## Wrapping Up

That's everything! You can see how little you need to make a real card, it just takes time to find the ideal position for everything. What I recommend is to design the basic layout is something that reports real world units, like Inkscape, then translate that to CLS, that's what I did for this, although you'll still need to fine tune some numbers. 