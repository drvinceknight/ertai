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
    This is to test that no color can be passed to the Mana class.
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


def test_equality_of_mana_when_they_are_equal():
    """
    Test the quality method on Mana. Here the Mana is created with the strings in
    a different order but they are the same.
    """
    mana = ertai.Mana("Black", "Blue", "Red", "Red")
    other_mana = ertai.Mana("Black", "Red", "Red", "Blue")
    assert mana == other_mana


def test_equality_of_mana_when_they_are_not_equal():
    """
    Test the quality method on Mana. Here the Mana is created with different
    strings.
    """
    mana = ertai.Mana("Black", "Blue", "Red", "Red")
    other_mana = ertai.Mana("Black", "Blue", "Red")
    assert mana != other_mana


def test_equality_of_mana_when_not_comparing_the_same_objects():
    """
    Test the quality method on Mana. Here the Mana is compared to a string.
    """
    mana = ertai.Mana("Black", "Blue", "Red", "Red")
    assert mana != "A string"


def test_addition_of_mana():
    """
    This tests that mana can be added to other mana.
    """
    pool = ertai.Mana("Black", "Blue", "Red", "Red")
    mana_from_land = ertai.Mana("Black")
    pool += mana_from_land
    assert pool.counter == collections.Counter({"Black": 2, "Blue": 1, "Red": 2})


def test_subtraction_of_mana():
    """
    This tests that mana can be taken from a pool
    """
    pool = ertai.Mana("Black", "Blue", "Red", "Red")
    mana_for_spell = ertai.Mana("Black", "Red")
    pool -= mana_for_spell
    assert pool.counter == collections.Counter({"Blue": 1, "Red": 1})


def test_comparisons_of_mana_quantity_when_true():
    """
    This tests if Mana from one quantity is less than another.
    """
    pool = ertai.Mana("Black", "Blue", "Red", "Red")
    mana_for_spell = ertai.Mana("Black", "Red")
    assert mana_for_spell <= pool
    assert pool >= mana_for_spell


def test_comparisons_of_mana_quantity_when_false():
    """
    This tests if Mana from one quantity less than another is False when there
    is not sufficient Mana.
    """
    pool = ertai.Mana("Black", "Blue", "Red", "Red")
    mana_for_spell = ertai.Mana("Black", "Red", "White")
    assert (mana_for_spell <= pool) is False
    assert (pool >= mana_for_spell) is False
