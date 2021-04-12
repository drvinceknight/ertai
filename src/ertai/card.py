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

    def tap(self):
        """A method to tap a card"""
        self.tapped = True

    def untap(self):
        """A method to untap a card"""
        self.tapped = False
