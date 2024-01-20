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
        if keys[pygame.K_SPACE]:
            if not self.reloading:
                self.shot_sound.play()
                self.reloading = True

