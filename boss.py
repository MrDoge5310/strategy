import pygame


class Mascot:
    def __init__(self):
        self.filename = "mascot.png"
        self.rect = pygame.Rect(400, -128, 64, 64)
        self.image = pygame.image.load(self.filename)

    def move(self):
        pass


class Boss:
    def __init__(self, filename):
        self.rect = pygame.Rect(200, -128, 128, 128)
        self.image = pygame.image.load(filename)
        self.direction = 'right'
        self.health = 100
        self.mascots = []
        self.ray = pygame.Rect(self.rect.centerx, self.rect.centery, 20, 0)

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

    def attack1(self):
        i = 5
        while i != 0:
            self.mascots.append(Mascot())

    def attack2(self, wnd):
        self.ray.y += 1
        pygame.draw.rect(wnd, 'green', self.ray)

    def stage1(self):
        pass

    def stage2(self):
        pass

