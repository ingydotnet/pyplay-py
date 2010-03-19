#!/usr/bin/env python

import sys
sys.path.insert(0, 'lib')

from distutils.core import setup

import playground

setup(
    name='playground',
    version=playground.__version__,
    description='Python Interactive Playground',
    author='Ingy dot Net',
    author_email='ingy@ingy.net',
    url='http://github.com/ingydotnet/',
    package_dir = {'': 'lib'},
    py_modules=['playground'],
    scripts=['python-playground'],
    license='bsd',
)
