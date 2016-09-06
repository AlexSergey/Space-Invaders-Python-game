import pygame
from screenManager import screenManager

class HealthBar():
    def __init__(self, width, health):
        self.health = health
        self.damageCounter = 0
        self.width = width
        self.height = 4

    def damage(self):
        self.damageCounter += 1

    def update(self, x, y, isWaitingToRespawn):
        if not isWaitingToRespawn:
            width = self.width - ((self.width / self.health) * self.damageCounter)
            colorGetter = 0 if self.damageCounter == 0 else 1
            color = ((4, 164, 113), (255, 232, 38))[colorGetter]
            pygame.draw.rect(screenManager.getScreen(), color, (x, y - 5, width, self.height))

    def reset(self):
        self.damageCounter = 0