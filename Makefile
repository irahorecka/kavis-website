## Crops images with whitespace to have 10px whitespace around core image content.
## E.g. $ make crop-10px IN=assets/images/kavistech-logo-full.png OUT=assets/images/test.png
crop-10px:
	convert $$IN -bordercolor white -border 10x10 -trim temp.png && convert temp.png -bordercolor white -border 10x10 $$OUT;
	rm temp.png;

## Crops images with whitespace to have 80x175px whitespace around core image content.
crop-100-0px:
	convert $$IN -bordercolor white -border 10x10 -trim temp.png && convert temp.png -bordercolor white -border 80x175 $$OUT;
	rm temp.png;

## Crops images with whitespace to have 320x175px whitespace around core image content.
crop-small-banner:
	convert $$IN -bordercolor white -border 10x10 -trim temp.png && convert temp.png -bordercolor white -border 320x175 $$OUT;
	rm temp.png;

## Crops images with whitespace to have 10px void space around core image content.
## E.g. $ make crop-null IN=assets/images/kavistech-logo-full.png OUT=assets/images/test.png
crop-null:
	convert $$IN -border 0x0 -trim temp.png && convert temp.png -border 0x0 $$OUT;

## Removes white background from image.
## E.g. $ make transparent IN=assets/images/kavistech-logo-full.png OUT=assets/images/test.png
transparent:
	convert $$IN -transparent white $$OUT;