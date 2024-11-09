import math
import pygame


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
