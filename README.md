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

To use the program in the command line, run

python3 compare_semver.py

then type the versions:

python3 compare_semver.py
1.2.3 1.2.3

and use ctrl-d to finish the input. Press enter to enter multiple lines.

To run tests, install pytest and run 

pytest tests.py
