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
