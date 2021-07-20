"""
Class for Creature
"""

from .card import Card
from .mana import Mana


class Creature(Card):
    """
    A class for basic creatures.
    """

    def __init__(
        self,
        title=None,
        cost=Mana(),
        tapped=False,
        power=0,
        toughness=0,
    ):
        """
        Initiate this creature by giving power, toughness of it.

        Other basic information below of this Creature derived from Card:

        title : title of this creature

        cost : cost to cast this creature

        tapped : tap information of this creature

        Parameters:
            - power : power  of this creature
            - toughness : Toughness value of this creature,
                but this value can be modified in a fight or other condition
            - base_toughness : Toughness value of this creature,
                use to store the base toughness of this creature
        """

        Card.__init__(self, title, cost, tapped)

        self.power = power
        self.toughness = toughness
        self.base_toughness = toughness
        self.state = True

    def __repr__(self):
        """
        This is used to print the information about this creature.
        """
        return (
            self.title
            + "\t Cost:"
            + str(self.cost)
            + "\t Power:"
            + str(self.power)
            + "\t Toughness:"
            + str(self.toughness)
        )

    def check_state(self):
        """
        This function is used after a attack happended.
        If the toughness of this creature drop down to 0 or less,
        then we set it's state to False which means that this creature is died.
        """
        if self.toughness <= 0:
            self.state = False
        else:
            self.toughness = self.base_toughness

    def attack(self, target) -> int:
        """
        A simulation of this creature fight with other one.
        This function also be called on the target creature when fight happen.
        It returns a int value represent the damage opponent player taken.
        Also,if no Creature block this attack from this creature,
        then the opponent would take the damage
        as this creature's power value

        Parameters:
            - target : Another creature this one fight with
        """

        if self.tapped is True:
            return 0

        if not target:
            return self.power
        else:
            self.toughness = self.toughness - target.power
            self.check_state()
        self.tap()

        return 0
