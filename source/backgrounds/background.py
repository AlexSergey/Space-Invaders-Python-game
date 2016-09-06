import pygame
from screenManager import screenManager

class Background(pygame.sprite.Sprite):
    def __init__(self, image):
        width = screenManager.getScreen().get_width()
        height = screenManager.getScreen().get_height()
        self.original_image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.original_image, (width, height))
        self.rect = self.image.get_rect()

    def update(self):
        pass