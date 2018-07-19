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

import re

class SemVer():

    def __init__(self, major, minor, patch, prerelease, meta):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.prerelease = prerelease
        self.meta = meta

def comparison(semver1, semver2):
    pass

def is_postive_integer_w_no_leading_zeros(string):
    pass

def is_valid_major(string):
    return is_non_negative_integer(string)

def is_non_negative_integer(string):
    if string== '0':
        return True
    elif string[0] != 0 and int(string) > 0:
        return True
    else:
        return False

def is_valid_minor(string):
    return is_non_negative_integer(string)

def is_valid_patch(string):
    return is_non_negative_integer(string)

def is_valid_prerelease(string):
    return re.match(r"[0-9A-Za-z-]", string)


def is_valid_metadata(string):
    return re.match(r"[0-9A-Za-z-]", string)

def is_patch_prerelease_meta_valid(input):
    #patch only [nonneg or 0]
    #patch and prerelase [nonneg or 0 - [any . or - separated asccii]
    #patch and meta #plus [nonnegative or 0 + ascii alphanumerics or -]
    #patch prelease and meta [nonnegative or 0 - any number dot separated ascii / hyphens + ascii or -

    input = input.split('+')
    if len(input) == 1:
        #patch and/or prerelease
        input = input[0].split('-', maxsplit=1)
        if len(input) ==2:
            return is_valid_patch(input[0]) and is_valid_prerelease(input[1])
        else:
            return is_valid_patch(input[0])

    elif len(input) == 2:
        #yes metadata

        #prelease?
        patch_and_prerelease = input[0].split('-', maxsplit=1)
        if len(patch_and_prerelease) == 1:
            return is_valid_patch(patch_and_prerelease[0]) and \
                   is_valid_metadata(input[1])
        else:
            return is_valid_patch(patch_and_prerelease[0]) and \
                   is_valid_prerelease(patch_and_prerelease[1]) and \
                   is_valid_metadata(input[1])
    else:
        return False

def parse_patch_prerelease_meta(input):
    input = input.split('+')
    if len(input) == 1:
        #patch and/or prerelease
        input = input[0].split('-', maxsplit=1)
        patch = input[0]
        prerelease = input[1]
        metadata = None
    elif len(input) == 2:
        #yes metadata
        metadata = input[1]

        #prelease?
        patch_and_prerelease = input[0].split('-', maxsplit=1)
        if len(patch_and_prerelease) == 1:
            patch = patch_and_prerelease[0]
            prerelease = None
        else:
            patch = patch_and_prerelease[0]
            prerelease = patch_and_prerelease[1]

    return patch, prerelease, metadata

def parse_input_to_semver(input):

    input = input.split('.', maxsplit=2)
    major = input[0]
    minor = input[1]
    patch, prerelease, meta = parse_patch_prerelease_meta(input[2])

    newSemVer= SemVer(major, minor, patch, prerelease, meta)
    return newSemVer

def is_arg_valid(input):
    valid = True

    input = input.split('.', maxsplit=1)
    if not is_valid_major(input[0]):
        valid = False

    input = input[1].split('.', maxsplit=1)
    if not is_valid_minor(input[0]):
        valid = False

    ppm_valid = is_patch_prerelease_meta_valid(input[1])

    return valid and ppm_valid

def is_input_valid(input):

    input = input.split()
    if len(input) != 2:
        return False
    return is_arg_valid(input[0]) and is_arg_valid(input[1])


def get_cli_input(args):
    args.split()
    return args



def main():

    args = get_cli_input(sys.argv[1])
    valid = is_input_valid(args)
    if valid:
        semver1 = parse_input_to_semver(args[0])
        semver2 = parse_input_to_semver(args[1])
        result = comparison(semver1, semver2)
        print(result)
    else:
        print("invalid")


if __name__=="__main__":
    main()



