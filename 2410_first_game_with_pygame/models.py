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
