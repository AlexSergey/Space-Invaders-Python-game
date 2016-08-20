from _enemies import Enemyies
from imageLoader import imageLoader
from screenManager import screenManager
from collectionObjects import collectionObjects

class Middle(Enemyies):
    def __init__(self, player, levelManager):
        self.scoreBonus = 3
        self.width = 28
        self.height = 53
        self.scale = 2
        self.healthBarWidth = self.height * self.scale
        self.healthInit = 3
        self.maxVelocity = 4
        self.health = self.healthInit
        bounds = (screenManager.getScreen().get_width() + self.width, screenManager.getScreen().get_height() + self.height)
        self.target = player
        self.levelManager = levelManager
        self.seeing = 300
        self.asset = imageLoader('./images/enemies/middle.png', self.scale, (0, 0, self.width, self.height))
        self.image = self.asset
        # remove 255, 255, 255 background color
        self.image.set_colorkey((255, 255, 255))
        super(Middle, self).__init__(bounds)
        collectionObjects.add(self)
        player.collisionGroup.append(self)