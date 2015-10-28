import unittest

class RashodiImportingTestCases(unittest.TestCase):

    def setUp(self):
        pass

    def test_upper_case(self):
      self.assertEqual('foo'.upper(), 'FOO')

class PrihodiImportingTestCases(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()