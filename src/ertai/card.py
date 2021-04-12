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
