import unittest

#  subclassing unittest.Testcase creates a test case
class TestStringMethods(unittest.TestCase):

    # test informs the test runner about which methods represents tests
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        #  check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    #  Provides a command-line interface to the test script
    unittest.main()