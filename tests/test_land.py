"""Tests for the land class"""

import ertai


def test_land_initialisation():
    """
    For all colors test that lands have given color and enter untapped.
    """
    for color in ertai.colors:
        card = ertai.BasicLand(color=color)
        assert card.color == color
        assert card.tapped is False


def test_land_can_add_mana_of_given_color_if_untapped():
    """
    For all colors test that lands can give required color.
    """
    for color in ertai.colors:
        card = ertai.BasicLand(color=color)
        assert card.generate_mana() == ertai.Mana(color)
        assert card.tapped is True


def test_land_cannot_add_mana_of_given_color_if_tapped():
    """
    For all colors test that lands cannot give mana if tapped.
    """
    for color in ertai.colors:
        card = ertai.BasicLand(color=color)
        card.tap()
        assert card.generate_mana() is None
        assert card.tapped is True
