from _spriteObject import SpriteObject
from screenManager import screenManager

class Scores(SpriteObject):
    def __init__(self):
        self.numberWidth = 11
        super(Scores, self).__init__("./images/misc/numbers.jpg", 10, 2, self.numberWidth, 24, (0, 0, 0))
        self.frames = self.fillFrameArray([])
        self.current = 0

    def get(self):
        return self.current

    def up(self, num):
        self.current += num

    def down(self, num):
        self.current -= num

    def reset(self):
        self.current = 0

    def render(self):
        firstDigit = self.current % 10
        lastDigit = (self.current % 100 - firstDigit) / 10
        screenManager.getScreen().blit(self.frames[firstDigit], (22, 0))
        screenManager.getScreen().blit(self.frames[lastDigit], (-2, 0))