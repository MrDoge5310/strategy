import random

import pygame


class Sprite:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.step = 5
        self.rect = pygame.Rect(x, y, 64, 64)
        self.image = pygame.image.load(filename)
        self.shot_sound = pygame.mixer.Sound('shot.mp3')
        self.shot_sound.set_volume(0.2)
        self.reloading = False

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))

    def control(self, win_width, win_height):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.step
        if keys[pygame.K_RIGHT] and self.rect.x < win_width - 64:
            self.rect.x += self.step
        if keys[pygame.K_UP] and self.rect.y > 5:
            self.rect.y -= self.step
        if keys[pygame.K_DOWN] and self.rect.y < win_height - 64:
            self.rect.y += self.step

    def shot(self):
        if not self.reloading:
            self.shot_sound.play()
            b = Bullet(self.rect.centerx, self.rect.centery)
        return b


class Enemy:
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, 64, 64)
        self.image = pygame.image.load(filename)
        self.hspeed = 0
        self.vspeed = 5

    def draw(self, scr):
        scr.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, player):
        if player.rect.y - self.rect.y < 200:
            self.vspeed = 10
            self.hspeed = 5

        if self.rect.x > player.rect.x:
            self.rect.x -= self.hspeed
        elif self.rect.x < player.rect.x:
            self.rect.x += self.hspeed

        self.rect.y += self.vspeed

    def isAway(self, height):
        if self.rect.y > height:
            return True
        else:
            return False


class RangeEnemy(Enemy):
    def __init__(self, x, y, filename):
        super().__init__(x, y, filename)
        self.position = random.randint(0, 201)
        self.canShoot = False
        self.reload_time = 120

    def move(self, player):
        if self.rect.y < self.position:
            self.rect.y += 3

        if self.rect.x > player.rect.x:
            self.rect.x -= 2
        elif self.rect.x < player.rect.x:
            self.rect.x += 2

    def shot(self):
        if self.rect.y >= self.position:
            self.canShoot = True

        if self.canShoot:
            if self.reload_time > 0:
                self.reload_time -= 1
            if self.reload_time == 0:
                self.reload_time = 60
                return True


class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 7, 20)

    def draw(self, wnd):
        pygame.draw.rect(wnd, 'yellow', self.rect, 0, 10)
        self.rect.y -= 10


class EnemyBullet(Bullet):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, wnd):
        pygame.draw.rect(wnd, 'red', self.rect, 0, 10)
        self.rect.y += 10