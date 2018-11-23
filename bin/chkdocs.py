#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re

if __name__ == '__main__':
    import os
    import pickle
    import sys

    base_dir = os.path.join(os.path.dirname(sys.argv[0]), '..')

    print(sys.version_info)
    with open(os.path.join(base_dir, 'doc/coverage/undoc.pickle'), 'rb') as f:
        undoc = pickle.load(f)
        ok = True
        for package in undoc:
            for mod in sorted(package.keys()):
                for what, which in package[mod].items():
                    if len(which) == 0:
                        continue
                    what = re.sub('e?s$', '', what)
                    which = ', '.join(['"%s"' % w for w in which])
                    print('Module %s: no docs for %s %s' % (mod, what, which))
                    ok = False
    exit(0 if ok else 1)

