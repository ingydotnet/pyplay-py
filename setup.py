#!/usr/bin/env python
# coding=utf-8

import os
import sys
sys.path.insert(0, 'lib')
sys.path.insert(0, '.')
import codecs

from distutils.core import setup, Command

import pyplay


class Test(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        build_cmd = self.get_finalized_command('build')
        build_cmd.run()
        sys.path.insert(0, build_cmd.build_lib)
        sys.path.insert(0, 'tests')
        import test_compiled
        test_compiled.main()


if __name__ == '__main__':
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

        cmdclass={'test': Test},
    )

