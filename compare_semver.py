#implementation of semantic versioning
#https://semver.org/ specification here

#provides a datatype for semantic versions, in which major, minor, patch, pre-release, and metadata can be separately
#accessed.
#A way to parse semver strings as described in the specification
#comparison functions to implement precedence as described in the specification

import sys
import string

class SemVer():

    def __init__(self, input):
        self.major = input[0]
        self.minor = input[1]
        self.patch = input[2]
        self.prerelease = input[3]
        self.meta = input[4]


#---------------------------------------------------
#comparison functions to implement precedence.
#---------------------------------------------------

#a > b ---> 1
#a == b --> 0
#a < b --> -1

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
    patch2 = semver2.patch
    prerelease2 = semver2.prerelease

    #pass the state of the compare function down the line of the semantic string
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


def compare_prerelease_ids(ids1, ids2):
    # ids consisting of only digits are compared numerically
    # ids with letters or hyphens are compared lexically in ASCII sort order.
    # numeric identifiers always have lower precedence than non-numeric ids
    # larger set of prerelease fields has a higher precedence than a
    # smaller set if all the preceding identifiers are equal

    i = 0
    min_len = min(len(ids1), len(ids2))
    while i < min_len:
        id1 = ids1[i]
        id2 = ids2[i]
        if is_non_negative_integer(id1) and is_non_negative_integer(id2):
            if int(id1) > int(id2):
                return 1
            elif int(id1) < int(id2):
                return -1
            else:
                i += 1
        elif is_non_negative_integer(id1):  # .1 < .beta
            return -1
        elif is_non_negative_integer(id2):
            return 1
        else:  # compare ascii sort order
            if id1 > id2:  #
                return 1
            elif id1 < id2:
                return -1
            else:
                i += 1
    max_len = max(len(ids1), len(ids2))
    if max_len > min_len:
        if max_len == len(ids1):
            return 1
        else:  # max_len == len(ids2):
            return -1
    else:
        return 0

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
            return -1
        elif pre1 == None:
            return 1
        else:
            ids1 = pre1.split('.')
            ids2 = pre2.split('.')
            return compare_prerelease_ids(ids1, ids2)

    else:
        return patch


#---------------------------------------------------
#functions for validating semantic version strings as correct
#---------------------------------------------------

def is_non_negative_integer(string): #have test
    try:
        if string== '0':
            return True
        elif string[0] != '0' and int(string) > 0:
            return True
        else:
            return False
    except Exception:
        return False

def is_alnum_or_hyphen(id):
    x = id.replace('-','')
    return x.isalnum()

def is_valid_major(string):
    return is_non_negative_integer(string)

def is_valid_minor(string):
    return is_non_negative_integer(string)

def is_valid_patch(string):
    return is_non_negative_integer(string)

def is_valid_prerelease_identifier(id): #have test
    #identifers must comprise only ascii alphanumerics and hyphen
    #identifier must not be empty
    #numeric identifiers must not include leading zeroes
    try:
        if id == "":
            return False
        elif id.isnumeric():
            return is_non_negative_integer(id)
        elif is_alnum_or_hyphen(id):
            return True
        else:
            return False
    except Exception:
        return False

def is_valid_metadata_identifier(id): #have test
    #identifers must comprise only ascii alphanumerics and hyphen
    #identifers must not be empty. [leading zeroes ok]
    try:
        if id == "":
            return False
        elif is_alnum_or_hyphen(id):
            return True
        else:
            return False
    except Exception:
        return False

def is_valid_prerelease(string): #have test
    #pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers
    #identifiers MUST comprise only ASCII alphanumeris and hyphen
    # identifiers MUST NOT be empty, MUST NOT include leading zeroes
    identifiers = string.split('.')
    return all([is_valid_prerelease_identifier(x) for x in identifiers])

def is_valid_metadata(string): #have test
    #build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers
    #identifiers MUST comprise only ASCII alphanumerics and hyphen,
    #identifers MUST NOT be empty
    identifiers = string.split('.')
    return all([is_valid_metadata_identifier(x) for x in identifiers])

def is_valid_patch_and_prerelease(input):
    #prerelease may or may not be present
    input = input.split('-', maxsplit=1)

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

def is_arg_valid(input): #have test
    #must do this carefully and step by step as all components may not be present

    #major
    input = input.split('.', maxsplit=1) #1.2.3-4 --> ["1", "2.3-4"]
    if len(input) < 2:
        return False
    if not is_valid_major(input[0]):
        return False


    #minor
    input = input[1].split('.', maxsplit=1) #"2.3-4" --->["2", "3-4"]
    if len(input) < 2:
        return False
    if not is_valid_minor(input[0]):
        return False

    #patch and other
    if not is_patch_prerelease_meta_valid(input[1]): #3-4"
        return False

    return True


def is_input_valid(input): #have test
    if input[0] in string.whitespace:
        return False

    input = input.split()
    if len(input) != 2:
        return False
    return is_arg_valid(input[0]) and is_arg_valid(input[1])

#------------------------------------------
#after validation parse the version number into a semVer class
#------------------------------------------

def split_patch_and_prerelease(input_string):
    input = input_string.split('-', maxsplit=1)
    if len(input) == 1:
        patch = input[0]
        prerelease = None
    elif len(input) == 2:
        patch = input[0]
        prerelease = input[1]
    else:
        return False #throw exception
    return patch, prerelease

def parse_input_to_semver(semver_string):
    #assuming string is valid...
    input = semver_string.split('.', maxsplit=2)
    major = input[0]
    minor = input[1]

    input = input[2].split('+', maxsplit=1)
    if len(input) == 1:
        # patch and/or prerelease, no metadata
        metadata = None
        patch, prerelease = split_patch_and_prerelease(input[0])

    elif len(input) == 2:
        # yes metadata
        metadata = input[1]
        patch, prerelease = split_patch_and_prerelease(input[0])

    return [major, minor, patch, prerelease, metadata]


def main_cli(args):
    #this does not fit the specification because of what happens with initial whitespace
    if len(args) == 1: #whitespace
        result = None

    #validation
    elif len(args) == 3:
        valid = is_arg_valid(args[1]) and is_arg_valid(args[2])
        if valid:

            #parsing
            semver1 = parse_input_to_semver(args[0])
            semver2 = parse_input_to_semver(args[1])

            #comparison
            result = comparison(semver1, semver2)
        else:
            result = -2
    else:
        result = -2
    return result

def main_stdin(line_of_stdin):
    try:
        if line_of_stdin == "" or line_of_stdin in string.whitespace:
            result = None
        elif is_input_valid(line_of_stdin):
            args = line_of_stdin.split()
            semver1 = SemVer(parse_input_to_semver(args[0]))
            semver2 = SemVer(parse_input_to_semver(args[1]))
            result = comparison(semver1, semver2)
        else:
            result = -2
    except Exception:
        return -2
    return result

def print_result(result):
    if result == 1:
        print("after")
    elif result == 0:
        print("equal")
    elif result == -1:
        print("before")
    elif result == None:
        pass
    else:
        print("invalid")



if __name__=="__main__":
    messages = sys.stdin.readlines()
    for line in messages:
        r =main_stdin(line)
        print_result(r)