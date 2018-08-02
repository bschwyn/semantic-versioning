# semantic-versioning

What I learned creating this program the second time through:

I was able to get the unittests running in the way that I wanted to. I decided to go through the program much slower and to find all the bugs that I could before they appeared. Some of the resulted in me changing the use case of the program as more standard approaches ("python semver.py 1.2.3 4.5.6") would remove small error cases (removing the need for a particular whitespace check would would then be handled by the command line)


I didn't know how sys.argv split the input and whether or not it was on whitespace or normal spaces, and whether an input like: "python semver_check.py    1.2.3 4.5.6" would result in a sys.argv file like ["   1.2.3","4.5.6"] or ["1.2.3","4.5.6"]. Following the specification carefully, my reading is that the first would be an invalid input.

Arrgggg... I think the proper thing to do would have been to spend the before time thinking about "what is standard input, how does it work exactly, do I really know how to read from it?"
How is sys.stdin different from sys.argv? Do I know the difference?

#what problem semantic verisoning solves


#Formal specifications are an interesting problem and occur in contract codes.

Semantic versioning is a formalization of what was previously widespread practice in versioning software updates.

This is a program which will verify the precedence ordering of two program versions.

Why is this useful?

It's important to verify that a version is implemented


#in systems with many dependencies, there is a set of rules and requirements dictating
how version numbers are assigned and incremented.
Formal specifications are an interest

#small code example of how the project is used

python3 semver_check.py
1.2.3-alpha 1.3.4+12003
ctr-d

before

#about