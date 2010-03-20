#!/usr/bin/env python
# coding=utf-8

import os
import sys
sys.path.insert(0, 'lib')
import codecs

from distutils.core import setup

import pyplay

setup(
    name='pyplay',
    version=pyplay.__version__,

    description='Python Interactive Playground',
    long_description = codecs.open(
        os.path.join(
            os.path.dirname(__file__),
            'README.rst'
        ),
        'r',
        'utf-8'
    ).read(),

    # See: http://pypi.python.org/pypi?:action=list_classifiers
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Education',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Shells',
        'Topic :: Utilities',
    ],

    author='Ingy dot Net',
    author_email='ingy@ingy.net',
    license='Simplified BSD License',
    url='http://github.com/ingydotnet/pyplay-py/',

    py_modules=['pyplay'],
    scripts=['bin/pyplay'],
)
