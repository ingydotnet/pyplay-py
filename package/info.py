def get():
    dict = {}
    dict.update(
{ 'author': 'Ingy dot Net',
  'author_email': 'ingy@ingy.net',
  'classifiers': [ 'Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: POSIX',
                   'Programming Language :: Python',
                   'Topic :: Education',
                   'Topic :: Software Development :: Testing',
                   'Topic :: System :: Shells',
                   'Topic :: Utilities'],
  'description': 'Python Interactive Playground',
  'license': 'Simplified BSD License',
  'long_description': 'About\n-----\n\n``pyplay`` is a command line tool that invokes the interactive Python\nshell, but starts it up with tab completion turned on, common paths\nadded to ``sys.path``, common modules preloaded and optionally some\nstartup python commands run.\n\nIt is configurable, both at a system-wide level and a per project\n(directory) level.\n\nInstallation\n------------\n\nInstall from sources::\n\n    sudo python setup.py install\n\nUsage\n-----\n\nTo start a ``pyplay`` shell, just enter a command like this::\n\n    pyplay                  # Start Python and handy modules\n    pyplay --none           # No extras\n    pyplay -re yaml         # All except re, then add yaml\n    pyplay --none yaml      # Nothing except yaml\n    pyplay xyz test_foo     # import xyz and test_foo\n\nConfiguration\n-------------\n\nIf you use ``pyplay`` a lot and always want to preload the same modules,\nyou can set up your own custom configuration in a file called\n``~/.pyplay/config.yaml`` or ``./pyplay/config.yaml`` like this::\n\n    # Is readline & tab completion on?\n    readline: true\n    \n    # Added to the front of sys.path.\n    pythonpath:\n    - .\n    - lib\n    - tests\n    \n    # Modules to import by default.\n    modules:\n    - os\n    - sys\n    - yaml\n\n    # Commands to run by default\n    - from yaml import *\n\nIf you explicitly supply the ``PYPLAY_CONFIG_DIR`` environment variable,\nthat directory will be used to find the ``config.yaml`` file. If you set\n``PYPLAY_CONFIG_DIR`` to an empty string, no config file will be read,\neven if the one of them exists.\n\nAlso, ``PYPLAY_CONFIG_DIR``, ``~/.pyplay/`` and ``./pyplay/`` will be\nadded to the front of ``sys.path`` if they exist, so you can put modules\nthat you want to play with in those directories.\n\nCommand Line Options\n--------------------\n\n``--none``\n    Clear the list of modules to import\n\n``module``\n    Add a module to the import list\n\n``-module``\n    Remove a module from the import list\n\nSample Run\n----------\n\nHere is what a session looks like on startup::\n\n    $ pyplay foo bar\n    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) \n    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin\n    Type "help", "copyright", "credits" or "license" for more information.\n    *** Welcome to PyPlay version 0.3 -- Type h() for help.\n    *** PyPlay tab completion enabled\n    >>> import os\n    >>> import sys\n    >>> import re\n    >>> import foo\n    >>> import bar\n    >>> \n\nPyPlay Commands\n---------------\n\nPyplay adds some extra shell commands. The current commands are:\n\nh()\n    Show the PyPlay help screen.\n\ny(object)\n    Print a YAML dump of any object. (Requires the ``yaml`` module)\n\nFrom the Author\n---------------\n\nThe interactive Python shell is a great tool for learning Python,\nbecause Python has such great introspection. The only things that bugged\nme about it are 1) I am always needing to set it up a certain way every\ntime I use it, B) and that it doesn\'t have tab completion on by default.\n``pyplay`` takes care of these issues nicely.\n\n``pyplay`` is my first (but definitely not last) Python module. I hope\nyou find it useful. Please email me if you have any problems or\nsuggestions.\n\nKind regards, Ingy dot Net\n\nTo Do\n-----\n\nIn a future release, you might see:\n\n* Logging of shell commands\n* Save readline history between sessions\n* More PyPlay special commands\n',
  'name': 'pyplay',
  'py_modules': ['pyplay'],
  'scripts': ['bin/pyplay'],
  'url': 'http://github.com/ingydotnet/pyplay-py/',
  'version': '1.0.3'}
)
    return dict
