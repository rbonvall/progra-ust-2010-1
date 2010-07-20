#!/usr/bin/python

import sys

programs = open(sys.argv[1]).read().split('\n\n')
for i, p in enumerate(programs):
    if p.strip():
        open('p{0}.py'.format(i + 1), 'w').write(p)


