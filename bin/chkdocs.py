#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    import os
    import pickle

    base_dir = os.path.join(os.path.dirname(__file__), '..')

    ok = True
    with open(os.path.join(base_dir, 'doc/coverage/undoc.pickle'), 'rb') as f:
        for package in pickle.load(f):
            for mod in sorted(package.keys()):
                for what, which in package[mod].items():
                    if len(which) == 0:
                        continue
                    what = re.sub('e?s$', '', what)
                    which = ', '.join(['"%s"' % w for w in which])
                    print('In "%s": no docs for %s %s' % (mod, what, which))
                    ok = False
    exit(0 if ok else 1)

