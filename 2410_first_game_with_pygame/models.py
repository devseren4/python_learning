import random
import pygame
from pygame.sprite import Sprite


SCORE_POINT_EVENT = pygame.event.Event(pygame.USEREVENT + 1)


class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(370, 480))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 736:
            self.rect.x = 736


class Bullet(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("bullet.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 480))
        self.state = "ready"

    def reset(self):
        self.rect.y = 480
        self.state = "ready"

    def fire(self, player: Sprite):
        bullet_Sound = pygame.mixer.Sound("laser.wav")
        bullet_Sound.set_volume(0.2)
        bullet_Sound.play()
        self.rect.x = player.rect.x
        self.state = "fire"

    def update(self, player: Sprite):
        keys = pygame.key.get_pressed()

        if self.state == "ready":
            if keys[pygame.K_SPACE]:
                self.fire(player)
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

        if self.rect.y <= 0:
            self.reset()

        if self.state == "fire":
            self.rect.y -= 10


class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect(
            topleft=(random.randint(0, 735), random.randint(50, 150))
        )
        self.direction = "right"

    def respawn(self):
        self.rect.x = random.randint(0, 735)
        self.rect.y = random.randint(50, 150)

    def explode(self):
        explosion_Sound = pygame.mixer.Sound("explosion.wav")
        explosion_Sound.set_volume(0.1)
        explosion_Sound.play()

    def move(self):
        x_change = 2 if self.direction is "right" else -2
        self.rect.x += x_change
        if self.rect.x <= 0:
            self.direction = "right"
            self.rect.y += 30
        elif self.rect.x >= 736:
            self.direction = "left"
            self.rect.y += 30

    def update(self, bullet: Bullet):
        self.move()
        if bullet.rect.colliderect(self.rect):
            self.explode()
            bullet.reset()
            self.respawn()
            pygame.event.post(SCORE_POINT_EVENT)
