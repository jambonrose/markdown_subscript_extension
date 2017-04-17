Latest Release: |Version|

Compatibility: |Implementation| |Python| |License|

Tests: |Build| |Coverage| |Requirements|

.. |Version| image:: http://img.shields.io/pypi/v/MarkdownSubscript.svg
        :target: https://pypi.python.org/pypi/MarkdownSubscript/
        :alt: PyPI Version

.. |Implementation| image:: https://img.shields.io/pypi/implementation/MarkdownSubscript.svg
        :target: https://pypi.python.org/pypi/MarkdownSubscript/
        :alt: Python Implementation Support

.. |Python| image:: https://img.shields.io/pypi/pyversions/MarkdownSubscript.svg
        :target: https://pypi.python.org/pypi/MarkdownSubscript/
        :alt: Python Support

.. |License| image:: http://img.shields.io/pypi/l/MarkdownSubscript.svg
        :target: http://opensource.org/licenses/BSD-2-Clause
        :alt: License

.. |Build| image:: https://travis-ci.org/jambonrose/markdown_subscript_extension.svg?branch=development
        :target: https://travis-ci.org/jambonrose/markdown_subscript_extension
        :alt: Build Status

.. |Coverage| image:: https://img.shields.io/coveralls/jambonrose/markdown_subscript_extension.svg
        :target: https://coveralls.io/r/jambonrose/markdown_subscript_extension
        :alt: Coverage Status

.. |Requirements| image:: https://requires.io/github/jambonrose/markdown_subscript_extension/requirements.svg?branch=development
        :target: https://requires.io/github/jambonrose/markdown_subscript_extension/requirements/?branch=development
        :alt: Requirements Status

=======
Read Me
=======

An extension to the `Python Markdown`_ project which adds the ability to
subscript text. To do so, the character :code:`~` becomes a Markdown tag
for text meant to be subscripted, and is replaced with the HTML
:code:`sub` tag.

For example, given the text: ::

    The molecular composition of water is H~2~O.

… using Markdown with this extension will output:

.. code :: html

    <p>The molecular composition of water is H<sub>2</sub>O.</p>

This project is provided under the `Simplified (2 Clause) BSD license`_,
provided in full in the LICENSE file.

.. _`Python Markdown`: https://pypi.python.org/pypi/Markdown
.. _`Simplified (2 Clause) BSD license`: http://choosealicense.com/licenses/bsd-2-clause/

Installation
------------

Dependencies:

- Python 2.7, 3.3+

- Markdown 2.5+
  (Tested against latest patch version of Markdown 2.5 and 2.6)

To install the latest stable release (recommended):

.. code :: bash

    pip install MarkdownSubscript

To install the development version:

.. code :: bash

    pip install git+git://github.com/jambonrose/markdown_subscript_extension.git

Basic Usage
-----------

Python
^^^^^^

.. code :: pycon

    >>> from markdown import markdown
    >>> text = "The molecular composition of water is H~2~O."
    >>> markdown(text, ['subscript'])
    '<p>The molecular composition of water is H<sub>2</sub>O.</p>'

Command Line
^^^^^^^^^^^^

.. code :: bash

    $ echo 'The molecular composition of water is H~2~O.' > text.md
    $ python -m markdown -o html5 -x 'subscript' -f text.html text.md
