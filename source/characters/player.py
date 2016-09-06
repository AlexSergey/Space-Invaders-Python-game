import pygame
from gun import Gun
from explosion import Explosion
from healthbar import HealthBar
from imageLoader import imageLoader
from _baseCharacter import BaseCharacter
from levelManager import levelManager
from keyboard import getControls

class Player(BaseCharacter):
    def __init__(self):
        self.width = 66
        self.height = 45
        self.scale = 1
        self.healthBarWidth = self.width * self.scale
        self.objectType = 'player'
        super(Player, self).__init__()
        self.asset = imageLoader('./images/player.png', self.scale, (0, 0, self.width, self.height))
        self.image = self.asset
        # remove black background color
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.thrust = .5
        self.angle = 0
        self.damping = .3
        self.healthInit = 5
        self.maxVelocity = 8
        self.health = self.healthInit
        self.collisionGroup = []
        self.healthBar = HealthBar(self.healthBarWidth, self.health)
        self.explosion = Explosion('./images/misc/explosion1.jpg', 5, 2, 23, 26, (0, 0, 0))
        self.gun = Gun(self)
        self.shootReady = True
        self.onSpawn()

    def delay(self):
        super(Player, self).delay()
        levelManager.resetScore()

    def reset(self):
        self.health = self.healthInit
        super(Player, self).reset()
        self.isWaitingToRespawn = False
        self.rect.x = 400
        self.rect.y = 300
        self.velocityX = 0
        self.velocityY = 0
        self.accelerationX = 0
        self.accelerationY = 0
        self.collision = False

    def update(self):
        super(Player, self).update()
        self.healthBar.update(self.rect.x, self.rect.y, self.isWaitingToRespawn)
        if self.isWaitingToRespawn:
            self.explosion.animate(self, self.resetCoords)
            self.delay()
            # Update explosion animation (Player is Dead)
        else:
            # Process player input
            controls = getControls()
            self.processControls(controls)
            self.image = pygame.transform.rotate(self.asset, self.angle)
            # Collision detection
            self.checkForCollisions()
            self.gun.update()
            # Update the physics
            self.updatePhysics()

    def checkForCollisions(self):
        if self.health < 1:
            for gameObject in self.collisionGroup:
                if gameObject.objectType == 'enemy':
                    gameObject.onSpawn()
            self.onDeath()
            return False

        for gameObject in self.collisionGroup:
            self.collision = self.rect.colliderect(gameObject.rect)
            if self.collision:
                self.damage()
                gameObject.damage(True)
                break

    def updatePhysics(self):
        self.velocityX += self.accelerationX
        self.velocityY += self.accelerationY

        # Horizontal
        if self.velocityX < 0 - self.damping:
            self.velocityX += self.damping
        elif self.velocityX > 0 + self.damping:
            self.velocityX -= self.damping
        else:
            self.velocityX = 0

        # Vertical
        if self.velocityY < 0 - self.damping:
            self.velocityY += self.damping
        elif self.velocityY > 0 + self.damping:
            self.velocityY -= self.damping
        else:
            self.velocityY = 0

        self.setMaxVelocity()

        self.rect.x += self.velocityX
        self.rect.y += self.velocityY

    def processControls(self, controls):
        pos = pygame.mouse.get_pos()
        mouseX = pos[0]
        mouseY = pos[1]

        self.angle = self.calcAngle(mouseX, mouseY)

        leftBtn = pygame.mouse.get_pressed()[0]

        if leftBtn == 1 or controls[4] == 1:
            if self.shootReady:
                self.gun.fire(mouseX, mouseY, self.angle)
                self.shootReady = False
        else:
            self.shootReady = True

        playerWidth = self.image.get_rect().size[0]
        playerHeight = self.image.get_rect().size[1]

        x1 = self.rect.x + (playerWidth / 2)
        y1 = self.rect.y + (playerHeight / 2)

        x2 = mouseX
        y2 = mouseY

        up = 1 if controls[0] or controls[2] else 0
        down = 1 if controls[1] or controls[3] else 0

        if up == 1 or down == 1:
            results = self.mathCalc(x1, y1, x2, y2)
            targetVectorX = results['targetVectorX']
            targetVectorY = results['targetVectorY']

            self.accelerationX = (targetVectorX * self.thrust) * (up - down)
            self.accelerationY = (targetVectorY * self.thrust) * (up - down)
        else:
            self.accelerationX = 0
            self.accelerationY = 0