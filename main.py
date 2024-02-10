import random
import pygame.transform

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

delay = 60
enemies = []
bullets = []

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

    if delay > 0:
        delay -= 1
    if delay == 0:
        enemies.append(Enemy(random.randint(0, width - 64), -64, 'player-img.png'))
        delay = 60

    player.control(width, height)
    player.draw(screen)

    for enemy in enemies:
        enemy.move(player)
        enemy.draw(screen)
        if enemy.isAway(height):
            enemies.remove(enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
