# Introduction to Card Layout Script

Card Layout Script (CLS) is a language for designing cards. Cards are described as layouts that are rendered by the CLR Renderer.

Use CLS to make cards and things for print-n-play games, prototyping board games, video games, or just to jazz up your favorite TTRPG.

CLS was made because the two main card programs I used both felt lacking. The venerable nanDECK can do most anything, but the arcane syntax and the clinical documentation make it a hard to learn. The WYSIWYG [CardMaker](https://github.com/nhmkdev/cardmaker) is easy to use, but it's limitations felt stifling at times.  So I made a language and renderer that did what I wanted it to, and added some other handy features along the way. 

Some features of note:

 - Powerful placement system allowing you to locate an item from any edge, easily center things, and position things relative to another, all of which is rotation aware
 - Units for numbers are built into the syntax, as well as fractions, allowing you to use things like `1/3in` and the renderer knows what you mean
 - Rich text in the form of HTML, so you can **bold**, *italicize*, and even include images
 - Images! There's not a lot to this one, but sets of images with different proportions can be positioned to always be in the same spot. And SVG support in on the way
 - A system of macros that allow you to change any property on any part of a card on a per card basis, with functions for math, string manipulation, and conditions among others
 - Cards can be exported to PDF for home printing, textures for Table Top Simulator, or individual images
 - Everything is thoroughly documented, and if something isn't clear enough just ask and I'll gladly clarify


## How it works
Write a layout file like this one

    layout {
        size: 2.5in, 3.5in
    }
    label {
        type: text
        position: 1in, 1in
        size: 1in, 1in
        angle: 180
        font: 55pt, Segoe Script
        align: right, bottom
        text: use <u>html</u>
    }
    box {
        type: rect
        position: ^1in, ^1in
        line: 1/8in, #696969
        fill-color: transparent
    }

in your favorite editor (there's a plugin for VS Code) and give it to the CLS Renderer to see how it looks.

![](./img/index-shot.png)

From there you can export your cards to individual images, a texture image for Tabletop Simulator, or a PDF for print and play.

Download the CLR Renderer from the home page at [codlark.itch.io/CLS](https://codlark.itch.io/CLS) then take a look at the [tutorial](./Tutorial.md).


```{toctree}
:caption: Tutorials
:maxdepth: 2
:hidden:

Tutorial
Tutorial2
Tutorial3
```
```{toctree}
:caption: Reference
:maxdepth: 2
:hidden:

Quick-Ref
Special-Sections
Export-Section
Elements-and-Properties
Macros
Glossary
```
```{toctree}
:caption: Technical Stuff
:maxdepth: 2
:hidden:

Syntax
changelog
```
```{toctree}
:caption: Links
:maxdepth: 2
:hidden:

Home Page <https://codlark.itch.io/cls>
VS Code Extension <https://marketplace.visualstudio.com/items?itemName=codlark.CLS-vscode>
```