"""Tests for the card class"""

import ertai


def test_base_card_class_has_expected_attributes_and_defaults():
    """
    This is a test to check that the base card class has the attributes
    expected and the defaults expected.
    """
    card = ertai.Card()
    assert card.title is None
    assert card.cost == ertai.Mana()
    assert card.tapped is False


def test_base_card_class_takes_expected_attribute_on_init():
    """
    This is a test to check that the base card class initialises as expected
    """
    card = ertai.Card(title="Island")
    assert card.title == "Island"
    assert card.cost == ertai.Mana()
    assert card.tapped is False


def test_base_card_class_taps():
    """
    This is a test to check the `tap` method works.
    """
    card = ertai.Card()
    assert card.tapped is False
    card.tap()
    assert card.tapped is True
    card.untap()
    assert card.tapped is False


def test_base_card_class_can_be_cast_when_given_sufficient_mana():
    """
    Test that a card can be cast given a mana pool.

    If there is sufficient Mana in the pool it will update the mana pool.
    """
    pool = ertai.Mana("Blue", "Blue", "Red")
    counter_spell = ertai.Card(title="Counter Spell", cost=ertai.Mana("Blue", "Blue"))
    assert counter_spell.cast(pool=pool) == ertai.Mana("Red")


def test_base_card_class_can_be_cast_when_not_given_sufficient_mana():
    """
    Test that a card cannot be cast given a mana pool.
    """
    pool = ertai.Mana("Blue", "Red", "Red")
    counter_spell = ertai.Card(title="Counter Spell", cost=ertai.Mana("Blue", "Blue"))
    assert counter_spell.cast(pool=pool) == pool
