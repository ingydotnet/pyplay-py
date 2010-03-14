"""\
python.playground module.
"""

import os

class Playground():
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
        config_path = os.path.expanduser('~/.python-playground/config.yaml')
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
            if len(option) > 2 and option[0:2] == '--':
                option = option[2:]
            if len(option) > 3 and option[0:3] == 'no-':
                module = option[3:]
                self.modules.remove(module)
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

if __name__ == '__main__':
    import playground
    pg = playground.Playground()

    import sys
    sys.path.extend(pg.config['pythonpath'])

    for command in pg.commands():
        print '>>> %s' % command
        exec command

    if pg.config['readline']:
        pg.init_readline()

