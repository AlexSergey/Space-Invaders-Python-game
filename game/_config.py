import sys
sys.path.append('.\\core\\')
sys.path.append('.\\utils\\')
sys.path.append('.\\python_modules\\')
sys.path.append('.\\misc\\')
sys.path.append('.\\characters\\')
sys.path.append('.\\characters\\asteroids\\')
sys.path.append('.\\characters\\enemies\\')
sys.path.append('.\\backgrounds\\')
sys.path.append('.\\weapons\\')

screen_width = 1024
screen_height = 768

_player_max_bullets = 9
_player_weapon_reload = 250
_asteroids_count = 10


_levels = {
    'level1': {
        'title': 'level 1',
        'scoreStart': 0,
        'score': 25,
        'enemies': {
            'Simple': 5
        }
    },
    'level2': {
        'title': 'level 2',
        'scoreStart': 25,
        'score': 50,
        'enemies': {
            'Simple': 7
        }
    },
    'level3': {
        'title': 'level 3',
        'scoreStart': 50,
        'score': 75,
        'enemies': {
            'Simple': 6,
            'Middle': 2
        }
    },
    'level4': {
        'title': 'level 4',
        'scoreStart': 75,
        'score': 90,
        'enemies': {
            'Simple': 3,
            'Middle': 2,
            'Hard': 2
        }
    },
    'level5': {
        'title': 'level 5',
        'scoreStart': 90,
        'score': 100,
        'enemies': {
            'Boss': 1
        }
    }
}