import pygame

def imageLoader(image, scale, clip):
    asset = pygame.image.load(image)
    assetClipped = pygame.Surface((clip[2], clip[3]))
    assetClipped.blit(asset, (0, 0), clip)
    scale_gabarites = (clip[2] * scale, clip[3] * scale)
    scaledAsset = pygame.transform.scale(assetClipped, scale_gabarites)

    return scaledAsset