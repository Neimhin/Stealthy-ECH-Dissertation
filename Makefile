FIGURES :=  figure/ech-reject-and-hrr.pdf figure/ech-accept-and-hrr.pdf figure/ServerHello-struct.pdf figure/sech-split-mode-accept.pdf
figures: $(FIGURES)
clean:
	rm $(FIGURES)
figure/ServerHello-struct.pdf: figure/ServerHello-struct.txt
	enscript --line-numbers --color --highlight=c --output=- --no-header --media=A3 $< | ps2pdf - - | pdfcrop - $@
figure/sech-split-mode-accept.pdf: figure/sech-split-mode-accept.puml
	plantuml -tpdf $<
figure/ech-accept-and-hrr.pdf: figure/ech-accept-and-hrr.puml
	plantuml -tpdf $<
figure/ech-reject-and-hrr.pdf: figure/ech-reject-and-hrr.puml
	plantuml -tpdf $<
