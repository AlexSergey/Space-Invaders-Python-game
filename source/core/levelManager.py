from _config import _levels
from singleton import Singleton
from Scores import Scores
from imageLoader import imageLoader
from soundManager import soundManager
from screenManager import screenManager
from collectionObjects import collectionObjects
from simple import Simple
from middle import Middle
from hard import Hard
from boss import Boss
# We save all enemies in the object
# When we get scores for next level, we render it
enemies = {
    'Simple': Simple,
    'Middle': Middle,
    'Hard': Hard,
    'Boss': Boss
}
# Set level, enemies and score
# Respawn enemies after death
class _LevelManager(Singleton):
    def __init__(self):
        self.initialize = True
        self.level = 'level1'
        self.levelDelay = 160
        self.showLevelState = True
        self.scoreToNextLevel = 25
        self.currentWave = 1
        self.enemySpawnedCount = 0
        self.enemyDeathCount = 0
        self.enemiesPerWave = 0
        self.waitingToSpawn = []
        self.score = Scores()
        self.score.current = 0
        self.isSetLevel = True

    def init(self, player):
        self.player = player
        self.setLevel(self.initialize)
        self.initialize = False

    def allowSpawn(self):
        return not self.enemySpawnedCount >= self.enemiesPerWave

    def enemyHasSpawned(self):
        self.enemySpawnedCount += 1

    def resetScore(self):
        self.score.reset()
        self.level = 'level1'
        self.scoreToNextLevel = 25
        self.isSetLevel = True
        for gameObject in self.waitingToSpawn:
            gameObject.reset()

        self.setLevel(True)
        self.showLevel()

    def scoreUp(self, bonus):
        self.score.up(bonus)
        self.isSetLevel = True

    def addWaitingSpawn(self, gameObject):
        self.waitingToSpawn.append(gameObject)

    def update(self):
        toNextLevel = self.checkScore()
        self.checkScoreToNextLevel()
        self.setLevel(toNextLevel)
        self.showLevel()
        self.score.render()

        if self.allowSpawn():
            for gameObject in self.waitingToSpawn:
                gameObject.reset()

            self.waitingToSpawn = []

    def checkScoreToNextLevel(self):
        for l in _levels:
            if _levels[l]['scoreStart'] <= self.score.current < _levels[l]['score']:
                self.scoreToNextLevel = _levels[l]['score']
                self.level = l

    def checkScore(self):
        return self.score.current >= self.scoreToNextLevel

    def setLevel(self, toNextLevel):
        if self.isSetLevel and toNextLevel:
            self.showLevelState = True
            self.enemiesSet()
        self.isSetLevel = False

    def showLevel(self):
        if self.showLevelState and self.levelDelay >= 0:
            self.levelImage = imageLoader('./images/texts/' + self.level + '.jpg', 2, (0, 0, 128, 32))
            self.levelImage.set_colorkey((0, 0, 0))
            screenManager.getScreen().blit(self.levelImage, ((screenManager.getScreen().get_width() / 2) - (128 * 2 / 2), (screenManager.getScreen().get_height() / 2) - (32 * 2 / 2)))
            self.levelDelay -= 1
        else:
            self.levelDelay = 160
            self.showLevelState = False

    def enemiesSet(self):
        collectionObjects.resetObjects()
        enemiesInLevel = _levels[self.level]['enemies']
        self.enemySpawnedCount = 0
        self.enemyDeathCount = 0
        self.enemiesPerWave = 0
        self.waitingToSpawn = []

        for className in enemiesInLevel:
            count = enemiesInLevel[className]
            self.enemiesPerWave += count
            for i in range(0, count):
                enemies[className](self.player, self)

        if self.level != 'level1':
            soundManager.playNextLevel()

levelManager = _LevelManager()