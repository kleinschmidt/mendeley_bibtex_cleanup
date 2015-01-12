# Mendeley makes a mess of BibTeX

Mendeley will automatically generate a BibTeX file from your library but it kind of sucks sometimes:

1. There's no way to include/exclude particular fields from the BibTeX export.  This is a problem because [some packages](http://www.ctan.org/pkg/apacite) look for the presence of particular information (like a `month` field) to determine whether an `@article` is from an academic journal or magazine.  You could fix this manually by going through and deleting the `month` entry for every single item in your library, but why.

2. If you've ever shared something in your library with a group, it gets a duplicate entry in the BibTeX file.  This makes BibTeX exit with an error even though it runs perfectly fine, screwing up any kind of automatic build system you might have set up.

## Cleaning it up

The work is done by `clean_library.py`, a python script that, in the dumbest possible way, removes the fields I don't want and duplicate entries.

# Making it work for you

## Quick and dirty

    ./clean_library.py < /path/to/library.bib > /path/to/output.bib 2> /dev/null

## Automagic

Included with this is also a `launchctl` job that will watch the `library.bib` file, and run the script on it when it changes, writing `library-clean.bib`.

There's a convenient Makefile to automate this process.  To configure it, change the `LIBRARYDIR = ` line in the Makefile to your own Mendeley library directory (or wherever it exports `library.bib`).  Then run `make install` and profit.  Actually, change something in the Mendeley metadata, then check in `Console.app` that it actually updated (you should see a log message).

# Thanks

* Watching plist from [stackoverflow](http://stackoverflow.com/questions/1515730/is-there-a-command-like-watch-or-inotifywait-on-the-mac)
