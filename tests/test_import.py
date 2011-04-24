from package.unittest import *

class TestImport(TestCase):
    def test_compiled(self):
        import pyplay
        self.assertTrue(pyplay, "pyplay was loaded successfully")

if __name__ == '__main__':
    main()
