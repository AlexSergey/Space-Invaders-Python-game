import random
from _baseCharacter import BaseCharacter
from imageLoader import imageLoader

class Asteroid(BaseCharacter):
    def __init__(self, image, scale, clip, bounds):
        self.isWaitingToRespawn = False
        self.image = imageLoader(image, scale, clip)
        self.objectType = 'asteroid'
        # remove #454e5b background color
        self.image.set_colorkey(0x454e5b)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 400
        speed = random.randrange(1, 4)
        self.velocityX = speed
        self.velocityY = speed
        self.accelerationX = 0
        self.accelerationY = 0
        self.boundX = bounds[0]
        self.boundY = bounds[1]
        self.angle = 0
        self.onSpawn()

    def reset(self):
        self.angle = 0
        self.rect.x = random.randrange(0, self.boundX) * -1
        self.rect.y = random.randrange(0, self.boundY) * -1

    def update(self):
        if self.isWaitingToRespawn:
            self.isWaitingToRespawn = False
            self.reset()
        else:
            self.velocityX += self.accelerationX
            self.velocityY += self.accelerationY
            self.rect.x += self.velocityX
            self.rect.y += self.velocityY

            self.checkObjectLeftTheArea()