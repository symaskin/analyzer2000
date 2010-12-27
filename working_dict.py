#!/usr/bin/python -tt

import sys
import os
from collections import defaultdict

#nicksAndurls = defaultdict(lambda: defaultdict(list))
d = defaultdict(list)

f = open('utfil', 'rU')

for lines in f:
    fields = [(lines.split()[1], {'file':lines.split()[3], 'url':lines.split()[2], 'date':lines.split()[0]})]
    for k, v in fields:
        d[k.lower()].append(v)

print type(d)
