SIZE=23

all: left.png right.png up.png down.png

%.png : %.ppm
	pnmscale -width $(SIZE) $< | pnmtopng -transparent white > $@
	cp -f $@ ../../static/images/

left.ppm : arrow.ppm
	pnmflip -lr $< > $@

right.ppm : arrow.ppm
	cp -f $< $@

up.ppm : arrow.ppm
	pnmflip -r90 $< > $@

down.ppm : up.ppm
	pnmflip -tb $< > $@

right.ppm : right373.png
	pngtopnm $< > $@
