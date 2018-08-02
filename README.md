# semantic-versioning

In software management, keeping track of new package versions can become unweildy as they make changes that make it difficult
to safely move your own project forward. Semantic Versioning is a formal specification of how to assign numbers to new package
versions in order to keep track of which changes are being made and what this will require from the program using the package.
For example, a simple version has the format Major.Minor.Patch. Bug fixes that do not affect the API increment the patch version,
backwards compatible API additions/changes increment the minor version, and incompatible changes to the API result in a change
of the major version. The full specifiation can be found https://semver.org/

This program verifies both the validity and the ordering of two semantic versions. This is important for a larger program 
which might detect packages in use and find the most recent version using a comparison process. With complicated pre-release 
and metadata formats, it can become difficult to find the ordering of package versions.

### Usage

To use the program in the command line, run
```
python3 compare_semver.py
```
then type the versions:
```
python3 compare_semver.py
1.2.3 1.2.3
```
and use `ctrl-d` to finish the input. Press enter to enter multiple lines.

To run tests, `pip install -U pytest 3.7.0` and run 
```
pytest tests.py
```
### Public Api

- empty lines are ignored

A valid line of input will contain, in order:
- 1) a valid semantic version string
- 2) one or more whitespace characters
- 3) another semantic version string
- 4) zero or more whitespace characters

invalid lines print the string "invalid" to std_out, and valid strings print "before" if the left version is earlier than the right, "after" if if the left version is later than the right, and "equal" if they have the same precedence.

For example, given the following input:
```
1.3.6 1.4.2
1.7.9 1.3.5 0.0.2

4.2.3-beta     4.2.3-alpha
1.6 1.6.3
```
The program prints:
```
before
invalid
after
invalid
```
