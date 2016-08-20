from singleton import Singleton
import pygame

class _SoundManager(Singleton):
    def __init__(self):
        pygame.init()
        self.audioExplosion = pygame.mixer.Sound("./audio/explosion.wav")
        self.audioExplosion.set_volume(.5)
        self.shot = pygame.mixer.Sound("./audio/shot.wav")
        self.shot.set_volume(.5)
        self.audioNextLevel = pygame.mixer.Sound("./audio/next-level.wav")
        self.audioNextLevel.set_volume(.5)

    def playMusic(self):
        pass
        #music = pygame.mixer.Sound("./audio/")
        #music.set_volume(.3)
        # -1 loop music
        #music.play(-1)

    def playExplosion(self):
        self.audioExplosion.play()

    def playNextLevel(self):
        self.audioNextLevel.play()

    def playShot(self):
        self.shot.play()

soundManager = _SoundManager()