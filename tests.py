#import unittest
from unittest.mock import patch, call
import io
#import unittest.mock

from semver_check import *


def incr(x):
    return x + 1

def test_answer():
    assert(incr(3) == 5)

class Test():#unittest.TestCase):

    def testtest(self):
        self.assertEqual(5,5)

    def test_main(self):
        self.assertIsNone(main)

    def test_cli(self):
        self.assertEqual(["hello", "world", "foo"], get_cli_input("hello     world   foo "))
        self.assertEqual("", get_cli_input(("")))
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


    def test_main_cli(capsys):

        args = ["semver_check.py", "1.3.6", "1.4.2"]
        main_cli(args)
        captured = capsys.readouterr()
        assert captured.out == "before\n"

        args = ["semver_check.py", "1.3.5", "1.3.5", "0.0.2"]
        main_cli(args)
        captured = capsys.readouterr()
        assert captured.out == "invalid\n"

        args = ["semver_check.py", "4.2.3-beta", "4.2.3-alpha"]
        main_cli(args)
        captured = capsys.readouterr()
        assert captured.out == "after\n"

        args = ["semver_check.py", "1.6.3", "1.6.3"]
        main_cli(args)
        captured = capsys.readouterr()
        assert captured.out == "equal\n"

    def test_main_stdin(capsys):
        args = "1.3.6   1.4.2"
        main_stdin(args)
        captured = capsys.readouterr()
        assert captured.out == "before\n"

        args = "1.3.5 1.3.5 \t0.0.2"
        main_stdin(args)
        captured = capsys.readouterr()
        assert captured.out == "invalid\n"

        args = "4.2.3-beta 4.2.3-alpha"
        main_stdin(args)
        captured = capsys.readouterr()
        assert captured.out == "after\n"

        args = " 1.6.3  1.6.3"
        main_stdin(args)
        captured = capsys.readouterr()
        assert captured.out == "invalid\n"



if __name__ == '__main__':
    pass
    #unittest.main()