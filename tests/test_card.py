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
    assert card.tapped is False


def test_base_card_class_takes_expected_attribute_on_init():
    """
    This is a test to check that the base card class initialises as expected
    """
    card = ertai.Card(title="Island")
    assert card.title == "Island"
    assert card.cost == 0
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


def test_land_initialisation():
    """
    For all colors test that lands have given color and enter untapped.
    """
    for color in ertai.colors:
        card = ertai.BasicLand(color=color)  # TODO Add color class
        assert card.color == color
        assert card.tapped is False


def test_land_can_add_mana_of_given_color_if_untapped():
    """
    For all colors test that lands can give required color.
    """
    for color in ertai.colors:
        card = ertai.BasicLand(color=color)  # TODO Add color class
        assert card.generate_mana() == color
        assert card.tapped is True


def test_land_cannot_add_mana_of_given_color_if_tapped():
    """
    For all colors test that lands cannot give mana if tapped.
    """
    for color in ertai.colors:
        card = ertai.BasicLand(color=color)  # TODO Add color class
        card.tap()
        assert card.generate_mana() is None
        assert card.tapped is True
