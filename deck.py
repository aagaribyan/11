from random import shuffle as rd_shuffle
from card import Card
from itertools import product
from consts import SUITS, VALUES, CARD_SIZE


# Колода
class Deck(object):
    def __init__(self):
        self.cards = []

    # тасовка карт
    def shuffle(self, times=1):
        for i in range(times):
            rd_shuffle(self.cards)

    # взятие карты из колоды
    def deal(self):
        return self.cards.pop(0)


# Колода для игры в 11
class Deck11(Deck):
    def __init__(self):
        Deck.__init__(self)

        # создание колоды
        for suit, name in product(SUITS, VALUES):
            self.cards.append(Card(0, 0, CARD_SIZE['w'], CARD_SIZE['h'], name, VALUES[name], suit))

            # колоду будем отображать рядом с раздающим, так что координату нужно передавать близкую у нему
            # наверное где-то в углу рядом с ним
            # но делать ли это во время создания колоды?
