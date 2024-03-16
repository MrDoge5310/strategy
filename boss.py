import pygame


class Mascot:
    def __init__(self, filename):
        self.rect = pygame.Rect(400, -128, 128, 128)
        self.image = pygame.image.load(filename)


class Boss:
    def __init__(self, filename):
        self.rect = pygame.Rect(400, -128, 128, 128)
        self.image = pygame.image.load(filename)
        self.direction = 'right'
        self.health = 100

    def isAway(self, height):
        pass

    def shot(self):
        pass

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, player):
        if self.rect.y <= 100:
            self.rect.y += 2

        if self.direction == 'left':
            self.rect.x -= 2
            if self.rect.x <= 0:
                self.direction = 'right'

        if self.direction == 'right':
            self.rect.x += 2
            if self.rect.x + 128 >= 700:
                self.direction = 'left'

    def stage1(self):
        pass

    def stage2(self):
        pass

