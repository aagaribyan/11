# from game_object import GameObject

# карты на столе
class Table:  # (GameObject):
    def __init__(self, first_cards):
        self.cards_on_table = first_cards[:]  # возможно стоит перенести это в add_card
        # (с изменением её на случ неск карт)

    # выкладывание карты на стол
    def add_card(self, card):
        self.cards_on_table.append(card)

    # удаление собранных игроком карт со стола
    def remove_cards(self, cards):
        for card in cards:
            self.cards_on_table.remove(card)
