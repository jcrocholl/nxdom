logo.png : logo.ppm
	pnmtopng -transparent "#FFFFFF" $< > $@

logo.ppm : big.ppm
	pnmscale -width 111 $< > $@

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
	pngtopnm $< > $@
