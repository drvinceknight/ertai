"""
Class for Mana
"""
from __future__ import annotations
import collections

from typing import Optional


class Mana:
    """A class for collections of Mana."""

    def __init__(self, *colors: Optional[str]) -> None:
        """
        Initialises with any number of colors.

        Mana("Blue")

        Or

        Mana("Blue", "Red", "Blue")
        """
        self.counter = collections.Counter(colors)

    def __repr__(self) -> str:
        """
        The repr method.

        This displays the mana in alphabetical, human readable form.
        """
        if len(self.counter) == 0:
            return "0 Mana"
        return ", ".join(
            f"{count} {color} Mana" for color, count in self.counter.items()
        )

    def __eq__(self, other: object) -> bool:
        """
        The equality method that correspond to checking equality of the
        underlying counter objects.
        """
        if not isinstance(other, Mana):
            return False
        return self.counter == other.counter

    def __add__(self, other: Mana) -> Mana:
        """
        Add mana together
        """
        counter = self.counter + other.counter
        return Mana(*counter.elements())

    def __sub__(self, other: Mana) -> Mana:
        """
        Subtract mana
        """
        counter = self.counter - other.counter
        return Mana(*counter.elements())

    def __le__(self, other: Mana) -> bool:
        """
        This checks if the mana in `self` is contained in the mana in `other`.

        It does this by looping over all keys and counts in self and check if it
        exists in other.
        """
        for key, count in self.counter.items():
            if count > other.counter[key]:
                return False
        return True

    def __ge__(self, other: Mana) -> bool:
        """
        This is the opposite operation to __ge__. Implemented for convenience.
        """
        return other <= self
