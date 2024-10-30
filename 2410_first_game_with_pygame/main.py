import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
background = pygame.image.load("background.png")

# Ttile and Icon
pygame.display.set_caption("Galaxion")
icon = pygame.image.load("alien.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
# Values for the player placement
playerX = 370
playerY = 480
playerX_change = 0


# Enemy
enemyImg = pygame.image.load("enemy.png")
# making the enemy spawn random
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 30


# Bullet
bulletImg = pygame.image.load("bullet.png")
# making the enemy spawn random
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# ready - you can't see the bullet on the screen
# fire - the bullet is currently moving
bullet_state = "ready"


def player(x, y):
    # draw the image on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


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

        # if key is pressed check if its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            # fire the bullet when we press space
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # adding collision with the wall for player
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # enemy moving and  adding coliision with wall for enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change
    # bullet movement
    if bullet_state is "fire":
        fire_bullet(playerX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
