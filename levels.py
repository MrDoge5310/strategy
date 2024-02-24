from sprites import *


meele_enemy_img = ['sword.png', 'enemycar.png']
range_enemy_img = ['Skat.png', 'dalnik.png']


def level1():
    enemies = []
    i = 3
    while i > 0:
        img = meele_enemy_img[1]
        enemies.append(Enemy(random.randint(0, 700 - 64),
                             -64, img))
        i -= 1
    return enemies


def level2():
    enemies = []
    img = meele_enemy_img[0]

    i = 2  # количество врагов ближнего боя
    n = 3  # количество врагов дальнего боя
    while i > 0:
        enemies.append(Enemy(random.randint(0, 700 - 64),
                             -64, img))
        i -= 1

    img = range_enemy_img[0]
    while n > 0:
        enemies.append(RangeEnemy(random.randint(0, 700 - 64), -64, img))
        n -= 1
    return enemies
