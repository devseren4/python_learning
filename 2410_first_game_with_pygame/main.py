import pygame
from models import Player, Bullet, Enemy, SCORE_POINT_EVENT

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

enemy_group = pygame.sprite.Group()

for i in range(6):
    enemy = Enemy()
    enemy_group.add(enemy)

bullet = Bullet()
bullet_group = pygame.sprite.GroupSingle(bullet)

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
over_font = pygame.font.Font("freesansbold.ttf", 64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def hide_all_enemies():
    for enemy in enemy_group.sprites():
        enemy.rect.y = 2000


def did_enemy_win():
    for enemy in enemy_group.sprites():
        if enemy.rect.y > 440:
            return True
    return False


running = True
while running:
    screen.fill((31, 62, 90))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SCORE_POINT_EVENT.type:
            score_value += 1

    if did_enemy_win():
        hide_all_enemies()
        game_over_text()

    enemy_group.update(bullet)
    enemy_group.draw(screen)

    bullet_group.update(player)
    bullet_group.draw(screen)

    player_group.update()
    player_group.draw(screen)

    show_score(textX, textY)
    pygame.display.update()
