=====
Usage
=====

Python
------

.. code :: pycon

    >>> from markdown import markdown
    >>> text = "The molecular composition of water is H~2~O."
    >>> markdown(text, ['subscript'])
    '<p>The molecular composition of water is H<sub>2</sub>O.</p>'

Command Line
------------

.. code :: bash

    $ echo 'The molecular composition of water is H~2~O.' > text.md
    $ python -m markdown -o html5 -x 'subscript' -f text.html text.md
