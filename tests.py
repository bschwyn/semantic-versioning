import unittest

from semantic_verification import *

class Test(unittest.TestCase):

    def test_cli(self):
        self.assertEqual(["hello", "world", "foo"], get_cli_input("hello     world   foo "))

        #should be false get_cli_input("   helo world  foo")

    def test_is_parse_to_semver(self):
        parse_string_to_semver("123.456.789")
        parse_string_to_semver("00.123.456")
        parse_string_to_semver("0.01")