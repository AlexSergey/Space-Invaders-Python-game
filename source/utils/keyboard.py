import pygame

def getControls():
    up = pygame.key.get_pressed()[pygame.K_UP]
    down = pygame.key.get_pressed()[pygame.K_DOWN]
    w = pygame.key.get_pressed()[pygame.K_w]
    s = pygame.key.get_pressed()[pygame.K_s]
    space = pygame.key.get_pressed()[pygame.K_SPACE]

    return (up, down, w, s, space)