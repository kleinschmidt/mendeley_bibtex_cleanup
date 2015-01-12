# Make sure there's a trailing slash here:
LIBRARYDIR = /Users/dkleinschmidt/Documents/papers/

clean-library-auto.%: clean-library-auto.%.template
	sed s:{{LIBRARYDIR}}:$(LIBRARYDIR): < $< > $@

.PHONY: install
install: clean-library-auto.plist clean-library-auto.sh
	cp clean-library-auto.sh clean_library.py $(LIBRARYDIR)
	launchctl load ./clean-library-auto.plist
