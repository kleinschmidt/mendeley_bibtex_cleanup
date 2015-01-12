# Make sure there's a trailing slash here:
LIBRARYDIR = /Users/dkleinschmidt/Documents/papers/

clean-library-auto.%: templates/clean-library-auto.%
	sed s:{{LIBRARYDIR}}:$(LIBRARYDIR): < $< > $@
	chmod +x $@

.PHONY: install all

all: clean-library-auto.plist clean-library-auto.sh

install: all
	cp clean-library-auto.sh clean_library.py $(LIBRARYDIR)
	launchctl load ./clean-library-auto.plist
