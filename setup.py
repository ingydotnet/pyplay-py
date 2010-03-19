#!/usr/bin/env python

import sys
sys.path.insert(0, 'lib')

from distutils.core import setup

import pyplay

setup(
    name='pyplay',
    version=pyplay.__version__,
    description='Python Interactive Playground',
    author='Ingy dot Net',
    author_email='ingy@ingy.net',
    url='http://github.com/ingydotnet/pyplay-py/',
    py_modules=['pyplay'],
    scripts=['bin/pyplay'],
    license='bsd',
)
