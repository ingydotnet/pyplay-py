"""\
The ``pyplay.py`` module supports the ``pyplay.py`` command line utility.
"""

__version__ = '0.1'

import os

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
        'readline': True,
    }

    def __init__(self):
        config_path = os.path.expanduser('~/.pyplay/config.yaml')
        if os.path.exists(config_path):
            import yaml
            config = yaml.load(file(config_path, 'r'))
            if 'import' in config:
                self.config['import'] = config['import']
            if 'pythonpath' in config:
                self.config['pythonpath'] = config['pythonpath']
            if 'readline' in config:
                self.config['readline'] = config['readline']
    
    def commands(self):
        self.parse_options()
        list = []
        for module in self.modules:
            command = "import %s" % module
            list.append(command)
        return list

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
    pg = PyPlay()

    import sys
    sys.path.extend(pg.config['pythonpath'])

    for command in pg.commands():
        print '>>> %s' % command
        exec command

    if pg.config['readline']:
        pg.init_readline()

