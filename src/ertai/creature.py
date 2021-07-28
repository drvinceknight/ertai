"""
Class for Creature
"""

from .card import Card
from dataclasses import dataclass


@dataclass(repr=False)
class Creature(Card):
    """
    A base class for creatures.

    Initiate this creature by passing power and toughness.

    Parameters:
        - power : power  of this creature
        - toughness : Toughness value of this creature,
                but this value can be modified in a fight or other condition
        - base_toughness : Toughness value of this creature,
                use to store the base toughness of this creature.
        - is_alive : A bool value represent wether this creature is alive.
    """

    power: int = 0
    toughness: int = 0
    is_alive: bool = True

    def __post_init__(self):
        """
        Set base_toughness to record the base toughness
        this creature has. It can be used after a fight
        to recover this creature's toughness to default value
        if this creature is alive after fighting.
        """
        self.base_toughness = self.toughness

    def __repr__(self):
        """
        This is used to print the information about this creature.
        """
        return (
            self.title
            + "    Cost:"
            + str(self.cost)
            + "    Power:"
            + str(self.power)
            + "    Toughness:"
            + str(self.toughness)
        )

    def check_state(self):
        """
        This function is used after a attack happended.
        If the toughness of this creature drop down to 0 or less,
        then we set it's state to False which means that this creature is died.
        """
        if self.toughness <= 0:
            self.is_alive = False
        else:
            self.toughness = self.base_toughness

    def fight(self, target):
        """
        A simulation of this creature fight with other one.
        This function also be called on the target creature when fight happen.
        If no another creature is set as target in this fight,
        then it prints a message says Need a target.

        Parameters:
            - target : Another creature this one fight with
        """

        if target is None:
            print("Need a target")

        else:
            self.toughness = self.toughness - target.power
            self.check_state()
