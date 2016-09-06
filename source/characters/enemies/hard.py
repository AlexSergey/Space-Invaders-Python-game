from _enemies import Enemyies
from imageLoader import imageLoader
from screenManager import screenManager
from collectionObjects import collectionObjects

class Hard(Enemyies):
    def __init__(self, player, levelManager):
        self.scoreBonus = 5
        self.width = 26
        self.height = 25
        self.scale = 1
        self.healthBarWidth = self.height * self.scale
        self.healthInit = 3
        self.maxVelocity = 7
        self.health = self.healthInit
        bounds = (screenManager.getScreen().get_width() + self.width, screenManager.getScreen().get_height() + self.height)
        self.target = player
        self.levelManager = levelManager
        self.seeing = 700
        self.asset = imageLoader('./images/enemies/hard.png', self.scale, (0, 0, self.width, self.height))
        self.image = self.asset
        # remove 255, 255, 255 background color
        self.image.set_colorkey((255, 255, 255))
        super(Hard, self).__init__(bounds)
        collectionObjects.add(self)
        player.collisionGroup.append(self)