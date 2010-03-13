"""\
Sandbox module.
"""

def options():
    import os

    options = {
        'readline': True,
        'readline2': False,
        'os': True,
        'sys': True,
        're': True,
        'yaml': True,
    }

    for option in os.environ['SANDBOX_ARGV'].split():
        if len(option) <= 2 or option[0:2] != '--':
            continue
        option = option[2:]
        value = True
        if len(option) > 3 and option[0:3] == 'no-':
            option = option[3:]
            value = False
        if option == 'all':
            for key in options:
                options[key] = True
        elif option == 'none':
            for key in options:
                options[key] = False
        else:
            options[option] = value
        if options['readline2']:
            options['readline'] = False

    return options
