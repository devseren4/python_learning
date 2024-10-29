import random
import math
import pygame
import os
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer")

BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))


# CREATE THE PLAYER
class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)


# CREATE THE BACKGROUND
def get_background(name):
    image = pygame.image.load(join("assets", "Background", name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    return tiles, image


# DRAW THE BACKGROUND
def draw(window, background, bg_image):
    for tile in background:
        window.blit(bg_image, tile)

    pygame.display.update()


# LOOP THE MAIN WINDOW
def main(window):
    clock = pygame.time.Clock()
    background, bg_image = get_background("Blue.png")

    run = True
    while run:
        # ensure that our while loop is gonna run 60 frames per sec
        clock.tick(FPS)

        # check if the user quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        draw(window, background, bg_image)

    pygame.quit()
    quit()


# we only call the main function if we run this file directly
if __name__ == "__main__":
    main(window)
