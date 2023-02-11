class Player(object):
    def __init__(self, name, bot=False):
        self.cards = []  # карты в руке
        self.taken = []  # отбой игрока
        self.name = name  # имя игрока/бота
        self.score = 0  # набранные очки
        self.isBot = bot  # чтобы отличать бота от игрока

    # очищение отбоя для следующей партии
    def new_round(self):
        self.taken = []
        # self.cards = []

    # добавление карт в руку игрока (всегда добавляется по 4 карты)
    def add_hand_cards(self, cards):
        for card in cards:
            self.cards.append(card)

    # добавление карт в отбой игрока, в осномном по несколько карт за раз
    def add_taken_cards(self, cards):
        for card in cards:
            self.taken.append(card)

    # удаление карты с руки
    def remove_hand_card(self, card):
        self.cards.remove(card)

        # for hc in enumerate(self.cards):
        #    if hc == card:
        #        self.cards.pop(i)
        #        break

    # проверка правильности комбинации
    def check_combination(self, from_table, hand_card):
        if hand_card.value in ['Q', 'K']:
            if len(from_table) == 1 and from_table.value == hand_card.value:
                return True

        elif hand_card.value == 'J' and not any([tCard.value in ['Q', 'K'] for tCard in from_table]):
            return True

        elif len(from_table) > 0 and all([type(c.value) is int for c in from_table]):
            # проверка на int исключает не только Q и K, но так же J
            if hand_card.value + sum([c.value for c in from_table]) == 11:
                return True

        return False

    # подсчет карт по окончанию партии
    def calculate_score(self):
        all_cards_count = len(self.taken)
        clubs_cards_count = 0
        clubs_two = False
        diamonds_ten = False

        for card in self.taken:
            if card.suit == 'Clubs':
                clubs_cards_count += 1

                if card.name == 'Two':  # 2-ка крестей
                    clubs_two = True

            elif card.suit == 'Diamonds' and card.name == 'Ten':  # 10-ка бубей
                diamonds_ten = True

        return [all_cards_count, clubs_cards_count, clubs_two, diamonds_ten]
