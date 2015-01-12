"""
Clean up the mess that Mendeley leaves behind when it exports to BibTeX
"""

import bibtexparser
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import homogeneize_latex_encoding
import sys

parser = BibTexParser()
parser.customization = homogeneize_latex_encoding

bib = bibtexparser.load(sys.stdin, parser=parser)

## loop over entries, removing dupes
entries_nodupes = []
ids = set()
for entry in bib.entries:
    if entry['id'] not in ids:
        ids.add(entry['id'])
        entries_nodupes.append(entry)
bib.entries = entries_nodupes

## write output to stdout
bib_string = bibtexparser.dumps(bib)
sys.stdout.write(bib_string.encode('utf-8'))
