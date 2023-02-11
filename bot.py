from player import Player


class Bot(Player):
    def __init__(self, name):
        Player.__init__(self, name, bot=True)

    # подбор наименее нужной карты на руке для сброса
    def choose_less_priority_card(self):
        # учесть вальта, нежелательно его выбрасывать  раньше времени
        min_prior = 100
        lp_card = None
        for card in self.cards:
            c_prior = card.priority

            if card.value == 'J':
                c_prior += 7

            if c_prior < min_prior:
                min_prior = c_prior
                lp_card = card

        return lp_card

    # выбор наилучшей комбинации
    def find_best_combination(self, table_cards):
        # для бота нужно реализовать проверку всех возможных сочетаний одной из карт с руки с картами на столе
        # желательно придумать как бы это хоть как-то оптимизировать

        # решение в лоб
        # формируем список всех возможных комбинаций карт со стола (не забыть не учитывать пустую)
        sub_lists = [ [] ]
        for a in table_cards:
            sub_lists += [s + [a] for s in sub_lists]

        # проверяем все комбинации в сочетании к каждой картой на руке
        best_comb = []
        best_prior = -3   # начальное значение этой переменной влияет на использование вальта
        for h_card in self.cards:  # карты на руках бота
            for t_cards in sub_lists:
                if t_cards != [] and self.check_combination(t_cards, h_card):  # проверяем возможна ли такая комбинация
                    sum_prior = h_card.priority + sum([card.priority for card in t_cards])
                    if sum_prior > best_prior:
                        best_comb = t_cards + [h_card]
                        best_prior = sum_prior

        return best_comb  # если возможных комбинаций нет, вернет пустой список
