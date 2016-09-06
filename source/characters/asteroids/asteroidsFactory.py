from collectionObjects import collectionObjects
from asteroid import Asteroid
from screenManager import screenManager
from _config import _asteroids_count

def generateAsteroids():
    for i in range(1, _asteroids_count):
        _n = i / 2
        n = str(_n)
        gabarites = {}

        if _n == 0:
            gabarites['width'] = 5
            gabarites['height'] = 6
        if _n == 1:
            gabarites['width'] = 11
            gabarites['height'] = 10
        if _n == 2:
            gabarites['width'] = 22
            gabarites['height'] = 12
        if _n == 3:
            gabarites['width'] = 29
            gabarites['height'] = 26
        if _n == 4:
            gabarites['width'] = 29
            gabarites['height'] = 26

        name = 'stone' + n + '.jpg'
        asteroid = Asteroid('./images/asteroids/' + name, 1, (0, 0, gabarites['width'], gabarites['height']), (screenManager.getScreen().get_width() + gabarites['width'], screenManager.getScreen().get_height() + gabarites['height']))
        collectionObjects.add(asteroid)