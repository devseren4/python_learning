import math
import pygame
from pygame.rect import Rect
from pygame.sprite import Sprite


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


class Box:
    def __init__(self, **kwargs):
        self.data = kwargs.get("data", {})
        self.x_pos = kwargs.get("x_pos", 0)
        self.y_pos = kwargs.get("y_pos", 0)
        self.x_change = kwargs.get("x_change", 0)
        self.y_change = kwargs.get("y_change", 0)
        img_file = kwargs.get("img_file")
        if img_file:
            self.img = pygame.image.load(img_file)

    def draw(self, screen: pygame.Surface, offset=(0, 0)):
        screen.blit(self.img, (self.x_pos + offset[0], self.y_pos + offset[1]))

    def collides(self, other, distance=27):
        current_distance = math.sqrt(
            (math.pow(self.x_pos - other.x_pos, 2))
            + (math.pow(self.y_pos - other.y_pos, 2))
        )
        if current_distance < distance:
            return True
        else:
            return False
