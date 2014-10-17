#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
==================================
Markdown Subscript Extension Setup
==================================

:website: https://github.com/jambonrose/markdown_subscript_extension
:copyright: Copyright 2014 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""

from setuptools import setup
from codecs import open as codec_open
from os import path


HERE = path.abspath(path.dirname(__file__))


# Get the long description from the relevant file
with codec_open(path.join(HERE, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()


setup(
    name='MarkdownSubscript',

    version='1.0.1',  # PEP 440 Compliant Semantic Versioning

    keywords='text filter markdown html subscript',
    description='Python-Markdown extension to allow for subscript text.',
    long_description=LONG_DESCRIPTION,

    author='Andrew Pinkham',
    author_email='hello at andrewsforge dot com',

    url='https://github.com/jambonrose/markdown_subscript_extension',

    py_modules=['mdx_subscript'],
    install_requires=['Markdown>=2.4'],

    license='Simplified BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)
