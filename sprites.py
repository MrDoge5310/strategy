import pygame


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.step = 5
        self.rect = pygame.Rect(x, y, 64, 64)
        self.image = pygame.image.load(filename)

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))
