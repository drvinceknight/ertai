"""
Tests for Creatures.
"""


import ertai


def test_creature_takes_expected_attribute_on_init():
    """
    This is a test to check wether the
    full-attributes initialisation is working.
    """
    creature = ertai.Creature(
        title="Selfless Savior",
        cost=ertai.Mana("White"),
        tapped=False,
        power=1,
        toughness=1,
    )

    assert creature.title == "Selfless Savior"
    assert creature.cost == ertai.Mana("White")
    assert creature.tapped is False
    assert creature.power == 1
    assert creature.toughness == 1
    assert creature.base_toughness == 1
    assert creature.is_alive() is True


def test_creature_fight():
    """
    Tests the situation when a fight happend bewteen two creatures.
    """
    my_creature_1 = ertai.Creature(
        title="Selfless Savior",
        cost=ertai.Mana("White"),
        power=1,
        toughness=1,
    )

    my_creature_2 = ertai.Creature(
        title="Usher of the Fallen",
        cost=ertai.Mana("White"),
        power=2,
        toughness=2,
    )

    target_creature = ertai.Creature(
        title="Wall of Runes",
        cost=ertai.Mana("Blue"),
        tapped=False,
        power=0,
        toughness=4,
    )

    my_creature_1.fight(my_creature_2)
    my_creature_2.fight(target_creature)

    assert my_creature_1.is_alive() is False
    assert my_creature_2.is_alive() is True
    assert my_creature_1.toughness == -1
    assert my_creature_2.toughness == 1
    assert target_creature.toughness == 2
