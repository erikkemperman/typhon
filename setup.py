#!/usr/bin/env python3

from distutils.core import setup

setup(
    name='typhon',
    version='0.0.1-omega',
    url='https://github.com/erikkemperman/typhon/',
    description='concurrent / distributed computing framework for python',
    keywords=['concurrent', 'distributed', 'computing', 'python'],
    license='MIT',
    author='Erik Kemperman',
    author_email='erikkemperman@gmail.com',
    packages=['typhon'],
    package_dir={'': 'src'}
)
