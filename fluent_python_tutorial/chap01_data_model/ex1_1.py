import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])
print(type(Card), Card, dir(Card))

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
print(ranks)
suits = 'spades diamonds clubs hearts'.split()
print(suits)

card_list = [Card(rank, suit) for suit in suits
             for rank in ranks]

print(card_list)

# 구구단 예제
[print("{} * {} = {}".format(dan, i, dan * i)) for dan in range(2, 10) for i in range(1, 10)]


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck), deck[0], deck[-1])

    # 임의의카드 선택하기
    from random import choice

    print("choice(deck)", choice(deck), sep='\n')

    print(deck[:3], deck[12::13], sep='\n')

    # __getitem__을 구현함으써 iterator할 수 있다.
    for card in deck: # doctest: +ELLIPSIS
        print(card)
    print()
    [print(card) for card in reversed(deck)]

    print(Card('Q', 'hearts') in deck, Card('Q', 'beasts') in deck)

    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    print(type(suit_values), suit_values, sep='\n')

    [print(card) for card in sorted(deck, key=spades_high)]


"""
Point = collections.namedtuple('Point', ['x', 'y'])
print("Point.__doc__", Point.__doc__, sep='\n')                   # docstring for the new class

p = Point(11, y=22)             # instantiate with positional args or keywords
print("p[0] + p[1]", p[0] + p[1], sep='\n')                     # indexable like a plain tuple

x, y = p                        # unpack like a regular tuple
print(x, y)

print(p.x + p.y)                      # fields also accessible by name
d = p._asdict()                 # convert to a dictionary
print("d['x']", d['x'], sep='\n')

Point(**d)                      # convert from a dictionary
Point(x=11, y=22)
p._replace(x=100)               # _replace() is like str.replace() but targets named fields
Point(x=100, y=22)
"""
