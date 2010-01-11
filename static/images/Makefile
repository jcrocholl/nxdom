WIDTH=20

.SECONDARY :

vertical.png : vertical.ppm
	pnmtopng $< > $@

vertical.ppm : negative.ppm neutral.ppm interesting.ppm \
important.ppm critical.ppm
	pnmcat -leftright -white -jbottom $^ > $@

important.ppm : important.orig.png
	pngtopnm $< | pnmcrop \
	| pnmpad -white -width $(WIDTH) -halign 0 -bottom 4 > $@

interesting.ppm : interesting.orig.png
	pngtopnm $< | pnmcrop \
	| pnmpad -white -width $(WIDTH) -halign 0 -bottom 4 > $@

%.ppm : %.orig.png
	pngtopnm $< | pnmcrop \
	| pnmpad -white -width $(WIDTH) -halign 0 -bottom 3 > $@
