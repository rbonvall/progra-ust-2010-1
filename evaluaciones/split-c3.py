#!/usr/bin/python
programs = open('programas-c3.py').read().split('\n\n')
for i, p in enumerate(programs):
    if p.strip():
        open('c3-p{0}.py'.format(i + 1), 'w').write(p)


