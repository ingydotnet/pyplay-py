About
-----

``pyplay`` is a command line tool that invokes the interactive Python
shell, but starts it up with tab completion turned on, common paths
added to ``sys.path``, common modules preloaded and optionally some
startup python commands run.

It is configurable, both at a system-wide level and a per project
(directory) level.

Installation
------------

Install from sources::

    sudo python setup.py install

Usage
-----

To start a ``pyplay`` shell, just enter a command like this::

    pyplay                  # Start Python and handy modules
    pyplay --none           # No extras
    pyplay -re yaml         # All except re, then add yaml
    pyplay --none yaml      # Nothing except yaml
    pyplay xyz test_foo     # import xyz and test_foo

Configuration
-------------

If you use ``pyplay`` a lot and always want to preload the same modules,
you can set up your own custom configuration in a file called
``~/.pyplay/config.yaml`` or ``./pyplay/config.yaml`` like this::

    # Is readline & tab completion on?
    readline: true
    
    # Added to the front of sys.path.
    pythonpath:
    - .
    - lib
    - tests
    
    # Modules to import by default.
    modules:
    - os
    - sys
    - yaml

    # Commands to run by default
    - from yaml import *

If you explicitly supply the ``PYPLAY_CONFIG_DIR`` environment variable,
that directory will be used to find the ``config.yaml`` file. If you set
``PYPLAY_CONFIG_DIR`` to an empty string, no config file will be read,
even if the one of them exists.

Also, ``PYPLAY_CONFIG_DIR``, ``~/.pyplay/`` and ``./pyplay/`` will be
added to the front of ``sys.path`` if they exist, so you can put modules
that you want to play with in those directories.

Command Line Options
--------------------

``--none``
    Clear the list of modules to import

``module``
    Add a module to the import list

``-module``
    Remove a module from the import list

Sample Run
----------

Here is what a session looks like on startup::

    $ pyplay foo bar
    Python 2.6.2 (r262:71600, Apr 16 2009, 09:17:39) 
    [GCC 4.0.1 (Apple Computer, Inc. build 5250)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    *** Welcome to PyPlay version 0.3 -- Type h() for help.
    *** PyPlay tab completion enabled
    >>> import os
    >>> import sys
    >>> import re
    >>> import foo
    >>> import bar
    >>> 

PyPlay Commands
---------------

Pyplay adds some extra shell commands. The current commands are:

h()
    Show the PyPlay help screen.

y(object)
    Print a YAML dump of any object. (Requires the ``yaml`` module)

From the Author
---------------

The interactive Python shell is a great tool for learning Python,
because Python has such great introspection. The only things that bugged
me about it are 1) I am always needing to set it up a certain way every
time I use it, B) and that it doesn't have tab completion on by default.
``pyplay`` takes care of these issues nicely.

``pyplay`` is my first (but definitely not last) Python module. I hope
you find it useful. Please email me if you have any problems or
suggestions.

Kind regards, Ingy dot Net

To Do
-----

In a future release, you might see:

* Logging of shell commands
* Save readline history between sessions
* More PyPlay special commands
