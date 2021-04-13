"""
Classes for cards
"""
from dataclasses import dataclass


from typing import Union


@dataclass
class Card:
    """A class for a base card."""

    title: Union[str, None] = None
    cost: int = 0
    tapped: bool = False

    def tap(self) -> None:
        """A method to tap a card"""
        self.tapped = True

    def untap(self) -> None:
        """A method to untap a card"""
        self.tapped = False


@dataclass
class BasicLand(Card):
    """
    A class for a basic land.

    Can be tapped to add mana to a mana pool.
    """

    color: Union[str, None] = None

    def generate_mana(self) -> Union[str, None]:
        """
        Tap a given land card to create mana of the given color.
        """
        if self.tapped is False:
            self.tap()
            return self.color
        return None
