"""Tests for the mana class"""

import ertai
import collections

import pytest


@pytest.mark.parametrize("color", ertai.colors)
def test_initialisation_of_mana_with_single_color(color):
    """
    This is to test that a single color can be passed to the Mana class.
    """
    mana = ertai.Mana(color)
    assert mana.counter == collections.Counter({color: 1})


def test_initialisation_of_mana_with_collection_of_colors():
    """
    This is a test to check that given any selected collection of
    colors the Mana instance generates correctly.
    """
    mana = ertai.Mana("Red", "Blue", "Red", "Red")
    expected_counter = collections.Counter({"Red": 3, "Blue": 1})
    assert mana.counter == expected_counter


def test_initialisation_of_mana_with_no_mana():
    """
    This is to test that a single color can be passed to the Mana class.
    """
    mana = ertai.Mana()
    assert mana.counter == collections.Counter({})


def test_representation_of_mana():
    """
    This tests what a mana blob looks like
    """
    mana = ertai.Mana("Black", "Blue", "Red", "Red")
    assert mana.__repr__() == "1 Black Mana, 1 Blue Mana, 2 Red Mana"


def test_representation_of_no_mana():
    """
    This tests what a mana blob looks like when there is no mana
    """
    mana = ertai.Mana()
    assert mana.__repr__() == "0 Mana"
