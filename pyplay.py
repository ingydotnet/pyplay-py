"""\
The ``pyplay.py`` module supports the ``pyplay`` command line utility.
"""

__version__ = '0.2'

import os
import sys

class PyPlay():
    config = {
        'pythonpath': [
            '.',
            'lib',
        ],
        'import': [
            'os',
            'sys',
            're',
        ],
        'commands': [],
        'readline': True,
    }

    def __init__(self):
        config_path = './pyplay/config.yaml'
        if not os.path.exists(config_path):
            config_path = os.path.expanduser('~/.pyplay/config.yaml')
            if not os.path.exists(config_path):
                config_path = ''

        if config_path:
            import yaml
            config = yaml.load(file(config_path, 'r'))
            if 'import' in config:
                self.config['import'] = config['import']
            if 'pythonpath' in config:
                self.config['pythonpath'] = config['pythonpath']
            if 'readline' in config:
                self.config['readline'] = config['readline']
            if 'commands' in config:
                self.config['commands'] = config['commands']

        path = os.path.expanduser('~/.pyplay')
        if os.path.exists(path):
            sys.path.insert(0, path)
        path = './pyplay'
        if os.path.exists(path):
            sys.path.insert(0, path)

        for path in self.config['pythonpath'].__reversed__():
            sys.path.insert(0, path)
    
    def parse_options(self):
        self.modules = self.config['import']
        for option in os.environ['PYTHON_SANDBOX_ARGV'].split():
            if option == '--none':
                self.modules = []
            elif len(option) > 1 and option[0:1] == '-':
                module = option[1:]
                try:
                    self.modules.remove(module)
                except ValueError:
                    pass
            else:
                module = option
                self.modules.append(module)

        for module in self.modules.__reversed__():
            command = "import %s" % module
            self.config['commands'].insert(0, command)

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

if __name__ == '__main__':
    pyplay = PyPlay()

    pyplay.parse_options()

    if pyplay.config['readline']:
        print '*** Tab completion enabled'
        pyplay.init_readline()

    for command in pyplay.config['commands']:
        print '>>> %s' % command
        exec command

