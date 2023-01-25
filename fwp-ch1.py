
# Fluent with Python Chapter 1
# The Python Data Model


# a class to represent a deck of playing cards

from math import hypot
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


# illustrate the use of special methods through another example

# start by designing the API

"""
# the abs() function returns the absolute value of integers and floats, and the magnitude of complex numbers
# So our API uses abs to calculate the magnitude of a vector

>>> v = Vector(3, 4)
>>> abs(v)
 5.0

The * operator can be used to perform scalar multiplication (ie multiplying a vector by a 
number to produce a new vector with the same direction and a multiplied magnitude)

>>> v * 3
Vector(9, 12)
>>> abs(v * 3)
15.0
"""

# Vector class implementing the operations described by use of special methods:
# __repr__, __abs__, __add__, __mul:


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector (%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v = Vector(3, 4)
abs(v)
print(v * 3)
# Vector(9, 12)
print(abs(v * 3))
# 15.0

"""
String representation

The __repr__ method is called by the repr built-in to get string representations of the
object for inspection. If we didn't implement __repr__, vector instances would be shown
in console like <Vector object at 0x10e100070>

using %r to obtain the standard representation of the attr. displayed is good practice bc
it shows the crucual difference between Vector(1, 2) and Vector('1', '2'), the latter wouldn't
have worked because the constructor args need to be numbers not str.

Choose __repr__ over __str__ because when no custom string is available, Python will call __repr__ 
as a fallback
"""

"""
Arithmetic operators

The Vector example uses two operators + and * to show basic usage of __add__ and __mul__
In both examples, the methods create and return new instances of Vector and don't modify either
Self and other are merely read.

This is expected behavior of infix operators - to create new objects and not touch their operands
"""

"""
Bool value of a custom type

The implementation of __bool__ is conceptually simple - it returns False if the magnitude
of Vector is zero, True otherwise 

A faster implementation of Vector.__bool__ is:

def __bool__(self):
    return bool(self.x or self.y)

Harder to read but avoids the trip through __abs__  The conversion to bool is needed
because __bool__ must return a boolean and or returns either operand as is: x or y evaluates 
to x if that is truthy


"""
