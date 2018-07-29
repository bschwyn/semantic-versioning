#notes
#reserve problem
#author: ben schwyn

#not every language can be sent over
#explicitly a learning project, consequences of failure
# idiosyncratic human needs
# how do people choose projects
# launching in
# no expected timeline

#implement semantic versioning
#Major.Minor.Patch
#MAJOR version when you make incompatible API changes,
#MINOR version when you add functionality in a backwards-compatible manner, and
#PATCH version when you make backwards-compatible bug fixes.
# version lock (the inability to upgrade a package without having to release new versions of every dependent package)
#version promiscuity (assuming compatibility with more future versions than is reasonable)

# For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise.
# Once you identify your public API, you communicate changes to it with specific increments to your version number.

#what does the public API look like?

#a module
#convenient data type for semantic versions

#timing:
#4:40 time!
#4:30 start upload ish
#4:20 documentation
#4:00 clean up
#input &test 2:00
#class &t 2:45
#specification details & comparison functions


#check validity, then construct datatype with valid input
#attempt to construct datatype with potentially invalid input, check validity on the way


import sys
import string
import re

class SemVer():

    def __init__(self, major, minor, patch, prerelease, meta):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.meta = meta

def comparison(semver1, semver2):

    #precendece MUST be calclulated by separating the version into major, minor, patch, prerelease identifiers
    #precedence is determined by the first difference when comparing each of these from left to right as follows:
    #major, minor and patch versons are compared numerically. Ex 1.0.0 < 2.0.0 < 2.1.0 < 2.1.1
    #when major, minor, and patch are equal, a pre-release version has lower precedence. Ex: 1.0.0-alpha < 1.0.0
    #precedence for two prerelease versions MUST be determined by comparing each dot separated identifier from left to
    #right until a difference is found as follows: identifiers consisting only of digits are compared numerically and
    #identifiers with letters or hyphens are compared lexically in ASCII sort order. Numeric identifiers always have
    #lower precedence than non-numeric identifiers. A larger set of pre-release fields has a higher precedence than a
    #smaller set, if all of the preceding identifiers are equal. Example: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta
    #< 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0

    major1 = semver1.major
    minor1 = semver1.minor
    patch1 = semver1.patch
    prerelease1 = semver1.prerelease

    major2 = semver2.major
    minor2 = semver2.minor
    patch2 = semver2.minor
    prerelease2 = semver2.prerelease

    major_result = compare_major(major1, major2)
    minor_result = compare_minor(minor1, minor2, major_result)
    patch_result = compare_patch(patch1, patch2, minor_result)
    all_result = compare_prerelease(prerelease1, prerelease2, patch_result)
    return all_result


def compare_major(major1, major2):
    #numeric comparison
    if int(major1) > int(major2):
        return 1
    elif int(major1) == int(major2):
        return 0
    else:
        return -1

def compare_minor(minor1, minor2, major):
    #numeric comparison
    if major == 0:
        if int(minor1) > int(minor2):
            return 1
        elif int(minor1) == int(minor2):
            return 0
        else:
            return -1
    else:
        return major

def compare_patch(patch1, patch2, minor):
    #numeric comparison
    if minor == 0:
        if int(patch1) > int(patch2):
            return 1
        elif int(patch1) == int(patch2):
            return 0
        else:
            return -1
    else:
        return minor


def compare_prerelease_ids(pre1, pre2):
    # identifiers with letters or hyphens are compared lexically in ASCII sort order. Numeric identifiers always have
    # lower precedence than non-numeric identifiers. A larger set of pre-release fields has a higher precedence than a
    # smaller set, if all of the preceding identifiers are equal.

    ids1 = pre1.split('.')
    ids2 = pre1.split('.')
    # ids consisting of only digits are compared numerically
    # ids with letters or hypens are compared lexically
    # numeric identifiers always have lower precedence than non-numeric ids
    # larger set of prerelease fields has a higher precedence than a smaller set if all the preceding identifiers are equal


def compare_prerelease(pre1, pre2, patch):
    # precedence for two prerelease versions MUST be determined by comparing each dot separated identifier from left to
    # right until a difference is found as follows: identifiers consisting only of digits are compared numerically and
    # identifiers with letters or hyphens are compared lexically in ASCII sort order. Numeric identifiers always have
    # lower precedence than non-numeric identifiers. A larger set of pre-release fields has a higher precedence than a
    #smaller set, if all of the preceding identifiers are equal. Example: 1.0.0-alpha < 1.0.0-alpha.1 < 1.0.0-alpha.beta
    # < 1.0.0-beta < 1.0.0-beta.2 < 1.0.0-beta.11 < 1.0.0-rc.1 < 1.0.0

    if patch == 0:
        if pre1 == None and pre2 == None:
            return 0
        elif pre2 == None: #prerelease comes before no prerelease
            return 1
        elif pre1 == None:
            return -1
        else:
            return compare_prerelease_ids(pre1,pre2)
    else:
        return patch




