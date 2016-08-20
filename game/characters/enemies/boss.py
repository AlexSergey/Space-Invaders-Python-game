from _enemies import Enemyies
from imageLoader import imageLoader
from screenManager import screenManager
from collectionObjects import collectionObjects

class Boss(Enemyies):
    def __init__(self, player, levelManager):
        self.scoreBonus = 10
        self.width = 44
        self.height = 53
        self.scale = 2
        self.healthBarWidth = self.height * self.scale
        self.healthInit = 8
        self.maxVelocity = 5
        self.health = self.healthInit
        bounds = (screenManager.getScreen().get_width() + self.width, screenManager.getScreen().get_height() + self.height)
        self.target = player
        self.levelManager = levelManager
        self.seeing = 700
        self.asset = imageLoader('./images/enemies/boss.png', self.scale, (0, 0, self.width, self.height))
        self.image = self.asset
        # remove 255, 255, 255 background color
        self.image.set_colorkey((255, 255, 255))
        super(Boss, self).__init__(bounds)
        collectionObjects.add(self)
        player.collisionGroup.append(self)

    def enemyLogic(self):
        results = self.mathCalc(self.rect.x, self.rect.y, self.target.rect.x, self.target.rect.y)
        targetVectorX = results['targetVectorX']
        targetVectorY = results['targetVectorY']
        # Apply damping thrust
        self.velocityX += targetVectorX * self.thrust
        self.velocityY += targetVectorY * self.thrust