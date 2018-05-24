# Fetch and update word occurences from index in a single line
# save as index.py
"""Build an index mapping word -> list of occurences"""

import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

# print in alphabetical order
for word in sorted(index, key=str.upper):
    print(word, index[word])
