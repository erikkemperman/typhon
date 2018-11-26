#!/usr/bin/env python3
# -*- coding: utf-8 -*-

project_meta = {
    'name': 'typhon',
    'version': '0.0.1-omega',
    'url': 'https://github.com/erikkemperman/typhon/',
    'description': 'concurrent / distributed computing framework for typhon',
    'keywords': ['concurrent', 'distributed', 'computing', 'typhon'],
    'copyright': '2018 typhon authors & contributors',
    'license': 'MIT',
    'author': 'Erik Kemperman',
    'author_email': 'erikkemperman@gmail.com',
    'packages': ['typhon'],
    'package_dir': {'': 'src'}
}

if __name__ == '__main__':
    from distutils.core import setup
    #setup(**project_meta)
    setup()
