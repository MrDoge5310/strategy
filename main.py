from sprites import *
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player = Sprite(600, 400, "player-img.png")

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
