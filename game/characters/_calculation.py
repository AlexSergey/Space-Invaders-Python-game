import pygame
import math

class Calculation(pygame.sprite.Sprite):
    def setMaxVelocity(self):
        if self.velocityX > self.maxVelocity:
            self.velocityX = self.maxVelocity
        if self.velocityX < self.maxVelocity * -1:
            self.velocityX = self.maxVelocity * -1

        if self.velocityY > self.maxVelocity:
            self.velocityY = self.maxVelocity
        if self.velocityY < self.maxVelocity * -1:
            self.velocityY = self.maxVelocity * -1

    def checkObjectLeftTheArea(self):
        if self.rect.x > self.boundX or self.rect.y > self.boundY:
            self.onSpawn()

    def mathCalc(self, x1, y1, x2, y2):
        results = {}
        lineLength = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        results['targetVectorX'] = x2 - x1
        results['targetVectorY'] = y2 - y1
        distance = math.sqrt((0 - results['targetVectorX']) ** 2 + (0 - results['targetVectorY']) ** 2)

        results['lineLength'] = lineLength
        results['distance'] = distance

        if distance > 0:
            results['targetVectorX'] /= distance
            results['targetVectorY'] /= distance
        else:
            results = {
                'targetVectorX': 0,
                'targetVectorY': 0
            }
        return results

    def calcAngle(self, targetX, targetY):
        dx = self.rect.centerx - targetX
        dy = self.rect.centery - targetY
        dy *= -1

        radians = math.atan2(dy, dx)
        dir = radians * 180 / math.pi
        dir += 0
        return dir