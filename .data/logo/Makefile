logotitle.png : logo.ppm space.ppm title.ppm
	pnmcat -lr $^ | pnmtopng -transparent white > $@

space.ppm :
	ppmmake white 12 45 > $@

square.png : logo45.ppm
	pnmpad -white -height 86 -valign 0.5 $< | pnmtopng > $@

logo%.png : logo%.ppm
	pnmtopng -transparent white $< > $@
	cp $@ /Users/johann/Desktop/

logo.ppm : big.ppm
	pnmscale -height 45 $< > $@

logo120x60.ppm : big.ppm
	pnmscale -width 115 -height 60 $< | pnmpad -white -width 120 -height 60 -halign 0 -valign 1 > $@

favicon.png : 16x16.ppm
	pnmtopng -transparent "#AAAAAA" $< > $@

16x16.ppm : 16x4.ppm 16.ppm 16x3.ppm
	pnmcat -tb $^ > $@

16x%.ppm :
	ppmmake "#AAAAAA" 16 $* > $@

16.ppm : 17.ppm
	pamcut -width 16 $< > $@

17.ppm : gray.ppm
	pnmscale -width 17 $< | pnmquant 16 > $@

gray.ppm : big.ppm
	ppmchange "#FFFFFF" "#AAAAAA" $< > $@

square.ppm : big.ppm
	pnmpad -white -height 962 -valign 0.5 $< > $@

%.ppm : %.png
	pngtopnm -mix -background white $< > $@
