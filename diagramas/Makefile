TEXFILES = $(shell ls *.tex | grep -v ^flujo\.tex)
PDFFILES = $(addsuffix .pdf, $(basename $(TEXFILES)))

all: $(PDFFILES)

%.pdf: %.tex
	@echo "Building $@"
	#@pdflatex $< -halt-on-error -interaction=nonstopmode &> .my_log || (cat .my_log && rm .my_log && exit 1)
	#@rm .my_log
	@pdflatex $<

%.svg: %.pdf
	pdf2svg $< $@
%.png: %.svg
	inkscape $< --export-png=$@

clean:
	rm -f \
            $(wildcard *.aux) \
	    $(wildcard *.log) \
	    $(wildcard *.pdf) \
	    $(wildcard *.nav) \
	    $(wildcard *.toc) \
	    $(wildcard *.snm) \
	    $(wildcard *.vrb) \
	    $(wildcard *.out) \
	    $(wildcard *.svg) \
	    $(wildcard *.png)

.PHONY: clean all
