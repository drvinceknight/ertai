"""
Tests for Creatures.
"""


import ertai


def test_creature_has_expected_attributes_and_defaults():
    """
    This is a test to check the no-arguments
    initialised creature has all the attributes we expected.
    """
    creature = ertai.Creature()

    assert creature.title is None
    assert creature.cost == ertai.Mana()
    assert creature.tapped is False
    assert creature.power == 0
    assert creature.toughness == 0
    assert creature.base_toughness == 0


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


def test_creature_attack():
    """
    Tests the situation when a fight happend bewteen two creatures.
    """
    my_creature_1 = ertai.Creature(
        title="Selfless Savior",
        cost=ertai.Mana("White"),
        tapped=False,
        power=1,
        toughness=1,
    )

    my_creature_2 = ertai.Creature(
        title="Usher of the Fallen",
        cost=ertai.Mana("White"),
        tapped=False,
        power=2,
        toughness=2,
    )

    target_creature = ertai.Creature(
        title="Wall of Runes",
        cost=ertai.Mana("Blue"),
        tapped=False,
        power=1,
        toughness=4,
    )

    damage_to_player_1 = my_creature_1.attack(my_creature_2)
    damage_to_player_2 = my_creature_2.attack(target_creature)

    assert damage_to_player_1 == 0
    assert damage_to_player_2 == 0
    assert my_creature_1.state is False
    assert my_creature_2.state is True

    target_creature.tap()
    tapped_test = target_creature.attack(my_creature_1)
    assert tapped_test == 0

    target_creature.untap()
    direct_damage = target_creature.attack(None)
    assert direct_damage == 1
