# Looking at - Playing Cards

On this page we're going to look at making a deck of playing cards, including jokers. We'll look at when to use templates, and how to use them. This guide  is less a tutorial, and more of a walkthrough. Just like with the Werewolf example before, all the images used and layout files are provided with CLS.

## Deck Structure

Templates are used whenever multiple card layouts use the same or similar properties and elements. In the case of playing cards this means the indexes and the special sections. Then the aces, ranks, face cards, and jokers each use a separate layout that uses the index layout as a template.

## Indexes

Because it's going to be the first thing the CLS Renderer sees, let's look at indexes.cls

    layout {
        size: 2.5in, 3.5in
    }
    export {
        destination: cards/
        bulk {
            name: [suit][rank].png
        }
    }
    macros {
        red = #ff1569
        black = #1a1a5e
        rank = 0
    }
    upper-left-index {
        position: 1/8in, 1/8in
        size: .3in, .6in
        
        number {
            type: text
            size: .3in, .3in
            font: 1/4in, Consolas
            font-color: [if| [in| [suit], spade, club], [black], [red]]
            align: center, top
            text: [rank]
        }

        pip {
            type: image
            position: center, .3in
            source: images/[suit]-small.png
        }
    }

    lower-right-index {
        position: ^1/8in, ^1/8in
        size: .3in, .6in
        angle: 180

        number {
            type: text
            size: .3in, .3in
            font: 1/4in, Consolas
            font-color: [if| [in| [suit], spade, club], [black], [red]]
            align: center, top
            text: [rank]
        }

        pip {
            type: image
            position: center, .3in
            source: images/[suit]-small.png
        }
    }

    data{
    suit
    spade
    heart
    club
    diamond
    }

There are actually quite a few design choices in selecting size and position of the indexes, but beyond that
 
 - we define two variables, `[black]` and `[red]`, set to the colors of the pips, we use these for the font color of the rank
 - a third variable, `[rank]` is defined and set to 0. This is more of a placeholder on this layout, and will get filled in by each layout
 - the lower right index uses caret positioning and is rotated, but otherwise is the same as the upper left index
 - the data section only features the suits, this is because we can to replace it on every

## Aces

The aces are pretty simple because they can inherit so much from the index layout, let's see how little aces.cls does

    layout {
        template: indexes.cls
    }

    macros {
        rank = A
    }

    ace {
        type: image
        position: center, center
        source: images/[suit]-big.png
    }

There really isn't a lot there, is there? We define indexes.cls as our template, set `[rank]` to `A` and place the image. We don't even have to use different data. Let's take a look at this now.

```{image} ./img/aces.png
```

```{admonition} Where the Images Come From
As an aside, the art for these cards is pulled from a couple different projects I've worked on in the past. Also, the different size pips are tweaked to look better at their specific size.
```

## Ranks

The ranks do a lot in their layout, so I'm only going to show parts of it

    layout {
        template: indexes.cls
    }
    macros {
        rank = [=| [repeat-index] + 1]
    }

    defaults {
        source: images/[suit].png
    }

    row1 {
        position: .5in, .5in
        size: 1.5in, .5in
        draw: [in| [rank], 8, 9, 10]
        col1 {
            type: image
        }
        col3 {
            type: image
            x: ^0
        }
    }
    ...
    row4 {
        position: 0.5in, center
        size: 1.5in, .5in
        col1 {
            type: image
            draw: [in| [rank], 6]
        }
        col2 {
            type: image
            x: center
            draw: [in| [rank], 3, 5, 7, 9]
        }
        col3 {
            type: image
            x: ^0
            draw: [in| [rank], 6]
        }
    }
    ...
    row7 {
        position: 0.5in, ^.5in
        size: 1.5in, .5in
        angle: 180
        draw: [in| [rank], 8, 9, 10]
        col1 {
            type: image
        }
        col3 {
            type: image
            x: ^0
        }
    }

    data {
    repeat, suit
    9, spade
    9, heart
    9, club
    9, diamond
    }

I wasn't kidding when I said this did a lot! We use indexes.cls as a template, but that's about the only thing it does the same as the aces. You'll see `[rank]` is defined as adding one to `[repeat-index]`, that way we can use a repeat column without having to skip 1 or ignore it in the output. In the `defaults` section we define the default image to load as the pip of the current suit so we don't have to put it 10 different places.

The pips are were things get interesting. We define them a row at a time, then in each row we name them by column. Then we draw them based on their rank by checking to see if the pip should be seen for this rank. You can see how caret positioning and `center` make it simple to position everything.

```{image} ./img/ranks.png
```

I've shrunk the cards down some, but you can see how the pips get laid out properly.

## Face Cards

    layout {
        template: indexes.cls
    }

    macros {
        rank = [substr| [royal], 1, 1]
    }

    portrait {
        type: image
        position: center, center
        source: images/[color][royal].png
    }

    data {
    suit, color, royal
    spade, black, Jack
    spade, black, Queen
    spade, black, King
    heart, red, Jack
    heart, red, Queen
    heart, red, King
    club, black, Jack
    club, black, Queen
    club, black, King
    diamond, red, Jack
    diamond, red, Queen
    diamond, red, King
    }

Other than `[rank]`, which is set to the first character of `[royal]`, there isn't anything here we haven't seen before. I'm not going to put a picture of any face cards here, as you can probably assume what it looks like.

## Jokers

    layout {
        template: indexes.cls
    }

    export {
        bulk {
            name: [name].png
        }
    }

    upper-left-index {
        number {
            size: .75in, .5in
            font-color: [color]
            align: center, top
            text: [b|J]oker
        }
        pip {
            draw: off
        }
    }

    lower-right-index {
        number {
            size: .75in, .5in
            font-color: [color]
            align: center, top
            text: [b|J]oker
        }
        pip {
            draw: off
        }
    }

    portrait {
        type: image
        position: center, center
        source: images/[name].png
    }

    data {
    color, name
    [black], bigJoker
    [red], smallJoker
    }

The jokers do quite a bit. The big thing is the way they modify the indexes. Because they don't have a true rank and no suit, they don't need the standard index, but the position is still good. So they turn off the pip index and change the number index to show Joker, like so

```{image} ./img/jokers.png
```
The way this works is that when you load in a template, the special sections, elements, properties, and data that belong to the template are all put in memory. When the main layout gets loaded, that layout's elements, properties, etc. get put in the exact same place, overwriting anything that's there, and just as importantly, leaving anything that the layout doesn't change untouched. So when jokers.cls changes the `text` property without touching `position`, the `position` set in indexes.cls is kept.

And with that we have a deck of 54 cards and hopefully a better understanding of how templates work.