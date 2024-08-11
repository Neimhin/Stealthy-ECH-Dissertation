FIGURES :=  figure/ech-reject-and-hrr.pdf figure/ech-accept-and-hrr.pdf figure/ServerHello-struct.pdf figure/sech-split-mode-accept.pdf figure/pre_shared_key.pdf figure/sech2-cover.pdf figure/sech2-accept-function.pdf figure/sech2-transcript-hash.pdf figure/sech2-derive-secret.pdf figure/sech5-cover.pdf figure/birthday-paradox.pdf
figures: $(FIGURES)
clean:
	-rm $(FIGURES)
	-rm tmp/*

figure/birthday-paradox.pdf: figure/birthday-paradox.py
	python ./figure/birthday-paradox.py $@
figure/sech5-cover.pdf: figure/sech5-cover.tex lib.tex
	cd figure && pdflatex --output-directory ../tmp sech5-cover.tex && cp ../tmp/sech5-cover.pdf ./sech5-cover.pdf && rm ../tmp/sech5-cover.*

figure/sech2-cover.pdf: figure/sech2-cover.tex lib.tex
	cd figure && pdflatex --output-directory ../tmp sech2-cover.tex && cp ../tmp/sech2-cover.pdf ./sech2-cover.pdf && rm ../tmp/sech2-cover.*
figure/sech2-derive-secret.pdf: figure/sech2-derive-secret.c
	enscript --color --highlight=c --output=- --no-header --media=A3 $< | ps2pdf - - | pdfcrop - $@
figure/sech2-transcript-hash.pdf: figure/sech2-transcript-hash.c
	enscript --color --highlight=c --output=- --no-header --media=A3 $< | ps2pdf - - | pdfcrop - $@
figure/sech2-accept-function.pdf: figure/sech2-accept-function.c
	enscript --color --highlight=c --output=- --no-header --media=A3 $< | ps2pdf - - | pdfcrop - $@

figure/pre_shared_key.pdf: figure/pre_shared_key.c
	enscript --line-numbers --color --highlight=c --output=- --no-header --media=A3 $< | ps2pdf - - | pdfcrop - $@
figure/ServerHello-struct.pdf: figure/ServerHello-struct.txt
	enscript --line-numbers --color --highlight=c --output=- --no-header --media=A3 $< | ps2pdf - - | pdfcrop - $@
figure/sech-split-mode-accept.pdf: figure/sech-split-mode-accept.puml
	plantuml -tpdf $<
figure/ech-accept-and-hrr.pdf: figure/ech-accept-and-hrr.puml
	plantuml -tpdf $<
figure/ech-reject-and-hrr.pdf: figure/ech-reject-and-hrr.puml
	plantuml -tpdf $<
