from typing import List
import pygame
import random
import math
from models import Box, Player, Bullet

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# background sound
background_sound = pygame.mixer.Sound("background.wav")
background_sound.set_volume(0.1)
background_sound.play(-1)

# Ttile and Icon
pygame.display.set_caption("Galaxion")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

player = Player()
player_group = pygame.sprite.GroupSingle(player)

enemies: List[Box] = []

for i in range(6):
    x_pos = random.randint(0, 735)
    y_pos = random.randint(50, 150)
    x_change = 2
    y_change = 30
    enemy = Box(
        x_pos=x_pos,
        y_pos=y_pos,
        x_change=x_change,
        y_change=y_change,
        img_file="enemy.png",
    )
    enemies.append(enemy)

bullet = Bullet()
bullet_group = pygame.sprite.GroupSingle(bullet)

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

# Game Over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def fire_bullet():
    global bullet
    bullet.data["state"] = "fire"
    bullet.draw(screen, (16, 10))


# Game loop
running = True
while running:

    # changing the screen color
    screen.fill((31, 62, 90))
    # background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # enemy moving and  adding coliision with wall for enemy
    for i in range(len(enemies)):

        # Game Over
        if enemies[i].y_pos > 440:
            for j in range(len(enemies)):
                enemies[j].y_pos = 2000
            game_over_text()
            break

        enemies[i].x_pos += enemies[i].x_change
        if enemies[i].x_pos <= 0:
            enemies[i].x_change = 2
            enemies[i].y_pos += enemies[i].y_change
        elif enemies[i].x_pos >= 736:
            enemies[i].x_change = -2
            enemies[i].y_pos += enemies[i].y_change

        if bullet.rect.colliderect(
            pygame.rect.Rect(enemies[i].x_pos, enemies[i].y_pos, 64, 64)
        ):
            explosion_Sound = pygame.mixer.Sound("explosion.wav")
            explosion_Sound.set_volume(0.1)
            explosion_Sound.play()
            bullet.reset()
            score_value += 1
            enemies[i].x_pos = random.randint(0, 735)
            enemies[i].y_pos = random.randint(50, 150)

        enemies[i].draw(screen)

    # bullet Box

    bullet_group.update(player)
    bullet_group.draw(screen)

    player_group.update()
    player_group.draw(screen)

    show_score(textX, textY)
    pygame.display.update()
