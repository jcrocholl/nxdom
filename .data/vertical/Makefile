WIDTH=25

.SECONDARY :

vertical.png : vertical.ppm
	pamcut -right=-16 $< | pnmtopng -transparent white > $@

vertical.ppm : negative.ppm neutral.ppm positive.ppm \
important.ppm critical.ppm
	pnmcat -leftright -white -jbottom $^ > $@

important.ppm : important.png
	pngtopnm $< | pnmcrop \
	| pnmpad -white -width $(WIDTH) -halign 0 -bottom 4 > $@

positive.ppm : positive.png
	pngtopnm $< | pnmcrop \
	| pnmpad -white -width $(WIDTH) -halign 0 -bottom 4 > $@

%.ppm : %.png
	pngtopnm $< | pnmcrop \
	| pnmpad -white -width $(WIDTH) -halign 0 -bottom 3 > $@
