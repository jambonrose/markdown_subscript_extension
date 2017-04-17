#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==================================
Markdown Subscript Extension Setup
==================================

:website: https://github.com/jambonrose/markdown_subscript_extension
:copyright: Copyright 2014-2017 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""

from setuptools import setup
from codecs import open as codec_open
from os import path


HERE = path.abspath(path.dirname(__file__))


# Get the long description from the Read Me
with codec_open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

# Get runtime dependencies
run_reqs = 'requirements/run_requirements.txt'
with codec_open(path.join(HERE, run_reqs), encoding='utf-8') as f:
    install_requires = f.read().splitlines()

# Get test dependencies
test_reqs = 'requirements/test_requirements.txt'
with codec_open(path.join(HERE, test_reqs), encoding='utf-8') as f:
    tests_require = f.read().splitlines()


setup(
    name='MarkdownSubscript',

    version='2.0.0',  # PEP 440 Compliant Semantic Versioning

    keywords=['text', 'filter', 'markdown', 'html', 'subscript'],
    description='Python-Markdown extension to allow for subscript text.',
    long_description=long_description,

    author='Andrew Pinkham',
    author_email='hello at andrewsforge dot com',

    url='https://github.com/jambonrose/markdown_subscript_extension',

    py_modules=['mdx_subscript'],
    install_requires=install_requires,
    test_suite='tests',
    tests_require=tests_require,

    license='Simplified BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
