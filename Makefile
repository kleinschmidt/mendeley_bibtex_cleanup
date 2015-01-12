INSTALLDIR = /Users/dkleinschmidt/Documents/papers/

.PHONY: install
install:
	cp clean-library-auto.sh clean_library.py $(INSTALLDIR)
	launchctl load ./clean-library-auto.plist
