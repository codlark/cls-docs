# Looking at - Playing Cards

This guide (and the next one) is less a tutorial, and more of a look at how a design is put together with some explanation thrown in for good measure. Just like with the Werewolf example before, all the images used and the final layout files are provided with CLR.

The first thing we're going to look at with playing cards are the indexes. This files pretty simple.

    layout {
        size: 2.5in, 3.5in
    }
    export {
        destination: cards/
        bulk {
            name: [rank][suit].png
        }
    }
    macros {
        black = #1a1a5e
        red = #ff1569
        rank = 0
    }
    upper-left-index {
        position: 1/8in, 1/8in
        size: .3in, .6in
        number {
            type: text
            size: .3in, .3in
            font: 1/4in, Consolas
            font-color: [if| [in| [suit] | spade | club ] | [black] | [red] ]
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
            font-color: [if| [in| [suit] | spade | club ] | [black] | [red] ]
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

I'm just going to point out a few major things for now, starting from the top.
 
 - we define two user macros, `[black]` and `[red]`, set to the colors of the pip
 - a third user macro is defined and set to rank. This is more of a placeholder on this layout
 - 