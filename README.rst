About
-----

``pyplay`` is a command line tool that invokes the interactive Python
shell, but it starts up with tab completion turned on, some common
modules preloaded and optionally some startup python commands run.

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
    import:
    - os
    - sys
    - yaml

    # Commands to run by default
    - from yaml import *

Also, ``~/.pyplay/`` and ``./pyplay/`` will be added to the front of
``sys.path`` if they exist, so you can put modules there, that you want
to play with.

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
* pyplay special commands
* A plugin facility

