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

If you are reporting a bug, please follow the guidelines shown to you
while reporting the bug

Fix Bugs and Support Others
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Look through the open `GitHub issues`_. Anything tagged with
"help wanted" is open to whoever wants to implement it. Anything tagged
with "support" means someone needs help, and you may be the person to
help them!

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the `GitHub issues`_ for features. Anything tagged with
"enhancement" and "help wanted" is open to whoever wants to implement it.

Write Documentation
~~~~~~~~~~~~~~~~~~~

Markdown Subscript could always use more documentation, whether as part
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

.. _`file an issue on Github`:
.. _`Github Issues`: https://github.com/jambonrose/markdown_subscript_extension/issues

Get Started!
------------

Ready to contribute? Here's how to set up ``markdown_subscript_extension``
for local development.

1. Fork the ``markdown_subscript_extension`` repository on `GitHub`_.

.. _`Github`: https://github.com/jambonrose/markdown_subscript_extension

2. Create a directory for your project, and then create a virtual
   environment.  If you new to virtual environments, `RealPython's
   Virtualenv Primer`_ is for you! The code below demonstrates how to
   create a virtual project with `Virtualenvwrapper`_ ::

   $ mkproject markdown_subscript_extension

.. _`RealPython's Virtualenv Primer`: https://realpython.com/python-virtual-environments-a-primer/
.. _Virtualenvwrapper: https://virtualenvwrapper.readthedocs.io/en/latest/

3. Clone your fork locally into your new project. ::

    $ git clone git@github.com:YOUR_USERNAME_HERE/markdown_subscript_extension.git .

4. Install the necessary dependencies using pip. If you don't have
   `pip`_ installed, the `Python installation guide`_ can guide you
   through the process. ::

   $ pip install -r requirements/dev_requirements.txt
   $ pip install -r requirements/lint_requirements.txt
   $ pip install -r requirements/test_requirements.txt
   $ python setup.py develop

.. _pip: https://pip.pypa.io/en/stable/
.. _Python installation guide: https://docs.python-guide.org/starting/installation/

5. Create a branch for local development and begin to make changes! ::

   $ git checkout -b name-of-your-bugfix-or-feature

6. Make small, targeted changes. Commit often, and write clear messages!
   Remember that this is a volunteer-drive project. The clearer your
   intent and your changes, the easier it will be for us to review your
   work. ::

    $ git add .
    $ git commit -m "Your detailed description of your changes."

5. The project is configured to use `pre-commit`_. If you'd like to have
   each commit checked as you make it, install it as a hook for your
   repository, as demonstrated below. ::

   $ pre-commit install

.. _`pre-commit`: https://pre-commit.com/

6. When you're done making changes, check that your changes pass the
   test suite. If you're not using `pre-commit`_, you will also need to
   use the linters and auto-formatters. ::

   $ make test  # or python setup.py test
   $ # linters below
   $ flake8 mdx_subscript.py tests
   $ isort --verbose --check-only --diff mdx_subscript.py
   $ black mdx_subscript.py tests

7. If you have Python 2.7, 3.4, 3.5, 3.6, and 3.7 installed, as well as
   both PyPy and PyPy3, you may use ``tox`` to run all of the tests in
   all of the supported environments. ::

   $ tox

8. Once you've made the changes you want, push your branch to GitHub. ::

    $ git push -u origin name-of-your-bugfix-or-feature

9. Submit a pull request from your new branch to the original repository
   through the GitHub website.

10. 🎉 Thank you for taking the time to read this and for your potential
    contributions!

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. If a bug-fix or new feature, the pull request should include tests.

2. If the pull request adds functionality, the docs should be updated.

3. The pull request should work for all supported Python versions. If
   you are unable to run ``tox`` locally, the CI will run the test suite
   for you (but please consider running the suite beforehand).

.. _`Travis CI`: https://travis-ci.org/jambonrose/markdown_subscript_extension/
