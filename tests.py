
from semver_check import *
import pytest


@pytest.mark.parametrize(
    'compare, s1, s2', [
        (0,"1.2.3", "1.2.3"),
        (-1, "0.0.0", "0.0.1"),
        (1, "0.0.1", "0.0.0"),
        (-1, "1.2.3", "1.3.3"),
        (-1, "1.2.3", "2.1.1"),
        (-1, "1.0.0-alpha", "1.0.0-alpha.1"),
        (-1, "1.0.0-alpha.beta", "1.0.0-beta"),
        (-1, "1.0.0-beta.2", "1.0.0-beta.11"),
        (-1, "1.0.0-rc.1", "1.0.0")
    ]
)
def test_comparison(compare, s1, s2):
    l1 = parse_input_to_semver(s1)
    s1 = SemVer(l1)
    l2 = parse_input_to_semver(s2)
    s2 = SemVer(l2)
    assert comparison(s1, s2) == compare

@pytest.mark.parametrize(
    'compare, ids1, ids2', [
        (0, "1.2.3", "1.2.3"),
        (0, "123", "123"),
        (0, "alpha", "alpha"),
        (-1, "alpha.1", "alpha.beta"),
        (1, "alpha.beta", "alpha.1"),
        (-1, "alpha.beta", "beta"),
        (-1, "beta", "beta.2")
    ]
)
def test_compare_prerelease_ids(compare, ids1, ids2):
    assert compare_prerelease_ids(ids1, ids2) == compare


@pytest.mark.parametrize(
    'result, args', [
        (-1, "1.3.6   1.4.2"),
        (-2, "1.3.5 1.3.5 \t0.0.2"),
        (1, "4.2.3-beta 4.2.3-alpha"),
        (-2, " 1.6.3  1.6.3")
    ]
)
def test_main_stdin(result, args):
    assert main_stdin(args) == result

@pytest.mark.parametrize(
    'valid, string', [
        (True,"1.3.6 1.4.2"),
        (True, "4.2.3-beta 4.2.3-alpha"),
        (False, "1.8.9 1.3.5 0.0.2"),
        (False, "1.6 1.6.3")
    ]
)
def test_is_valid_input(valid, string):
    assert is_input_valid(string) == valid


@pytest.mark.parametrize(
    'valid, input', [
        (False, "1"),
        (False, "1.2"),
        (True, "1.2.3"),
        (True, "11.12.13"),
        (True, "0.0.1"),
        (False, "00.1.0"),
        (False, "1.2.03"),
        (False, "1.02.3"),
        (False, "-1.2.3"),
        (False, "1.-2.3"),
        (False, "1.-02.3"),
        (False, "-0.2.3"),
        (False, "1.2.3-"),
        (False, "1.2.3-alph*a"),
        (True, "1.2.3-aLp23aHa"),
        (True, "1.2.3-al-al-a-"),
        (False, "1.2.3-01.1.3alpha"),
        (True, "1.2.3-0alpha"),
        (True,"1.2.3-0.2.3"),
        (True,"1.2.3-alph+001"),
        (True, "1.2.3+0001-001-1.2.3"),
        (True, "1.2.3-1.2.3+123-001-11-1")
    ])
def test_is_arg_valid(valid, input):
    assert is_arg_valid(input)==valid

@pytest.mark.parametrize(
    'valid, number', [
        (True,"1"),
        (True, "99"),
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
    'valid, string', [
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
    'valid, string', [
        (True, "001"),
        (True, "12013"),
        (True, "exp.sha.51145"),
        (False, "exp.sha..1055"),
        (False, "3.0.1+18.1")
    ]
)
def test_is_valid_metadata(valid, string):
    assert is_valid_metadata(string)==valid

@pytest.mark.parametrize(
    'valid, string', [
        (True, "1"),
        (True, "0"),
        (True, "a---Z001"),
        (True, "-1"),
        (False, ""),
        (False, "01"),
        (False, "##123*")
    ]
)
def test_is_valid_prerelease_identifier(valid, string):
    assert is_valid_prerelease_identifier(string) == valid

@pytest.mark.parametrize(
    'valid, string', [
        (True, "1"),
        (True, "0"),
        (True, "a---Z001"),
        (True, "-1"),
        (False, ""),
        (True, "01"),
        (False, "##123*")
    ]
)
def test_is_valid_metadata_identifier(valid, string):
    assert is_valid_metadata_identifier(string) == valid


@pytest.mark.parametrize(
    'valid, string', [
        (True, "3-aLp23aHa"),
        (True, "3-al-al-a-"),
        (False, "3-01.1.3alpha"),
        (True, "3-0alpha"),
        (True, "3-0.2.3"),
        (False, "03-0.1.2"),
        (False, "3+001-1.2.3"),
        (False, "3-alph*a")
    ])
def test_is_valid_patch_and_prerelease(valid, string):
    assert is_valid_patch_and_prerelease(string) == valid


@pytest.mark.parametrize(
    'valid, string', [
        (True, "3"),
        (False,"03"),
        (False, "3-alph*a"),
        (True, "3-aLp23aHa"),
        (True, "3-al-al-a-"),
        (False, "3-01.1.3alpha"),
        (True, "3-0alpha"),
        (True, "3-0.2.3"),
        (True, "3-alph+001"),
        (True, "3+0001-001-1.2.3"),
        (True, "3-1.2.3+123-001-11-1")
    ])
def test_is_patch_prerelease_meta_valid(valid, string):
    assert is_patch_prerelease_meta_valid(string) == valid

@pytest.mark.parametrize(
    'patch, prerelease, input', [
        ('3', 'alpha', '3-alpha'),
        ('3', None, '3'),
        ('0', 'rc.123.3', '0-rc.123.3'),
    ]
)
def test_split_patch_and_prerelease(patch, prerelease, input):
    p1, p2 = split_patch_and_prerelease(input)
    assert p1 == patch and p2 == prerelease

@pytest.mark.parametrize(
    'input, major, minor, patch, pre, meta', [
        ("1.0.0", "1","0","0",None,None),
        ("1.2.3+123", "1","2","3",None,"123"),
        ("1.2.3-alpha", "1","2","3","alpha",None),
        ("1.2.3-alpha+001", "1","2","3","alpha","001"),
    ]
)
def test_parse_input_to_semver(input, major, minor, patch, pre, meta):
    mj, mn, pt, pr, m = parse_input_to_semver(input)
    assert mj == major and mn == minor and pt == patch and pr == pre and m == meta

