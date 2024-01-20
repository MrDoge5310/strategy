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

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_image, (0, 0))

    player.move(width, height)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
