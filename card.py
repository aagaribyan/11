import pygame
from game_object import GameObject


class Card(GameObject):
    def __init__(self, x, y, w, h, name, value, suit, showing=False):  # color, special_effect=None)
        GameObject.__init__(self, x, y, w, h)
        # self.color = color
        # self.special_effect = special_effect

        self.color = (0, 0, 0)  # пока оставлю цвет, пока не разберусь как картинку передать

        self.name = name  # название
        self.value = value  # значение (для вычисления сумм)
        self.suit = suit  # масть
        self.showing = showing  # для отображения/скрытия
        self.card_image = 'images/' + suit[0] + str(value) + '.png'  # картинка карты
        self._calculate_priority()  # нужно для бота

    # назначение карте приоритета (для бота)
    def _calculate_priority(self):
        self.priority = 1

        if self.suit == 'Clubs':
            # повышаем ценность крестей для бота
            self.priority += 1
            if self.name == 'Two':
                # особый приоритет двойке, чтобы взял при первой возможности
                self.priority += 9

        if self.name == 'Jack':
            # понижаем приоритет вальтов, чтобы бот не торопился их использовать
            self.priority -= 6

        if self.suit == 'Diamonds' and self.name == 'Ten':
            # аналогично особый приоритет десятке бубей
            self.priority += 9

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)  # позже переделать в отображение картинки, а не закрашивания

    def __str__(self):  # для принта, вряди ли понадобится
        message = self.suit + self.name
        return message
