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

def is_alive():
      """
      ... # TODO Add something here
      """
      return self.toughness > 0

    def fight(self, target):
        """
        A simulation of this creature fight with other one.
        This function also be called on the target creature when fight happen.
        If no another creature is set as target in this fight,
        then it prints a message says Need a target.

        Parameters:
            - target : Another creature this one fight with
        """


        self.toughness = self.toughness - target.power
        target.toughness == target.toughness - self.power
