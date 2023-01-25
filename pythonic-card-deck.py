
# a class to represent a deck of playing cards

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(deck[0])
print(deck[-1])

# to pick a random card - python already has a function to get random item

from random import choice
print(choice(deck))

# our deck automatically supports slicing
print("The deck supports slicing")
print(deck[:3])
print(deck[12::13])

# because we implemented __getitem__, the deck is also iterable
print("Iterability of the deck")
for card in deck:
    print(card)

# iterability in reverse...
print("reverse iterability")
for card in reversed(deck):
    print(card)

# boolean
print("The 'in' operator does a scan and acts as a bool")
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# Sorting - below is a function that ranks cards by the rule we provide in 'suit_values'
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)