=======
Release
=======

This document serves as a guide for the release manage of the project.

The project follows a 'Squash and Rebase' git branch model.

The package is to be released on both Github and PyPI. The packages are to be identical, which means that the git tag that generates the Github release must be generated on the commit that is checked out when the PyPI release is created. For this reason and because the project follows a 'Squash and Rebase' branch workflow, `bumpversion` does not automatically tag commits during version changes.

As such, releases will occur on the development branch after a feature or bug branch has been merged. While the test suite will have run on the feature/bug branch, releases should wait for tests to finish on the development branch. The Makefile provides the `dist` target for generating and signing packages.

This distribution should be tested on `Test PyPI`_. `PyPI must be configured first`_.

.. code :: console

    $ twine upload dist/* -r testpypi

The `Makefile` `release` target will upload the release to PyPI.

If this is successful, then the current git commit must be tagged. Remember to place a `v` in front of the version number.

.. code :: console

    $ git tag v2.0.1
    $ git push origin --tags

.. _`Test PyPI`: https://testpypi.python.org/pypi
.. _`PyPI must be configured first`: https://docs.python.org/3/distutils/packageindex.html#the-pypirc-file
