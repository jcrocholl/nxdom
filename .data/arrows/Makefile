SIZE=23

all: left.png right.png up.png down.png

%.png : %.ppm
	pnmscale -width $(SIZE) $< | pnmtopng -transparent white > $@
	cp -f $@ ../../static/images/

left.ppm : right.ppm
	pnmflip -lr $< > $@

down.ppm : up.ppm
	pnmflip -tb $< > $@

up.ppm : right.ppm
	pnmflip -r90 $< > $@

right.ppm : right23.png
	pngtopnm $< | pgmtoppm "#cccccc"-white > $@
