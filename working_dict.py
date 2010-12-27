#!/usr/bin/python -tt

import sys
import os
from collections import defaultdict

m = defaultdict(list)

f = open('utfil', 'rU')

for lines in f:
    fields = [(lines.split()[1], lines.split()[2])]
    for k, v in fields:
        m[k].append(v)

