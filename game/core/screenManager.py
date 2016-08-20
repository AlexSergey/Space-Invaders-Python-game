from singleton import Singleton
import pygame
from _config import screen_width, screen_height

class _ScreenManager(Singleton):
    def __init__(self):
        self.screen = pygame.display.set_mode((screen_width, screen_height))

    def getScreen(self):
        return self.screen

screenManager = _ScreenManager()