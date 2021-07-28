# Ertai

Mathematical models of Magic the Gathering.

## Tutorial

We will use `ertai` to obtain the probability of being able to play a card in
our first turn.

```python
>>> import ertai
>>> import random
>>> def build_deck(card_counts, number_of_lands):
...     """
...     This returns a list of `ertai.Card` objects with the
...     specified number of cards
...     """
...     deck = [ertai.BasicLand() for _ in range(number_of_lands)]
...     for cost, number in card_counts.items():
...         cost = ertai.Mana(*(None for _ in range(cost)))
...         deck += [ertai.Card(cost=cost) for _ in range(number)]
...     return deck
>>> card_counts = {1: 10, 2: 16}
>>> number_of_lands = 14
>>> deck = build_deck(card_counts=card_counts, number_of_lands=number_of_lands)
>>> for card in deck:
...     print(card)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
BasicLand(title=None, cost=0 Mana, tapped=False, color=None)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=1 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)
Card(title=None, cost=2 None Mana, tapped=False)

```

The above is code that uses the `ertai` classes to construct a deck.

Now let us write code to find the probability of drawing a hand with a card that
can be played.

```
>>> def play_land(hand):
...     """
...     If the hand contains a land, return it.
...     """
...     for card in hand:
...          if isinstance(card, ertai.BasicLand):
...              hand.remove(card)
...              return card
...     return None
>>> def play_card(hand, pool):
...     """
...     Given a pool of mana, play the first possible card in a hand.
...     """
...     for card in hand:
...         if (card.cost <= pool) and (isinstance(card, ertai.BasicLand) is False):
...             pool = card.cast(pool)
...             hand.remove(card)
...             return card
...     return None

```

With the above we can now write code to draw a hand of card and see if we can
play:

```
>>> def can_play_spell(card_counts, number_of_lands, seed):
...     """
...     Given a hand returns a boolean if we are able to play a spell
...
...     This assumes we play on the first turn.
...     """
...     deck = build_deck(card_counts=card_counts, number_of_lands=number_of_lands)
...     random.seed(seed)
...     random.shuffle(deck)
...     hand = deck[:7]
...     if (land:=play_land(hand)) is not None:
...         pool = land.generate_mana()
...         return play_card(hand, pool) is not None
...     return False
>>> can_play_spell(card_counts=card_counts, number_of_lands=number_of_lands, seed=0)
True

```

The above is a single simulation, let us compute the expected probability:

```python
>>> import numpy as np
>>> def expected_probability_of_first_turn_play(card_counts, number_of_lands, number_of_repetitions=500):
...     """Returns the expected probability of having a first turn play."""
...     return np.mean([can_play_spell(card_counts=card_counts, number_of_lands=number_of_lands, seed=seed) for seed in range(number_of_repetitions)])

```

Let us see how this probability changes as we modify the number of cards with
cost 1 in our deck. We will assume a 40 card deck with 16 lands and all other
cards have cost 2.

```python
>>> number_of_lands = 14
>>> for number_of_cards_with_cost_1 in range(1, 26 + 1):
...     card_counts = {1: number_of_cards_with_cost_1, 2: 26 - number_of_cards_with_cost_1}
...     probability = expected_probability_of_first_turn_play(card_counts=card_counts, number_of_lands=number_of_lands)
...     print(number_of_cards_with_cost_1, round(probability, 3))
1 0.134
2 0.286
3 0.422
4 0.504
5 0.58
6 0.644
7 0.714
8 0.762
9 0.796
10 0.838
11 0.862
12 0.88
13 0.898
14 0.914
15 0.932
16 0.946
17 0.948
18 0.95
19 0.954
20 0.958
21 0.958
22 0.958
23 0.958
24 0.958
25 0.958
26 0.958

```

We see that as expected the probability of playing in the first turn goes up as
the number of cards with cost 1 increases.

## How to

### How to create mana

`ertai` has a mana class that can be used to create any amount of mana.

```python
>>> spell_cost = ertai.Mana("Blue", "Blue")
>>> spell_cost
2 Blue Mana

```

### How to add more mana

```python
>>> spell_cost += ertai.Mana("Red")
>>> spell_cost
2 Blue Mana, 1 Red Mana

```

### How to check if one collection of mana can be paid using another

```python
>>> mana_pool = ertai.Mana("Blue", "Red", "Red", "Blue")
>>> spell_cost <= mana_pool
True

```

### How to take one collection of mana away from another

```python
>>> mana_pool -= spell_cost
>>> mana_pool
1 Red Mana

```

We see that we no longer have enough mana for the spell:

