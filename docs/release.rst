==========================
Package Release Guidelines
==========================

This document serves as a guide for the release manage of the project.
The package is to be released on both Github and PyPI.

The project follows semantic versioning and uses the 'Squash and Rebase'
git branch model.

If the version of the package has not been properly increased, please use
``bumpversion`` to increase the major, minor, or patch number as needed.
Add change notes to the history document.

Once the branch for bumping the version has been tested and squashed, the
**package release** should occur on the **development branch**. Remember
to pull/fast-forward the development branch from Github!

To release to PyPI, first run the Makefile ``dist`` target. If all goes
well, upload the release using the ``release`` target.

.. code-block:: console

    $ make dist
    $ make release

Tag the latest commit  with the new version (the version should be
prefixed with a ``v`` for consistency), and then push to Github.

.. code-block:: console

    $ git tag v2.0.1
    $ git push origin --tags

🎉 That's all! You've released on Github and PyPI!
