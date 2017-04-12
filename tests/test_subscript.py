# -*- coding: utf-8 -*-
"""
==================================
Markdown Subscript Extension Tests
==================================

:website: https://github.com/jambonrose/markdown_subscript_extension
:copyright: Copyright 2014-2017 Andrew Pinkham
:license: BSD, see LICENSE for details.
"""

from __future__ import unicode_literals
import unittest
from markdown import markdown


class SubscriptTest(unittest.TestCase):
    """Basic functional tests for correct extension behavior."""

    def test_simple_string(self):
        """Basic use case."""
        text = "The molecular composition of water is H~2~O."
        expected = ("<p>The molecular composition of water "
                    "is H<sub>2</sub>O.</p>")
        result = markdown(text, ['subscript'])
        self.assertEqual(expected, result)

    def test_multiple(self):
        """Test mutliple matches."""
        text = "Caffeine is represented as C~8~H~10~N~4~O~2~."
        expected = ("<p>Caffeine is represented as "
                    "C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>"
                    ".</p>")
        result = markdown(text, ['subscript'])
        self.assertEqual(expected, result)
