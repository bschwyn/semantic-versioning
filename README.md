# semantic-versioning

What I learned creating this program the second time through:

I was able to get the unittests running in the way that I wanted to. I decided to go through the program much slower and to find all the bugs that I could before they appeared. Some of the resulted in me changing the use case of the program as more standard approaches ("python semver.py 1.2.3 4.5.6") would remove small error cases (removing the need for a particular whitespace check would would then be handled by the command line)


I didn't know how sys.argv split the input and whether or not it was on whitespace or normal spaces, and whether an input like: "python semver_check.py    1.2.3 4.5.6" would result in a sys.argv file like ["   1.2.3","4.5.6"] or ["1.2.3","4.5.6"]. Following the specification carefully, my reading is that the first would be an invalid input.

Arrgggg... I think the proper thing to do would have been to spend the before time thinking about "what is standard input, how does it work exactly, do I really know how to read from it?"
How is sys.stdin different from sys.argv? Do I know the difference?
