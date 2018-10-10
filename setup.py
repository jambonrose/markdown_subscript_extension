#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Markdown Subscript Extension Setup

:website: https://github.com/jambonrose/markdown_subscript_extension
:copyright: Copyright 2014-2018 Andrew Pinkham
:license: Simplified BSD, see LICENSE for details.
"""

from codecs import open as codec_open
from distutils.command.check import check as CheckCommand  # noqa: N812
from os.path import abspath, dirname, join
from sys import argv

from setuptools import setup

HERE = abspath(dirname(__file__))


def load_file_contents(file_path, as_list=True):
    """Load file as string or list"""
    abs_file_path = join(HERE, file_path)
    with codec_open(abs_file_path, encoding="utf-8") as file_pointer:
        if as_list:
            return file_pointer.read().splitlines()
        return file_pointer.read()


# Get the long description from the Read Me
LONG_DESCRIPTION = (
    load_file_contents("README.rst", as_list=False)
    .split(".. start-pypi-description")[1]  # remove badge icons and title
    .lstrip()  # remove any extraneous spaces before title
)

# Get test dependencies
TESTS_REQUIRE = load_file_contents("requirements/test_requirements.txt")

SETUP_REQUIRES_PYTEST_RUNNER = (
    ["pytest-runner>=4.2,<5"]
    if {"pytest", "test", "ptr"}.intersection(argv)
    else []
)


class CustomCheckCommand(CheckCommand):
    """Customized distutils check command"""

    # https://github.com/python/cpython/blob/master/Lib/distutils/command/check.py
    user_options = CheckCommand.user_options + [
        ("disable-metadata", None, "don't check meta-data"),
        ("enforce-email", "e", "Ensure that all author/maintainer use email"),
    ]
    negative_opt = {"disable-metadata": "metadata"}

    def initialize_options(self):
        """Set new options after superclass"""
        super().initialize_options()
        self.enforce_email = 0  # pylint:disable=attribute-defined-outside-init

    def check_metadata(self):
        """Ensure all required meta-data are supplied.

        Specifically: name, version, URL, author or maintainer
        Warns if any are missing.

        If enforce-email option is true, author and/or maintainer must
        specify an email.

        """
        metadata = self.distribution.metadata

        missing = []
        for attr in ("name", "version", "url"):
            if not (hasattr(metadata, attr) and getattr(metadata, attr)):
                missing.append(attr)

        # https://www.python.org/dev/peps/pep-0345/
        # author or maintainer must be specified
        # author is preferred; if identifcal, specify only author
        if not metadata.author and not metadata.maintainer:
            missing.append("author")
            if self.enforce_email:
                missing.append("author_email")
        else:
            # one or both of author or maintainer specified
            if (
                metadata.author
                and self.enforce_email
                and not metadata.author_email
            ):
                missing.append("author_email")
            if (
                metadata.maintainer
                and self.enforce_email
                and not metadata.maintainer_email
            ):
                missing.append("maintainer_email")
            if (
                metadata.author
                and metadata.maintainer
                and metadata.author == metadata.maintainer
            ):
                self.warn(
                    "Maintainer should be omitted if identical to Author.\n"
                    "See https://www.python.org/dev/peps/pep-0345/"
                    "#maintainer-email-optional"
                )
            if (
                metadata.author_email
                and metadata.maintainer_email
                and metadata.author_email == metadata.maintainer_email
            ):
                self.warn(
                    "Maintainer Email should be omitted if"
                    "identical to Author's.\n"
                    "See https://www.python.org/dev/peps/pep-0345/"
                    "#maintainer-email-optional"
                )

        if missing:
            self.warn("missing required meta-data: %s" % ", ".join(missing))


setup(
    name="MarkdownSubscript",
    version="2.1.1",  # PEP 440 Compliant Semantic Versioning
    keywords=["text", "filter", "markdown", "html", "subscript"],
    description="Python-Markdown extension to allow for subscript text.",
    long_description=LONG_DESCRIPTION,
    author="Andrew Pinkham",
    url="https://github.com/jambonrose/markdown_subscript_extension",
    project_urls={
        "Documentation": (
            "https://markdown-subscript-extension.rtfd.io/en/stable/"
        ),
        "Source": "https://github.com/jambonrose/markdown_subscript_extension",
        "Tracker": (
            "https://github.com/jambonrose/markdown_subscript_extension/issues"
        ),
    },
    cmdclass={"check": CustomCheckCommand},
    py_modules=["mdx_subscript"],
    install_requires=["Markdown>=2.5,<3.1"],
    tests_require=TESTS_REQUIRE,
    setup_requires=SETUP_REQUIRES_PYTEST_RUNNER,
    license="Simplified BSD License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    entry_points={
        "markdown.extensions": ["subscript = mdx_subscript:SubscriptExtension"]
    },
)
