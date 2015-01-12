"""
Clean up the mess that Mendeley leaves behind when it exports to BibTeX
"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
import sys

filename = "library.bib"
with open(filename) as bib_file:
    parser = BibTexParser()
    parser.customization = homogeneize_latex_encoding
    bib = bibtexparser.load(bib_file, parser=parser)

## loop over entries, removing dupes
entries_nodupes = []
ids = set()
for entry in bib.entries:
    if entry['id'] not in ids:
        ids.add(entry['id'])
        entries_nodupes.append(entry)
bib.entries = entries_nodupes

bib_string = bibtexparser.dumps(bib)

output_filename = "library_out.bib"
with open(output_filename, "w") as bib_output_file:
    bib_output_file.write(bib_string.encode('utf-8'))