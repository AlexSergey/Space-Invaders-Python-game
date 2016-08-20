import pygame
from _spriteObject import SpriteObject
from soundManager import soundManager

class Explosion(SpriteObject):
    def __init__(self, imageUrl, frameCount, scale, frameWidth, frameHeight, cutColor):
        super(Explosion, self).__init__(imageUrl, frameCount, scale, frameWidth, frameHeight, cutColor)
        self.explosionFrames = self.fillFrameArray([])
        self.explosionCurrentFrame = 0

    def reset(self, cb = False):
        self.explosionCurrentFrame = 0
        if callable(cb):
            cb()

    def animate(self, objectForExplosion, cb = False):
        if self.explosionCurrentFrame < len(self.explosionFrames):
            if (self.explosionCurrentFrame == 0):
                soundManager.playExplosion()

            objectForExplosion.image = self.explosionFrames[self.explosionCurrentFrame]
            self.explosionCurrentFrame += 1
        else:
            objectForExplosion.image = pygame.Surface((0, 0))
            self.reset(cb)