"""\
The ``pyplay.py`` module supports the ``pyplay`` command line utility.
"""

__version__ = '0.6'

import os
import sys


class PyPlay():
    def __init__(self):
        self.config = Config()

        modules = self.config.modules
        for option in os.environ['_PYPLAY_ARGV'].split():
            if option == '--none':
                modules = []
            elif option.startswith('-'):
                module = option[1:]
                try:
                    modules.remove(module)
                except ValueError:
                    pass
            else:
                module = option
                modules.append(module)

        for module in reversed(modules):
            command = "import %s" % module
            self.config.commands.insert(0, command)

    def set_pythonpath(self):
        if self.config.ENV_CONFIG_DIR != '':
            for dir in (
                self.config.HOME_CONFIG_DIR,
                self.config.LOCAL_CONFIG_DIR,
                self.config.ENV_CONFIG_DIR,
            ):
                if dir is not None:
                    sys.path.insert(0, dir)

        for path in reversed(self.config.pythonpath):
            sys.path.insert(0, path)

    def init_readline(self):
        try:
            import readline
        except ImportError:
            print "Module readline not available."
        else:
            import rlcompleter
            readline.parse_and_bind("tab: complete")

    def init_readline_TODO(self):
        # Add auto-completion and a stored history file of commands to your Python
        # interactive interpreter. Requires Python 2.0+, readline. Autocomplete is
        # bound to the Esc key by default (you can change it - see readline docs).
        #
        # Store the file in ~/.pystartup, and set an environment variable to point
        # to it, e.g. "export PYTHONSTARTUP=/max/home/itamar/.pystartup" in bash.
        #
        # Note that PYTHONSTARTUP does *not* expand "~", so you have to put in the
        # full path to your home directory.

        import atexit
        import os
        import readline
        import rlcompleter

        historyPath = os.path.expanduser("~/.pyhistory")
        historyTmp = os.path.expanduser("~/.pyhisttmp.py")

        endMarkerStr= "# # # histDUMP # # #"

        saveMacro= "import readline; readline.write_history_file('"+historyTmp+"'); \
            print '####>>>>>>>>>>'; print ''.join(filter(lambda lineP: \
            not lineP.strip().endswith('"+endMarkerStr+"'),  \
            open('"+historyTmp+"').readlines())[:])+'####<<<<<<<<<<'"+endMarkerStr

        readline.parse_and_bind('tab: complete')
        readline.parse_and_bind('\C-w: "'+saveMacro+'"')

        def save_history(historyPath=historyPath, endMarkerStr=endMarkerStr):
            import readline
            readline.write_history_file(historyPath)
            # Now filter out those line containing the saveMacro
            lines= filter(lambda lineP, endMarkerStr=endMarkerStr:
              not lineP.strip().endswith(endMarkerStr), open(historyPath).readlines())
            open(historyPath, 'w+').write(''.join(lines))

        if os.path.exists(historyPath):
            readline.read_history_file(historyPath)

        atexit.register(save_history)

        del os, atexit, readline, rlcompleter, save_history, historyPath
        del historyTmp, endMarkerStr, saveMacro

    def help(self):
        version = __version__
        dir = self.config.ENV_CONFIG_DIR
        if dir is None:
            dir = 'None'
        config = (
            self.config.CONFIG_FILE or
            'None found. See PyPlay documentation.'
        )
        return """
Welcome to PyPlay version %(version)s.

PYPATH_CONFIG_DIR:  %(dir)s
Config file:        %(config)s
Commands:
    * h()           -- Help screen.
    * y(...)        -- Print a YAML dump of any object.
                       For example, try: y(__builtins__.__dict__)

Tips and Tricks:
    * Use the tab key to complete a word or see what options are
      available in any given context.
    * Use <ctl>-L to clear the screen.
""" % locals()


class Config():
    dir = os.path.expanduser('~/.pyplay')
    HOME_CONFIG_DIR = dir if os.path.exists(dir) else None

    dir = './pyplay'
    LOCAL_CONFIG_DIR = dir if os.path.exists(dir) else None

    dir = os.environ.get('PYPLAY_CONFIG_DIR', None)
    ENV_CONFIG_DIR = dir if (not dir or os.path.exists(dir)) else None

    dir = ENV_CONFIG_DIR or LOCAL_CONFIG_DIR or HOME_CONFIG_DIR
    file = dir + '/config.yaml'
    if ENV_CONFIG_DIR == '':
        CONFIG_FILE = None
    else:
        CONFIG_FILE = file if (dir and os.path.exists(file)) else None

    def __init__(self):
        self.readline = True
        self.commands = []
        self.pythonpath = [
            'lib',
        ]
        self.modules = [
            'os',
            'sys',
            're',
        ]

        if self.CONFIG_FILE:
            import yaml
            config = yaml.load(file(self.CONFIG_FILE, 'r'))
            self.__dict__.update(config)


if __name__ == '__main__':
    def h():
        print pyplay.help()

    def y(object):
        import yaml
        print yaml.dump(
            object,
            default_flow_style=False,
            explicit_start=True
        ),

    pyplay = PyPlay()

    pyplay.set_pythonpath()

    print '*** Welcome to PyPlay version %s -- Type h() for help.' % (
        __version__,)

    if pyplay.config.CONFIG_FILE:
        print "*** PyPlay config file: '%s'" % pyplay.config.CONFIG_FILE

    if pyplay.config.readline:
        print '*** PyPlay tab completion enabled'
        pyplay.init_readline()

    for command in pyplay.config.commands:
        print '>>> %s' % command
        exec command

    del command
