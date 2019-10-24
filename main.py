import pygame
import random
from pygame import mixer

from components.bullet import Bullet
from components.enemy import Enemies
from components.mechanics import Mechanics
from components.player import Player

# initialize pygame

pygame.init()
# creating screen of width 800 and height 600
screen = pygame.display.set_mode((800, 600))
# game status
running = True
# background
background = pygame.image.load('./assets/background.jpg')
# score
score_value = 0

# player
player = Player(screen=screen)

# enemy invader/s
enemies = Enemies(screen=screen, number_of_enemies=6)
enemies.init_enemies()

# bullet
bullet = Bullet(screen=screen)

# mechanics
mechanics = Mechanics()


def set_defaults():
    # background music
    mixer.music.load('./assets/music/theme_music.wav')
    mixer.music.play(-1)

    # Title and logo
    pygame.display.set_caption("Space war")
    icon = pygame.image.load('./assets/project_logo.png')
    pygame.display.set_icon(icon)


def display_score(x, y):
    score_font = pygame.font.SysFont("comicsansmsttf", 36)
    text = score_font.render("Score - {0}".format(score_value), True, (255, 255, 255))
    screen.blit(text, (x, y))


# game loop
set_defaults()
while running:
    # background image
    screen.blit(background, (0, 0))
    # capturing events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.playerX_change = 10
            if event.key == pygame.K_LEFT:
                player.playerX_change = -10
            if event.key == pygame.K_SPACE and bullet.bullet_state == "ready":
                bullet.bullet_sound = pygame.mixer.Sound('./assets/music/fire.wav')
                bullet.bullet_sound.play()
                bullet.bulletX = player.playerX
                bullet.fire_bullet(x=bullet.bulletX, y=bullet.bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                player.playerX_change = 0
    # moving player horizontally
    player.playerX += player.playerX_change
    if player.playerX <= 0:
        player.playerX = 0
    if player.playerX >= 736:
        player.playerX = 736

    # moving the enemies
    for i in range(enemies.num_of_enemies):
        enemies.enemyX[i] += enemies.enemyX_change[i]
        if enemies.enemyX[i] <= 0:
            enemies.enemyX_change[i] = 10
            enemies.enemyY[i] += enemies.enemyY_change[i]
        elif enemies.enemyX[i] >= 736:
            enemies.enemyX_change[i] = -10
            enemies.enemyY[i] += enemies.enemyY_change[i]
        # collision
        collision = mechanics.is_collision(enemies.enemyX[i], enemies.enemyY[i], bullet.bulletX, bullet.bulletY)
        if collision:
            collision_sound = pygame.mixer.Sound('./assets/music/explosion.wav')
            collision_sound.play()
            bullet.bulletY = 480
            bullet.bullet_state = "ready"
            score_value += 1
            enemies.enemyX[i] = random.randint(0, 736)
            enemies.enemyY[i] = random.randint(0, 150)
        # drawing the enemies
        enemies.show_enemy(x=enemies.enemyX[i], y=enemies.enemyY[i], i=i)

    # bullet movement
    if bullet.bulletY <= 0:
        bullet.bullet_state = "ready"
        bullet.bulletY = 480
    if bullet.bullet_state is "fire":
        bullet.fire_bullet(bullet.bulletX, bullet.bulletY)
        bullet.bulletY -= bullet.bulletY_change

    # drawing the player
    player.show_player(x=player.playerX, y=player.playerY)
    # displaying the score
    display_score(0, 0)
    # updating the window(state)
    pygame.display.update()
