An extension to the `Python Markdown`_ project which adds the ability to subscript text. To do so, the character :code:`~` becomes a Markdown tag for text meant to be subscripted, and is replaced with the HTML :code:`sub` tag.

For example, given the text: ::

    The molecular composition of water is H~2~O.

… using Markdown with this extension will output: ::

    <p>The molecular composition of water is H<sub>2</sub>O.</p>

This project is provided under the `Simplified (2 Clause) BSD license`_.

Installation
------------

::

    pip install MarkdownSubscript

Usage
-----

Python
^^^^^^

>>> from markdown import markdown
>>> text = "The molecular composition of water is H~2~O."
>>> markdown(text, ['subscript'])
'<p>The molecular composition of water is H<sub>2</sub>O.</p>'

Command Line
^^^^^^^^^^^^

::

    $ echo 'The molecular composition of water is H~2~O.' > text.md
    $ python -m markdown -o html5 -x 'subscript' -f text.html text.md

.. _`Python Markdown`: https://pypi.python.org/pypi/Markdown
.. _`Simplified (2 Clause) BSD license`: http://choosealicense.com/licenses/bsd-2-clause/
