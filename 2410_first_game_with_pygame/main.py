import pygame
import random
import math

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
enemyX = random.randint(0, 735)
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
score = 0


def player(x, y):
    # draw the image on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    )
    if distance < 27:
        return True
    else:
        return False


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
                if bullet_state is "ready":
                    # get the current x position of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
