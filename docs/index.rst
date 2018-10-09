Welcome to Markdown Subscript's documentation!
==============================================

This Python package is an extension to the `Python Markdown`_ project
which adds the ability to subscript text. To do so, the character
:code:`~` becomes a Markdown tag for text meant to be subscripted, and
is replaced with the HTML :code:`sub` tag.

For example, the extension transforms the text directly below into the
HTML shown after it.

.. code-block:: text

    The molecular composition of water is H~2~O.

.. code-block:: html

    <p>The molecular composition of water is H<sub>2</sub>O.</p>

The code is `Simplified (2 Clause) BSD license`_ and is available on `Github.`_

.. _`Python Markdown`: https://pypi.org/project/Markdown/
.. _`Simplified (2 Clause) BSD license`: https://choosealicense.com/licenses/bsd-2-clause/
.. _`Github.`: https://github.com/jambonrose/markdown_subscript_extension

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage
   contributing
   release
   authors
   history
