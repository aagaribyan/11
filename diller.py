import pygame
from game_object import GameObject


class Ball(GameObject):  # потенциально переделывать
    def __init__(self, x, y, r, color, speed):
        GameObject.__init__(self, x-r, y-r, r*2, r*2, speed)

        self.radius = r
        self.diameter = r*2
        self.color = color  # позже добавить в круг букву D (diller) или Р (раздающий)

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)
