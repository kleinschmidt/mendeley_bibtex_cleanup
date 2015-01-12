#!/bin/bash

library_dir=/Users/dkleinschmidt/Documents/papers
cd ${library_dir}
./clean_library.py < library.bib > library_clean.bib 2> /dev/null

/usr/bin/logger library.bib modified and clean_library.py run
