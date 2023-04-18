# Export Section
Exporting cards produced by CLS Renderer is controlled by the `export` section and its subsections, each one controlling a different export target. These targets are:
 - `bulk` - this target exports cards to individual images
 - `pdf` - this target exports the cards to a pdf, useful print and play
 - `tts` - this target exports the cards into an image suitable for Tabletop Simulator

The `export` section and subsections use property: value format. These properties are common to all export targets:

 - `destination: FOLDER-PATH` - destination folder for exporting cards. Default value is `[]` which uses the same folder as the layout folder.
 - `name: NAME` - the name to use when generating the files. Each export target handles the name differently due to each target saving different kinds of files.
 - `include-bleed: TOGGLE` - whether to include the bleed area when exporting cards. Default value is `yes` for `bulk` export targets and `no` for all others.

Additionally the `export` section acts like the `defaults` section, but for export targets

    export {
        name: cards
        bulk {
            name: card[card-index].png
        }
    }

In this example the `pdf` and `tts` export sections will export cards as `cards.pdf` and `cards.png` while `bulk` will number each card.

## The `bulk` Export Target
The `bulk` subsection contains properties for exporting cards to individual images.

 - `name: NAME` - the name to use when saving the individual images. If no macros are present in `NAME` the variable `[card-index]` will be added to the front. Default value is `[card-index]card.png`.

## The `pdf` Export Target
The `pdf` subsection controls the exporting process for PDF files.

 - `name: NAME` - the name to save the PDF as. The file extension will always be converted to `.pdf`. Default value is `[]` which gives the pdf the same name as the layout file.
 - `margin: X-MARGIN(, Y-MARGIN)` - the page margin. Cards will not be put in the margin. If `Y-MARGIN` is left off `X-MARGIN` will be used for both. Unit is one of `in` or `mm`. Unit for both must be the same. Default value for both is `.25in`, most printers lose accuracy when closer than this to the edge of the page.
 - `border: WIDTH` - the width to draw a border around the cards with. If `0` no border will be drawn. A value of `1mm` will be appear on screen but not when printed. Unit is one of `in` or `mm`. Default value is `0.01in`
 - `page-size: SIZE` the size of the page. Default value is `letter`. Must be one of: 
     - `letter` - which is 8 1/2 by 11 inches or
     - `A4` - which is 297 by 210 millimeters
 - `orientation: ORIENTATION` - the rotation of the page, either `portrait` or `landscape`. The default value is `portrait`.


## The `tts` Export Target
The `tts` subsection is a specialized export target for Tabletop Simulator, which expects cards laid out in a grid. Tabletop Simulator also puts specific limits on the size of the image, namely that it must be 2-10 cards wide, 2-7 cards tall, and at max 4096 pixels wide. These are enforced by the CLS Renderer.

 - `name: NAME` - the name to save the image as. If no file extension is present the extension `.png` will be added. Default value is `[]` which gives the image the same name as the layout file.
 - `size: WIDTH, HEIGHT` - size, in cards, of the generated image. `WIDTH` must be between 2-10 inclusive and `HEIGHT` must be between 2-7 inclusive. Default is `5, 7`; a `WIDTH` of `5` is the max a US poker sized card at 300 dpi can have and keep under the 4096 pixel limit.

If there are more cards than can fit in a single generated image, the CLS Renderer will generate multiple images with a number appended to the front, eg `1cards.png` and `2cards.png`.
