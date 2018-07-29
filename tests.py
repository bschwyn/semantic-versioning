#import unittest
from unittest.mock import patch, call
import io
#import unittest.mock

from semver_check import *
import pytest

def incr(x):
    return x + 1

def test_answer():
    assert(incr(3) == 5)

def testtest(self):
    self.assertEqual(5,5)

#def test_main(self):
#    self.assertIsNone(main)

#def test_cli(self):
#    self.assertEqual(["hello", "world", "foo"], get_cli_input("hello     world   foo "))
#    self.assertEqual("", get_cli_input(("")))
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


@pytest.mark.parametrize(
    'expected', 'input', [
        (True, "1.2.3"),
        (True, "11.12.13"),
        (True, "0.0.1"),
        (False, "00.1.0"),
        (True, "1.2.03"),
        (True, "1.02.3"),
        (False, "-1.2.3"),
        (False, "1.-2.3"),
        (False, "1.-02.3"),
        (False, "-0.2.3"),
        (False, "1.2.3-"),
        (False, "1.2.3-alph*a"),
        (True, "1.2.3-aLp23aHa"),
        (True, "1.2.3-al-al-a-"),
        (True, "1.2.3-01.1.3alpha"),
        (True, "1.2.3-0alpha"),
        (True,"1.2.3-0.2.3"),
        (True,"1.2.3-alph+001"),
        (True, "1.2.3+0001-001-1.2.3"),
        (True, "1.2.3-1.2.3+123-001-11-1")
    ])
def test_is_arg_valid(expected, input):
    assert is_input_valid(input)==expected

@pytest.mark.parametrize(
    'valid','number', [
        (True,"1"),
        (True, "99")
        (True, "0"),
        (False, "-1"),
        (False, "aZ"),
        (False, "03"),
        (False, "00")
    ]
)
def test_is_non_negative_integer(valid, number):
    assert is_non_negative_integer(number)==valid

#valid prerelease MAY be denoted by a hypen and a series of dot separted identifiers
#identifiers ACII alphanumerics and hyphen [0-9A-Za-z-], identifiers must not be empty
@pytest.mark.parametrize(
    'valid', 'string', [
        (True, "1.0.0-alpha"),
        (True, "1.0.0-alpha.1"),
        (True, "1ad.0adj38-1"),
        (False, "3.01.49-alpha"),
        (False, "3.0.1..1")
    ]
)
def test_is_prerelease_valid(valid, string):
    assert is_valid_prerelease(string)==valid

#Build metadata MAY be denoted by appending a plus sign and a series of dot separated id
@pytest.mark.parametrize(
    'valid', 'string', [
        (True, "001"),
        (True, "12013"),
        (True, "exp.sha.51145"),
        (False, "exp.sha..1055"),
        (False, "3.0.1+18.1")
    ]
)
def test_is_valid_metadata(valid, string):
    assert is_valid_prerelease(string)==valid

@pytest.mark.parametrize(
    'valid', 'string', [
        (True, "1"),
        (True, "23"),
        (True, "0"),
        (False, "01"),
        (False, "-1")
    ]
)
def test_is_non_is_non_negative_integer(valid,string):
    assert is_non_negative_integer(string) == valid

@pytest.mark.parametrize(
    'valid', 'string', [
        (True, "1"),
        (True, ""),
        (True, "0"),
        (True, "a---Z001")
        (True, "-1")
        (False, ""),
        (False, "01"),
        (False, "##123*")
    ]
)
def test_is_valid_prerelease_identifier(valid, string):
    assert is_valid_prerelease(string) == valid

@pytest.mark.parametrize(
    'valid', 'string', [
        (True, "1"),
        (True, ""),
        (True, "0"),
        (True, "a---Z001")
        (True, "-1")
        (False, ""),
        (True, "01"),
        (False, "##123*")
    ]
)
def test_is_valid_metadata_identifier(valid, string):
    assert is_valid_prerelease(string) == valid

