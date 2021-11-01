# Introduction to brikWork
brikWork is a scripty card game maker that runs on the desktop. Text based layout files are combined with images and a data table to make cards that are exported as images or PDF files. 

## Features
 - CSS-like syntax familiar to any programmer
 - Easy to learn and powerful placement system that allows positions to be specified from any direction, and relative to other elements
 - Unitized numbers in pixels, inches, millimeters, and more
 - Text with complex character support, preliminary testing shows Arabic and Devanagari work but I'd love to hear from people who actually use these alphabets
 - Text can be structured and contextually styled with HTML
 - Beginner friendly documentation that doesn't expect you to already know how things work
 - Layouts can specify other layouts as templates and use their settings and elements
 - A suite of "briks" that allow you to program your layouts with utilities like condition testing, substrings, and math
 - Cards can be exported to single images, print ready PDF files, or images for Tabletop Simulator 


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

in your favorite editor (there's a plugin for VS Code) and run it in the brikWork app to see how it looks.

![](./img/index-shot.png)

From there you can export your cards to individual images, a texture image for Tabletop Simulator, or a PDF for print and play.

Download brikWork from the home page at [codlark.itch.io/brikWork](https://codlark.itch.io/brikwork) then take a look at the [tutorial](./Tutorial/).