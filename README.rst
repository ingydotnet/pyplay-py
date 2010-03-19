About
-----

``pyplay`` is a command line tool for invoking the interactive Python
shell, but with tab completion turned on and some modules preloaded.

Installation
------------

Install from sources::

    sudo python setup.py install

Usage
-----

To start a ``pyplay`` shell, just enter a command like this::

    pyplay                  # Start Python and handy modules
    pyplay --none           # Start up with no extras
    pyplay -yaml            # Start up with all except yaml
    pyplay --none yaml      # Start up with nothing except yaml
    pyplay xyz test_foo     # Start up then import xyz and test_foo

If you use ``pyplay`` a lot and always want to preload the same modules,
you can set up your own custom configuration in a file called
``~/.pyplay/config.yaml`` like this::

    # Is readline & tab completion on?
    readline: true
    
    # Places to find modules.
    pythonpath:
    - .
    - lib
    - tests
    
    # Modules to import by default.
    import:
    - os
    - sys
    - re
    - yaml
