.. highlight:: console

============
Contributing
============

Contributions are welcome, and they are greatly appreciated! Every
little bit helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs on `Github issues`_.

If you are reporting a bug, please include:

* Your operating system name and version.

* Any details about your local setup that might be helpful in
  troubleshooting.

* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the `GitHub issues`_ for bugs. Anything tagged with "bug" and
"help wanted" is open to whoever wants to implement it.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the `GitHub issues`_ for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Markdown Superscript could always use more documentation, whether as part
of the official Markdown Subscript docs, in docstrings, or even on the
web in blog posts, articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to `file an issue on Github`_.

If you are proposing a feature:

* Explain in detail how it would work.

* Keep the scope as narrow as possible, to make it easier to implement.

* Remember that this is a volunteer-driven project, and that contributions
  are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `markdown_subscript_extension`
for local development.

1. Fork the `markdown_subscript_extension` repo on GitHub.
2. Clone your fork locally::

    $ git clone git@github.com:YOUR_USERNAME_HERE/markdown_subscript_extension.git

3. Install your local copy into a virtualenv. Assuming you have
   virtualenvwrapper installed, this is how you set up your fork for local
   development::

    $ mkproject markdown_subscript_extension
    $ pip install -r requirements/dev_requirements.txt
    $ pip install -r requirements/test_requirements.txt
    $ python setup.py develop

4. Create a branch for local development::

    $ git checkout -b name-of-your-bugfix-or-feature

   Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8
   and the tests, including testing other Python versions with tox::

    $ flake8 mdx_subscript.py tests
    $ nosetests --with-coverage --cover-package=mdx_subscript # or: make test
    $ tox

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin name-of-your-bugfix-or-feature

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests.

2. If the pull request adds functionality, the docs should be updated.
   Put your new functionality into a function with a docstring, and add
   the feature to the list in README.rst.

3. The pull request should work for Python 2.7, 3.3, 3.4 3.5, 3.6, and
   for PyPy. Check `Travis CI`_ pull requests and make sure that the
   tests pass for all supported Python versions.

.. _`file an issue on Github`:
.. _`Github Issues`: https://github.com/jambonrose/markdown_subscript_extension/issues
.. _`Travis CI`: https://travis-ci.org/jambonrose/markdown_subscript_extension/
