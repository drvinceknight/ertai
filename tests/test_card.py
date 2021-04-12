"""Tests for the card class"""

import ertai


def test_base_card_class_has_expected_attributes_and_defaults():
    """
    This is a test to check that the base card class has the attributes
    expected and the defaults expected.
    """
    card = ertai.Card()
    assert card.title is None
    assert card.cost == 0


def test_base_card_class_initialises():
    """
    This is a test to check that the base card class initialises as expected
    """
    card = ertai.Card(title="Island")
    assert card.title == "Island"
    assert card.cost == 0
