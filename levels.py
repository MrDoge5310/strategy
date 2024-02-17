from sprites import *


def level1():
    enemies = []
    i = 5
    while i > 0:
        enemies.append(Enemy(random.randint(0, 700 - 64),
                             -64, 'player-img.png'))
        i -= 1
    return enemies
