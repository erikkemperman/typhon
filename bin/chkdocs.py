#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import os
    import pickle
    import sys

    base_dir = os.path.join(os.path.dirname(sys.argv[0]), '..')

    with open(os.path.join(base_dir, 'doc/coverage/undoc.pickle'), 'rb') as f:
        undoc = pickle.load(f)
        # TODO check that all members are empty
