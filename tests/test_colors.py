"""
Tests for the colors.

Currently this is implemented as a tuples of strings.
"""

import ertai


def test_colors_are_as_expected():
    """
    This is a basic test to check that the colors are as given.
    """
    expected_colors = ("Blue", "Red", "Black", "White", "Green")
    assert ertai.colors == expected_colors
