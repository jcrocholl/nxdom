.SECONDARY :

all : negative.png neutral.png interesting.png important.png critical.png

important.png : important.orig.png
	pngtopnm $< | pnmcrop | pnmpad -white -width 14 -halign 0 -bottom 4 | pnmtopng > $@

interesting.png : interesting.orig.png
	pngtopnm $< | pnmcrop | pnmpad -white -width 14 -halign 0 -bottom 4 | pnmtopng > $@

%.png : %.orig.png
	pngtopnm $< | pnmcrop | pnmpad -white -width 14 -halign 0 -bottom 3 | pnmtopng > $@
