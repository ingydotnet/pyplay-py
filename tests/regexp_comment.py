import re

class Test():
    string = """\
# one
# two
# three

# four
# five

...
"""

    regexp = r'(?:# (.*)\n)+'

    def test():
        assert re.match(regexp, string).groups().join('') == "onetwothree"
