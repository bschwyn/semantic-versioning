import unittest

from semver_check import *

class Test(unittest.TestCase):

    def testtest(self):
        self.assertEqual(5,5)

    def test_cli(self):
        self.assertEqual(["hello", "world", "foo"], get_cli_input("hello     world   foo "))

        #should be false get_cli_input("   helo world  foo")

    def test_is_valid_input(self):
        t1 = "1.3.6 1.4.2"
        t2 = "1.7.9 1.3.5 0.0.2"
        t3 = "4.2.3-beta 4.2.3-alpha"
        t4 = "1.6 1.6.3"
        print("tests pass if true")
        print(True == is_input_valid(t1))
        print(False == is_input_valid(t2))
        print(True == is_input_valid(t3))
        print(False == is_input_valid(t4))

if __name__ == '__main__':
    unittest.main()