import pygame
import random
import math
from move import Movement

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

# Player
playerImg = pygame.image.load("player.png")
# Values for the player placement


player = Movement(370, 480, 0, 0)


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_enemies = 6

for i in range(num_enemies):

    enemyImg.append(pygame.image.load("enemy.png"))
    # making the enemy spawn random
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(2)
    enemyY_change.append(30)


# Bullet
bulletImg = pygame.image.load("bullet.png")
# making the enemy spawn random
bullet = Movement(0, 480, 0, 10)

# ready - you can't see the bullet on the screen
# fire - the bullet is currently moving
bullet_state = "ready"


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


def draw_player(x, y):
    # draw the image on the screen
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY):
    distance = math.sqrt(
        (math.pow(enemyX - bullet.x_pos, 2)) + (math.pow(enemyY - bullet.y_pos, 2))
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
                player.x_change = -5
            if event.key == pygame.K_RIGHT:
                player.x_change = 5
            # fire the bullet when we press space
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = pygame.mixer.Sound("laser.wav")
                    bullet_Sound.set_volume(0.2)
                    bullet_Sound.play()
                    # get the current x position of the spaceship
                    bullet.x_pos = player.x_pos
                    fire_bullet(bullet.x_pos, bullet.y_pos)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player.x_change = 0

    # adding collision with the wall for player
    player.x_pos += player.x_change
    if player.x_pos <= 0:
        player.x_pos = 0
    elif player.x_pos >= 736:
        player.x_pos = 736

    # enemy moving and  adding coliision with wall for enemy
    for i in range(num_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i])
        if collision:
            explosion_Sound = pygame.mixer.Sound("explosion.wav")
            explosion_Sound.set_volume(0.1)
            explosion_Sound.play()
            bullet.y_pos = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bullet.y_pos <= 0:
        bullet.y_pos = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bullet.x_pos, bullet.y_pos)
        bullet.y_pos -= bullet.y_change

    draw_player(player.x_pos, player.y_pos)
    show_score(textX, textY)
    pygame.display.update()
