import pygame
from random import randint

class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.initY = y
        self.vel = -1
        self.dieOff = randint(2, 40)
        self.lead = randint(2, 10)

    def update(self, screen):
        colour = screen.get_at((self.x, self.y))[0] - self.dieOff

        self.y += self.vel

        tint = randint(0, 255)

        if tint >= colour:
            tint = 0

        try:
            screen.set_at((self.x, self.y), [colour, tint, 0])
            screen.set_at((self.x - 1, self.y + 1), [colour, tint, 0])
            screen.set_at((self.x + 1, self.y + 1), [colour, tint, 0])
            screen.set_at((self.x - 2, self.y + 1), [colour, tint, 0])
            screen.set_at((self.x + 2, self.y + 1), [colour, tint, 0])

            screen.set_at((self.x, self.y + self.lead), [0, 0, 0])
            screen.set_at((self.x - 1, self.y + 3), [0, 0, 0])
            screen.set_at((self.x + 1, self.y + 3), [0, 0, 0])
            screen.set_at((self.x - 2, self.y + 2), [0, 0, 0])
            screen.set_at((self.x + 2, self.y + 2), [0, 0, 0])

        except:
            self.y = self.initY
            self.dieOff = randint(2, 40)
            self.lead = randint(2, 10)
