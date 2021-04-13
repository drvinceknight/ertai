"""
Class for Mana
"""
import collections


class Mana:
    """A class for collections of Mana."""

    def __init__(self, *colors: str) -> None:
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
