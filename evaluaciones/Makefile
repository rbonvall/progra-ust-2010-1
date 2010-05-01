TEXFILES = $(wildcard *.tex)
TARGETS = $(addsuffix .pdf, $(basename $(TEXFILES)))

all: $(TARGETS)
%.pdf: %.tex
	pdflatex $<
clean:
	rm -f *.aux *.log
distclean: clean
	rm -f $(TARGETS)

.PHONY: clean all