```python
>>> spell_cost <= mana_pool
False

```

### How to create a basic land

```python
>>> island = ertai.BasicLand(title="Island", color="Blue")
>>> island
BasicLand(title='Island', cost=0 Mana, tapped=False, color='Blue')

```

### How to generate mana from a land

```python
>>> island.tapped
False
>>> island.generate_mana()
1 Blue Mana
>>> island.tapped
True

```

When tapped the land will not generate mana.

```python
>>> island.generate_mana()

```

### How to untap or tap a card

All cards in `ertai` have a `untap` method.

```python
>>> island.untap()
>>> island.tapped
False

```

They also have a `tap` method.

```python
>>> island.tap()
>>> island.tapped
True

```

### How to cast a card

At present, casting a card does nothing but modify a given mana pool **if the
cost can be paid**.

```python
>>> mana_pool = ertai.Mana("Red", "Red", "Black")
>>> card_cost = ertai.Mana("Red")
>>> card = ertai.Card(title="Lightning bolt", cost=card_cost)
>>> mana_pool = card.cast(mana_pool)
>>> mana_pool
1 Red Mana, 1 Black Mana

```

Note that if a card cannot be case then the mana pool will stay unchanged but no
warning is given.

```python
>>> card_cost = ertai.Mana("Blue", "Blue")
>>> card = ertai.Card(title="Counterspell", cost=card_cost)
>>> mana_pool = card.cast(mana_pool)
>>> mana_pool
1 Red Mana, 1 Black Mana

```

### How to create a ceature card

Pass a `power` and `toughness` to the `Creature` class:

```python
>>> creature = ertai.Creature(title="Selfless Savior",cost=ertai.Mana("White"),
...            power=1,
...            toughness=1)
>>> creature
Selfless Savior    Cost:1 White Mana    Power:1    Toughness:1

```

### How to use a creature to fight 

We can then use this creature to fight a `target` create:

```python
>>> target = ertai.Creature(title="Usher of the Fallen",cost=ertai.Mana("White"),
...          power=2,
...          toughness=1)
>>> creature.fight(target)

```

In this case the create is no longer alive after the fight:

```python
>>> creature.is_alive()
False

```

### How to contribute

Clone the repository and create a virtual environment:

```bash
$ git clone https://github.com/drvinceknight/ertai.git
$ cd ertai
$ python -m venv env

```

Activate the virtual environment and install [`tox`](https://tox.readthedocs.io/en/latest/):

```bash
$ source env/bin/activate
$ python -m pip install tox

```

Make modifications.

To run the tests:

```bash
$ python -m tox

```

Pull requests are welcome.


## Discussion

### What is Magic The Gathering

Magic the Gathering is a collectable card game that was first released in 1993.

- Here is the official basic rules:
  [https://magic.wizards.com/en/magic-gameplay](https://magic.wizards.com/en/magic-gameplay)
- Here is the wikipedia page entry: [https://en.wikipedia.org/wiki/Magic:_The_Gathering](https://en.wikipedia.org/wiki/Magic:_The_Gathering)

### Why is it called Ertai

Alongside the game there is a lot of lore that exists. Ertai was a particular
character. From [https://villains.fandom.com/wiki/Ertai]:

> He is a brilliant but arrogant mage who learned from the head wizard of the
> Tolarian Academy Barrin and signed up to join the Weatherlight Crew.

### What can this library be used for

At present this library offers data class that can be used to model aspects of
Magic the Gathering.

The `erta.Mana` class allows us to carry out Mana arithmetic:

```
>>> mana_pool = ertai.Mana("Blue", "Blue", "Red", "None", "Blue")
>>> ertai_the_adept_cost = ertai.Mana("Blue", "Blue", "None")
>>> mana_pool - ertai_the_adept_cost
1 Blue Mana, 1 Red Mana

```

The `ertai.Card` class can be used to create new cards with given abilities.

### Development stack

There are a number of continuous integration checks that are used:

- [black](https://github.com/psf/black) and
  [flake8](https://flake8.pycqa.org/en/latest/) for code style.
- [interrogate](https://interrogate.readthedocs.io/en/latest/) to ensure all
  code has docstrings.
- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking.
- [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) to ensure 100%
  coverage of source code by test.
- [mccabe](https://github.com/PyCQA/mccabe) to measure code complexity.

[tox](https://tox.readthedocs.io/en/latest/) is used to test the code in isolated environments.

## Reference

### Other Python magic the gathering libraries

[Magic: The Gathering SDK](https://github.com/MagicTheGathering/mtg-sdk-python):
A wrapper around the MTG API of magicthegathering.io