#---------------------------------------------------
#functions for validating version numbers as correct
#---------------------------------------------------

def is_non_negative_integer(string):
    if string== '0':
        return True
    elif string[0] != 0 and int(string) > 0:
        return True
    else:
        return False

def is_valid_major(string):
    return is_non_negative_integer(string)

def is_valid_minor(string):
    return is_non_negative_integer(string)

def is_valid_patch(string):
    return is_non_negative_integer(string)

def is_valid_prerelease_identifier(id):
    #identifers must comprise only ascii alphanumerics and hypen
    #identifier must not be empty
    #numeric identifiers must not include leading zeroes
    if id == "":
        return False
    elif re.match(r"[0-9]", id):
        return is_non_negative_integer(id)
    elif re.match(r"[0-9A-Za-z-]", id):
        return True
    else:
        return False

def is_valid_metadata_identifier(id):
    #identifers must comprise only ascii alphanumerics and hyphen
    #identifers must not be empty. [leading zeroes ok]
    if id == "":
        return False
    elif re.match(r"[0-9A-Za-z-]", id):
        return True
    else:
        return False

def is_valid_prerelease(string):
    #pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers
    #identifiers MUST comprise only ASCII alphanumeris and hyphen
    # identifiers MUST NOT be empty, MUST NOT include leading zeroes
    identifiers = string.split('.')
    return all([x for x in identifiers if is_valid_prerelease_identifier(x)])

def is_valid_metadata(string):
    #build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers
    #identifiers MUST comprise only ASCII alphanumerics and hyphen,
    #identifers MUST NOT be empty
    identifiers = string.split('.')
    return all([x for x in identifiers if is_valid_metadata_identifier(x)])

def is_valid_patch_and_prerelease(input):
    #prerelease may or may not be present
    input = input[0].split('-', maxsplit=1)

    # patch and prerelease
    if len(input) == 2:
        return is_valid_patch(input[0]) and is_valid_prerelease(input[1])

    # only patch
    else:
        return is_valid_patch(input[0])

def is_patch_prerelease_meta_valid(input):
    #input must have patch, may have prerelease, and may have metadata

    input = input.split('+')

    if len(input) == 1:     #no metadata,  #1.2.3-alpha--2.1 or 1.2.3
        return is_valid_patch_and_prerelease(input[0])

    elif len(input) == 2:   #yes metadata
        #1.2.3-alpha+001, 1.2.3+001, 1.2.3+0-1-0-1, 1.2.3-a-a-+101.13-aaa
        return is_valid_patch_and_prerelease(input[0]) and is_valid_metadata(input[1])

    else:
        return False

def is_arg_valid(input):
    valid = True

    #major
    input = input.split('.', maxsplit=1)
    if not is_valid_major(input[0]):
        valid = False

    #minor
    input = input[1].split('.', maxsplit=1)
    if not is_valid_minor(input[0]):
        valid = False

    #patch and other
    if not is_patch_prerelease_meta_valid(input[1]):
        valid = False

    return valid

def is_input_valid(input):
    if input[0] in string.whitespace:
        return False

    input = input.split()
    if len(input) != 2:
        return False
    return is_arg_valid(input[0]) and is_arg_valid(input[1])

#------------------------------------------
#after validation parse the version number into a semVer class
#------------------------------------------

def parse_input_to_semver(input):

    input = input.split('.', maxsplit=2)
    major = input[0]
    minor = input[1]

    input = input.split('+')
    if len(input) == 1:
        # patch and/or prerelease
        input = input[0].split('-', maxsplit=1)
        patch = input[0]
        prerelease = input[1]
        metadata = None
    elif len(input) == 2:
        # yes metadata
        metadata = input[1]

        # prelease?
        patch_and_prerelease = input[0].split('-', maxsplit=1)
        if len(patch_and_prerelease) == 1:
            patch = patch_and_prerelease[0]
            prerelease = None
        else:
            patch = patch_and_prerelease[0]
            prerelease = patch_and_prerelease[1]

    return major, minor, patch, prerelease, metadata


def main_cli(args):
    #this does not fit the specification because of what happens with initial whitespace
    if len(args) == 1: #whitespace
        result = None
    elif len(args) == 3:
        valid = is_arg_valid(args[1]) and is_arg_valid(args[2])
        if valid:
            semver1 = parse_input_to_semver(args[0])
            semver2 = parse_input_to_semver(args[1])
            result = comparison(semver1, semver2)
        else:
            result = "invalid"
    else:
        result = "invalid"
    if result:
        print(result)

def main_stdin(line_of_stdin):
    if line_of_stdin == "":
        result = None
    elif is_input_valid(line_of_stdin):
        args = line_of_stdin.split()
        semver1 = parse_input_to_semver(args[0])
        semver2 = parse_input_to_semver(args[1])
        result = comparison(semver1, semver2)
    else:
        result = "invalid"
    if result:
        print(result)


if __name__=="__main__":
    sys.stdin.readlines()
    input_string = sys.argv[1]
    main(input_string)



