DOCUMENTS = $(basename $(wildcard *.tex))
PDFS = $(addsuffix .pdf, $(DOCUMENTS))
DVIS = $(addsuffix .dvi, $(DOCUMENTS))
PSS  = $(addsuffix .ps,  $(DOCUMENTS))

RED = $(shell tput setaf 1)$(1)$(shell tput sgr0)
GREEN = $(shell tput setaf 2)$(1)$(shell tput sgr0)
YELLOW = $(shell tput setaf 3)$(1)$(shell tput sgr0)

ON_SUCCESS = (rm $(1); echo "$(call GREEN,done)")
ON_ERROR = (echo "$(call RED,error)"; sed -n '/^!/,$$p' $(1); rm $(1); exit 1)

TEXFLAGS = -halt-on-error -interaction nonstopmode
define BUILD_WITH
    T=$$(mktemp); \
    $(1) $(TEXFLAGS) $< > $$T 2>&1 /dev/null && \
        $(call ON_SUCCESS,$$T) || \
	$(call ON_ERROR,$$T)
endef
define BUILD_MSG
    echo -n "$< → $@... "
endef

all: pdfs
pdfs: $(PDFS)
dvis: $(DVIS)
pss: $(PSS)

%.pdf: %.tex
	@$(BUILD_MSG)
	@$(call BUILD_WITH,pdflatex)
%.dvi: %.tex
	@$(BUILD_MSG)
	@$(call BUILD_WITH,latex)
%.ps: %.dvi
	@$(BUILD_MSG)
	@dvips $< &> /dev/null
	@echo done
clean:
	@echo Deleting auxiliary files.
	@rm -f *.aux *.log
distclean: clean
	@echo Deleting output files.
	@rm -f $(PDFS) $(DVIS) $(PSS)

.PHONY: all pdfs dvis pss clean distclean

