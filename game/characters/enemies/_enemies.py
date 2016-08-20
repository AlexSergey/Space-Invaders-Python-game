import pygame, random, math
from healthbar import HealthBar
from explosion import Explosion
from _baseCharacter import BaseCharacter

class Enemyies(BaseCharacter):
    def __init__(self, bounds):
        self.objectType = 'enemy'
        super(Enemyies, self).__init__()
        self.angle = 0
        self.waitingToRespawn = 0
        self.isWaitingToRespawn = False
        self.rect = self.image.get_rect()
        self.damping = .3
        self.thrust = .4
        self.seeing = 300
        self.boundX = bounds[0]
        self.boundY = bounds[1]
        self.velocityX = 0
        self.velocityY = 0
        self.healthBar = HealthBar(self.healthBarWidth, self.health)
        self.explosion = Explosion('./images/misc/explosion1.jpg', 5, 2, 23, 26, (0, 0, 0))
        self.reset()

    def update(self):
        super(Enemyies, self).update()
        self.healthBar.update(self.rect.x, self.rect.y, self.isWaitingToRespawn)
        self.angle = self.calcAngle(self.target.rect.x, self.target.rect.y)
        if self.isWaitingToRespawn:
            self.explosion.animate(self, self.resetCoords)
            self.delay()
        else:
            if not self.damaged:
                self.image = pygame.transform.rotate(self.asset, self.angle)

                self.enemyLogic()

                self.setMaxVelocity()

                self.rect.x += self.velocityX
                self.rect.y += self.velocityY

                self.checkObjectLeftTheArea()

    def damage(self, damageByPlayer):
        self.damageByPlayer = damageByPlayer
        super(Enemyies, self).damage()

    def enemyLogic(self):
        ####################
        # AI State machine #
        ####################
        # State 1 - Search player
        if self.state == 1:
            if math.sqrt((self.rect.x - self.target.rect.x) ** 2 + (
                        self.rect.y - self.target.rect.y) ** 2) <= self.seeing:
                self.state = 2
            else:
                self.velocityX += self.thrust
                self.velocityY += self.thrust
        # State 2 - Chase player
        elif self.state == 2:
            if math.sqrt((self.rect.x - self.target.rect.x) ** 2 + (
                        self.rect.y - self.target.rect.y) ** 2) > self.seeing:
                self.state = 3
            else:
                # Get target vector
                results = self.mathCalc(self.rect.x, self.rect.y, self.target.rect.x, self.target.rect.y)
                targetVectorX = results['targetVectorX']
                targetVectorY = results['targetVectorY']
                # Apply damping thrust
                self.velocityX += targetVectorX * self.thrust
                self.velocityY += targetVectorY * self.thrust
        # State 3 - Lost chase
        elif self.state == 3:
            self.velocityX += self.thrust
            self.velocityY += self.thrust

    def reset(self):
        self.health = self.healthInit
        super(Enemyies, self).reset()
        if self.levelManager.allowSpawn():
            self.state = 1
            self.rect.x = random.randrange(0, self.boundX) * -1
            self.rect.y = random.randrange(0, self.boundY) * -1
            self.velocityX = 0
            self.velocityY = 0
        else:
            self.resetOffScreen()
            self.levelManager.addWaitingSpawn(self)
            self.levelManager.enemyHasSpawned()

    def resetOffScreen(self):
        self.rect.x = self.boundX
        self.rect.y = self.boundY

    def onDeath(self):
        self.health = self.healthInit
        super(Enemyies, self).onDeath()
        if not self.damageByPlayer:
            self.levelManager.scoreUp(self.scoreBonus)

    def onSpawn(self):
        self.health = self.healthInit
        self.healthBar.reset()
        super(Enemyies, self).onSpawn()