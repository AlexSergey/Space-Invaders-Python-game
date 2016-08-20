from _calculation import Calculation

DAMAGE_DELAY = 35

class BaseCharacter(Calculation):
    def __init__(self):
        self.damaged = False
        self.damageDelay = DAMAGE_DELAY
        self.waitingToRespawn = 0
        self.isWaitingToRespawn = False

    def reset(self):
        self.damaged = False
        self.damageDelay = DAMAGE_DELAY

    def onSpawn(self):
        self.reset()

    def resetCoords(self):
        self.rect.x = 9999
        self.rect.y = 9999

    def onDeath(self):
        self.isWaitingToRespawn = True
        self.waitingToRespawn = 120
        self.healthBar.reset()

    def delay(self):
        # Process Delayed events
        self.waitingToRespawn -= 1
        if self.waitingToRespawn <= 0:
            self.isWaitingToRespawn = False
            self.reset()

    def damage(self):
        if not self.damaged:
            self.healthBar.damage()
            self.health -= 1
            self.damaged = True
            self.damageDelay = DAMAGE_DELAY
            if self.health == 0:
                self.onDeath()

    def update(self):
        if self.damageDelay <= 0:
            self.damageDelay = 0
            self.damaged = False
        else:
            self.damageDelay -= 1