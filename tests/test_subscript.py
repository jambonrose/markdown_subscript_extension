# -*- coding: utf-8 -*-
"""Markdown Subscript Extension Tests

:website: https://github.com/jambonrose/markdown_subscript_extension
:copyright: Copyright 2014-2018 Andrew Pinkham
:license: BSD, see LICENSE for details.

"""
from __future__ import unicode_literals

from markdown import markdown, version_info as md_version
from mdx_subscript import SubscriptExtension
from pytest import fixture, mark, param

TEXT_DATA_FIELDS = "markdown_text, expected_html"
TEXT_DATA = [
    param(
        "Water is written as H~2~O in chemistry.",
        "<p>Water is written as H<sub>2</sub>O in chemistry.</p>",
        id="Simple substitution",
    ),
    param(
        "Caffeine is C~8~H~10~N~4~O~2~.",
        (
            "<p>Caffeine is "
            "C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>"
            ".</p>"
        ),
        id="Multiple substitutions",
    ),
]


@fixture(
    scope="session",
    params=[
        param([SubscriptExtension()], id="Direct Extension"),
        param(
            ["mdx_subscript"],
            marks=mark.skipif(
                md_version < (2, 6),
                reason="Module matching by full name added in Markdown 2.6",
            ),
            id="Full module name",
        ),
        param(["subscript"], id="Short module name"),
    ],
)
def extensions(request):
    """Parameterized Fixture for extensions kwarg of markdown"""
    return request.param


@mark.parametrize(TEXT_DATA_FIELDS, TEXT_DATA)
def test_subscript_extension(markdown_text, expected_html, extensions):
    """Test the subscript extensions

    PyTest parameterized arguments allow for multiple text inputs to be
    tested.

    The Markdown package allows for extensions to be requested in a
    number of ways. We use a PyTest parameterized fixture to test each
    of those methods.

    We are therefore testing multiple text inputs in multiple
    extension-loading scenarios.

    """
    result = markdown(markdown_text, extensions=extensions)
    assert result == expected_html
