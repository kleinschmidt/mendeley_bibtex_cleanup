# Make sure there's a trailing slash here:
LIBRARYDIR = /Users/dkleinschmidt/Documents/papers/

.PHONY: install
install:
	cp clean-library-auto.sh clean_library.py $(LIBRARYDIR)
	sed s:{{LIBRARYDIR}}:$(LIBRARYDIR): < clean-library-auto.plist.template > clean-library-auto.plist
	launchctl load ./clean-library-auto.plist
