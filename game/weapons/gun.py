import pygame
from bullet import Bullet
from Ammo import Ammo
from imageLoader import imageLoader
from screenManager import screenManager
from _config import _player_max_bullets, _player_weapon_reload
from soundManager import soundManager

class ReloadBar():
    def __init__(self, weaponReloadTime):
        self.widthInit = 125
        self.weaponReloadTime = weaponReloadTime
        self.width = self.widthInit
        self.reloading = False

        self.ammoTextImage = imageLoader('./images/texts/ammo.jpg', 1, (0, 0, 128, 32))
        # remove black background color
        self.ammoTextImage.set_colorkey((0, 0, 0))

        self.state = False

    def setState(self, state):
        self.state = state
        if not self.reloading:
            self.reloading = True

    def setReloading(self, state):
        self.width = self.widthInit
        self.reloading = state

    def update(self):
        screenManager.getScreen().blit(self.ammoTextImage, (screenManager.getScreen().get_width() - 128, 0))
        if self.state:
            self.width -= (1. / (self.weaponReloadTime / self.widthInit))
            pygame.draw.rect(screenManager.getScreen(), (255, 0, 0), (screenManager.getScreen().get_width() - self.widthInit, 50, self.width, 5))

class Gun():
    def __init__(self, player):
        self.player = player
        self.bullets = []
        self.ammo = Ammo()
        self.ammo.current = _player_max_bullets
        self.reloadBar = ReloadBar(_player_weapon_reload)
        self.reset()

    def fire(self, x2, y2, angle):
        isReloading = self.checkForReload()

        if not isReloading:
            soundManager.playShot()
            self.ammo.down(1)
            x1 = self.player.rect.x + self.player.width / 2
            y1 = self.player.rect.y + self.player.height / 2
            self.bullets.append(Bullet(x1, y1, x2, y2, angle))
            self.counter += 1


    def checkForReload(self):
        if self.counter >= self.charge:
            self.reloading = True
            self.reloadBar.setState(True)
            return True
        else:
            return False

    def update(self):
        self.ammo.render()
        self.reloadBar.update()
        self.checkForReload()
        if self.reloading:
            if self.reloadTime <= 0:
                self.ammo.current = _player_max_bullets
                self.reloadBar.setReloading(False)
                self.reloadBar.setState(False)
                self.reset()
            else:
                self.reloadTime -= 1

        for bullet in self.bullets:
            bullet.update()
            pass

    def reloading(self):
        self.bullets = []
        self.counter = 0

    def reset(self):
        self.counter = 0
        self.charge = _player_max_bullets
        self.reloadTime = _player_weapon_reload
        self.reloading = False

