# Markdown Subscript

[![Build Status](https://travis-ci.org/jambonrose/markdown_subscript_extension.svg?branch=master)](https://travis-ci.org/jambonrose/markdown_subscript_extension)
[![Coverage Status](https://img.shields.io/coveralls/jambonrose/markdown_subscript_extension.svg)](https://coveralls.io/r/jambonrose/markdown_subscript_extension)
[![Requirements Status](https://requires.io/github/jambonrose/markdown_subscript_extension/requirements.svg?branch=master)](https://requires.io/github/jambonrose/markdown_subscript_extension/requirements/?branch=master)
[![PyPI Version](http://img.shields.io/pypi/v/MarkdownSubscript.svg)](https://pypi.python.org/pypi/MarkdownSubscript/)

[![Python Implementation Support](https://img.shields.io/pypi/implementation/MarkdownSubscript.svg)](https://pypi.python.org/pypi/MarkdownSubscript/)
[![Python Support](https://img.shields.io/pypi/pyversions/MarkdownSubscript.svg)](https://pypi.python.org/pypi/MarkdownSubscript/)
[![License](http://img.shields.io/pypi/l/MarkdownSubscript.svg)](http://opensource.org/licenses/BSD-2-Clause)

An extension to [Waylan Limberg](https://github.com/waylan)'s [Python Markdown](https://github.com/waylan/Python-Markdown) project ([documentation here](https://pythonhosted.org/Markdown/index.html)) that provides support for subscript text in Markdown. The extension treats `~` characters as tags, converting pairs into HTML `sub` tags.

Given the text:

    The molecular composition of water is H~2~O.

… using Markdown with this extension will output:

    <p>The molecular composition of water is H<sub>2</sub>O.</p>

This project is provided under the [Simplified (2 Clause) BSD license](http://choosealicense.com/licenses/bsd-2-clause/), provided in full in the LICENSE file.

## Installation

Dependencies:

- Python 2.7, 3.3+
- Markdown 2.5+
  (Tested against latest patch version of Markdown 2.5 and 2.6)

To install the latest stable release (recommended):

```bash
$ pip install MarkdownSubscript
```

To install the development version:

```bash
$ pip install git+git://github.com/jambonrose/markdown_subscript_extension.git
```

## Basic Usage

### Python

```python
>>> from markdown import markdown
>>> text = "The molecular composition of water is H~2~O."
>>> markdown(text, ['subscript'])
'<p>The molecular composition of water is H<sub>2</sub>O.</p>'
```

### Command Line

```bash
$ echo 'The molecular composition of water is H~2~O.' > text.md
$ python -m markdown -o html5 -x 'subscript' -f text.html text.md
```

## Development

Development requires the installation of [Python](https://www.python.org/) and [Pip](https://pip.pypa.io/en/latest/installing.html). A virtual environment, such as [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) (used in the example below), is recommended. Once these are installed, the following steps may be taken:

```bash
$ git clone https://github.com/jambonrose/markdown_subscript_extension.git
$ cd markdown_subscript_extension/
$ mkvirtualenv markdown_subcript  # recommended, but optional
$ cat requirements/* > requirements.txt
$ pip install -r requirements.txt
```

The `Makefile` provides the ability to run tests by invoking `$ make test`, which will invoke the nose package with the command `$ nosetests --with-coverage --cover-package=mdx_subscript` (incidentally, this is also the command used on [TravisCI](https://travis-ci.org/jambonrose/markdown_subscript_extension) and [Coveralls.io](https://coveralls.io/r/jambonrose/markdown_subscript_extension)).

Additionally, provided you have all of the proper Python
implementations/versions installed, it is possible to use `tox` to test
multiple environments by invoking `tox` on the commandline (no arguments
required).
