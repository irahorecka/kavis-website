## Crops images with whitespace to have 10px whitespace around core image content.
## E.g. $ make crop-10px IN=assets/images/kavistech-logo-full.png OUT=assets/images/test.png
crop-10px:
	convert $$IN -bordercolor white -border 10 -trim temp.png && convert temp.png -bordercolor white -border 10 $$OUT;
	rm temp.png;
