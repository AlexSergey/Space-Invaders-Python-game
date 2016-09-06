import sys, pygame
from soundManager import soundManager
from background import Background
from screenManager import screenManager
from player import Player
from collectionObjects import collectionObjects
from asteroidsFactory import generateAsteroids
from levelManager import levelManager
from keyboard import getControls

clock = pygame.time.Clock()

mainMenu = {
    'newGame': False
}

class GameWorld():
    def __init__(self):
        # setup all game objects and scene
        soundManager.playMusic()
        self.setBg = False
        self.player = Player()
        self.loopStop = False
        self.gameState = 'mainMenu'
        self._prevControls = (0, 0, 0, 0)
        collectionObjects.add(self.player)
        generateAsteroids()
        levelManager.init(self.player)

    def gameLoop(self):
        while True:
            controls = self.getControls()
            # Game state manager
            # Input handler
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if controls[3] and self.gameState == 'pause':
                        self.gameState = 'run'
                        self.setBg = False
                        continue

                    if controls[3] and self.gameState == 'run':
                        self.gameState = 'pause'
                        self.setBg = False
                        continue

                    if controls[2] and self.gameState == 'mainMenu':
                        self.gameState = 'run'
                        self.setBg = False
                        continue

                    if controls[3] and self.gameState == 'gameOver':
                        sys.exit()

                # Don't block loop
                if event.type == pygame.QUIT:
                    sys.exit()

            if hasattr(self, 'background'):
                screenManager.getScreen().blit(self.background.image, (0, 0))

            self.gameOver()

            self.run()

            self.pause()

            self.mainMenu()

            pygame.display.flip()

            # 60 FPS
            clock.tick(60)

    def run(self):
        if self.gameState == 'run' or self.gameState == 'pause':
            if not self.setBg:
                self.background = Background('./images/backgrounds/bg-game.jpg')
                self.setBg = True

            levelManager.update()
            # Update objects position
            for game_object in collectionObjects.get():
                if not self.gameState == 'pause':
                    game_object.update()
                screenManager.getScreen().blit(game_object.image, (game_object.rect.x, game_object.rect.y))

    # We stoped game and set transparency rectangle
    def pause(self):
        if self.gameState == 'pause':
            fog = pygame.Surface((screenManager.getScreen().get_width(),
                                  screenManager.getScreen().get_height()))
            fog.set_alpha(128)
            fog.fill((255, 255, 255))
            screenManager.getScreen().blit(fog, (0, 0))

    def mainMenu(self):
        if self.gameState == 'mainMenu':
            if not self.setBg:
                self.background = Background('./images/backgrounds/bg-main-menu.jpg')
                self.setBg = True

    # If we catch 100 scores - you are win!
    def gameOver(self):
        if levelManager.score.current == 100:
            self.gameState = 'gameOver'
            self.background = Background('./images/backgrounds/bg-game-over.jpg')

    # get controls in Main menu
    def getControls(self):
        self.controls = getControls()
        up = 1 if self.controls[0] or self.controls[2] else 0
        down = 1 if self.controls[1] or self.controls[3] else 0
        enter = pygame.key.get_pressed()[pygame.K_RETURN]
        esc = pygame.key.get_pressed()[pygame.K_ESCAPE]
        return (up, down, enter, esc)
