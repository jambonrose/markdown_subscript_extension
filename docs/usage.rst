=====
Usage
=====

.. contents::
    :local:

Python
------

.. code-block:: pycon

    >>> from markdown import markdown
    >>> from mdx_subscript import SubscriptExtension
    >>> text = "The molecular composition of water is H~2~O."
    >>> markdown(text, extensions=[SubscriptExtension()])
    '<p>The molecular composition of water is H<sub>2</sub>O.</p>'

You may also refer to the extension by module name or short module name.

.. code-block:: pycon

    >>> markdown(text, extensions=['mdx_subscript'])
    >>> markdown(text, extensions=['subscript'])

.. NOTE::
    In older versions of Markdown, you will need to refer to the module
    without the ``mdx`` prefix (the second line of code above).

Command Line
------------

.. code-block:: console

    $ echo 'The molecular composition of water is H~2~O.' > text.md
    $ python -m markdown -o html -x 'mdx_subscript' -f text.html text.md
    $ cat text.html
    <p>The molecular composition of water is H<sub>2</sub>O.</p>
