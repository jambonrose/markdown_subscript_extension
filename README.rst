Latest Release: |Version| |Tag|

Documentation: |Docs|

Compatibility: |Implementation| |Python| |License|

Tests: |Build| |Coverage| |PyUp| |Requirements|

.. |Version| image:: http://img.shields.io/pypi/v/MarkdownSubscript.svg
        :target: https://pypi.org/project/MarkdownSubscript/
        :alt: PyPI Version

.. |Tag| image:: https://img.shields.io/github/tag/jambonrose/markdown_subscript_extension.svg
        :target: https://github.com/jambonrose/markdown_subscript_extension/releases
        :alt: Github Tag

.. |Docs| image:: https://readthedocs.org/projects/markdown_subscript_extension/badge/?version=latest
        :target: http://markdown_subscript_extension.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. |Implementation| image:: https://img.shields.io/pypi/implementation/MarkdownSubscript.svg
        :target: https://pypi.org/project/MarkdownSubscript/
        :alt: Python Implementation Support

.. |Python| image:: https://img.shields.io/pypi/pyversions/MarkdownSubscript.svg
        :target: https://pypi.org/project/MarkdownSubscript/
        :alt: Python Support

.. |License| image:: http://img.shields.io/pypi/l/MarkdownSubscript.svg
        :target: http://opensource.org/licenses/BSD-2-Clause
        :alt: License

.. |Build| image:: https://travis-ci.org/jambonrose/markdown_subscript_extension.svg?branch=development
        :target: https://travis-ci.org/jambonrose/markdown_subscript_extension
        :alt: Build Status

.. |Coverage| image:: https://codecov.io/gh/jambonrose/markdown_subscript_extension/branch/development/graph/badge.svg
        :target: https://codecov.io/gh/jambonrose/markdown_subscript_extension
        :alt: Coverage Status

.. |PyUp| image:: https://pyup.io/repos/github/jambonrose/markdown_subscript_extension/shield.svg
        :target: https://pyup.io/repos/github/jambonrose/markdown_subscript_extension/
        :alt: Updates

.. |Requirements| image:: https://requires.io/github/jambonrose/markdown_subscript_extension/requirements.svg?branch=development
        :target: https://requires.io/github/jambonrose/markdown_subscript_extension/requirements/?branch=development
        :alt: Requirements Status


=======
Read Me
=======

.. start-pypi-description

An extension to the `Python Markdown`_ project which adds the ability to
subscript text. To do so, the character :code:`~` becomes a Markdown tag
for text meant to be subscripted, and is replaced with the HTML
:code:`sub` tag.

For example, the extension transforms the text directly below into the
HTML shown after it.

.. code-block:: text

    Water is H~2~O.

.. code-block:: html

    <p>Water is H<sub>2</sub>O.</p>

This project is provided under the `Simplified (2 Clause) BSD license`_,
provided in full in the LICENSE file.

Please read `the documentation`_ for more information.

.. _`Python Markdown`: https://pypi.org/project/Markdown/
.. _`Simplified (2 Clause) BSD license`: http://choosealicense.com/licenses/bsd-2-clause/
.. _`the documentation`: https://markdown-subscript-extension.readthedocs.io/en/latest/
