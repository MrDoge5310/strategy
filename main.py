import random
import pygame.transform

from levels import *
from sprites import *
pygame.init()

width = 700
height = 680

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True

player = Sprite(width/2 - 32, height - 64, "player-img.png")
bg_image = pygame.image.load('images.png')
bg_image = pygame.transform.scale(bg_image, (width, height))

levels = [boss_lvl()]

healthbar = []

i = 10
while i > 0:
    healthbar.append(pygame.Rect(520 + 15*i, 630, 10, 30))
    i -= 1

delay = 60
enemies = levels[0]
lvl = 0
bullets = []
enemy_bullets = []

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(player.shot())

    screen.blit(bg_image, (0, 0))

    for b in bullets:
        b.draw(screen)
        if b.rect.y < 0:
            bullets.remove(b)
    for b in enemy_bullets:
        b.draw(screen)
        if b.rect.y > height:
            enemy_bullets.remove(b)
        if b.checkHit(player):
            player.health -= 1
            enemy_bullets.remove(b)
            print(player.health)

    if len(enemies) == 0:
        lvl += 1
        enemies = levels[lvl]

    if delay > 0:
        delay -= 1
    if delay == 0:
        for enemy in enemies:
            enemy.active = True
        delay = 60

    player.control(width, height)
    player.draw(screen)

    for enemy in enemies:
        enemy.move(player)
        enemy.draw(screen)
        if enemy.rect.colliderect(player.rect):
            player.health -= 1
            enemies.remove(enemy)
        if enemy.shot():
            enemy_bullets.append(EnemyBullet(enemy.rect.centerx, enemy.rect.centery))
        if enemy.isAway(height):
            enemies.remove(enemy)
        for b in bullets:
            if b.rect.colliderect(enemy.rect):
                bullets.remove(b)
                enemies.remove(enemy)

    i = 0
    while i < player.health:
        pygame.draw.rect(screen, 'red', healthbar[i])
        i += 1

    if player.health <= 0:
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
