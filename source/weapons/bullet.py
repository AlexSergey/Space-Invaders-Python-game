import pygame
from imageLoader import imageLoader
from _calculation import Calculation
from screenManager import screenManager
from collectionObjects import collectionObjects

class Bullet(Calculation):
    def __init__(self, x1, y1, x2, y2, angle):
        self.angle = angle
        self.width = 30
        self.height = 18
        self.thrust = .6
        self.asset = imageLoader('./images/misc/bullet.png', 2, (0, 0, self.width, self.height))
        self.image = self.asset
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x1
        self.rect.y = y1
        self.velocityX = 0
        self.velocityY = 0
        self.coords = self.mathCalc(x1, y1, x2, y2)

    def update(self):
        if self.rect.x < 0 or self.rect.y < 0 or self.rect.x > screenManager.getScreen().get_width() + self.rect.width or self.rect.y > screenManager.getScreen().get_height() + self.rect.height:
            self.rect.x = -9999
            self.rect.y = -9999
            return False

        for object in collectionObjects.get():
            # Check enemy collision
            if object.objectType == 'enemy':
                if self.rect.colliderect(object.rect) > 0:
                    object.damage(False)

        targetVectorX = self.coords['targetVectorX']
        targetVectorY = self.coords['targetVectorY']
        # Apply damping thrust
        self.velocityX += targetVectorX * self.thrust
        self.velocityY += targetVectorY * self.thrust

        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

        self.image = pygame.transform.rotate(self.asset, self.angle)
        screenManager.getScreen().blit(self.image, (self.rect.x, self.rect.y))