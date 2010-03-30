import unittest

class TestImport(unittest.TestCase):
    def test_compiled(self):
        import pyplay
        self.assertTrue(pyplay, "pyplay was loaded successfully")

if __name__ == '__main__':
    unittest.main()
