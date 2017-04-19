========
Overview
========

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
