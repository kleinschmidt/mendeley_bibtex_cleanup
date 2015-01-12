#! /usr/bin/env python2.7

"""
Clean up the mess that Mendeley leaves behind when it exports to BibTeX:

* Delete entries with duplicate citekeys (keep the first one encountered)
* Remove url and month fields (because apacite tries to include them and
  it's not necessary/is ugly)

Dave Kleinschmidt, 2015
"""

import sys
import re

include_this_entry = True
ids_seen = set()

start_entry_re = re.compile('@\w+{(?P<id>\w+),')
exclude_line_re = re.compile('^(month|url)')

print "Cleaned! Just like that!\n"

for line in sys.stdin:
    m = start_entry_re.match(line)
    if m:
        ## start of new entry. check for dupe
        if m.group('id') in ids_seen:
            include_this_entry = False
            sys.stderr.write('Duplicate ID: ' + m.group('id') + '\n')
        else:
            include_this_entry = True
            ids_seen.add(m.group('id'))
    if include_this_entry:
        if not exclude_line_re.match(line):
            sys.stdout.write(line)
