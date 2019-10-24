import pygame
import random
import math
from pygame import mixer
from components.player import Player

# initialize pygame

pygame.init()

# creating screen of width 800 and height 600
screen = pygame.display.set_mode((800, 600))

# background music
mixer.music.load('./assets/music/theme_music.wav')
mixer.music.play(-1)

# Title and logo
pygame.display.set_caption("Space war")
icon = pygame.image.load('./assets/project_logo.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('./assets/background.jpg')

# score
score_value = 0

# player
player = Player()

# enemy invader/s
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('./assets/space_invader.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))
    enemyX_change.append(10)
    enemyY_change.append(40)

# bullet
# ready state - you can't see the bullet on the screen
# fire state - the bullet is currently in motion
bulletImg = pygame.image.load('./assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # x+12 will get the bullet to the center of our spaceship
    # y+10 will get the bullet to the notch of the spaceship
    screen.blit(bulletImg, (x + 12, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bulletX - enemyX, 2) + math.pow(bulletY - enemyY, 2))
    if distance < 27:
        return True
    return False


def display_score(x, y):
    score_font = pygame.font.SysFont("comicsansmsttf", 36)
    text = score_font.render("Score - {0}".format(score_value), True, (255, 255, 255))
    screen.blit(text, (x, y))


# game loop
running = True
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
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_sound = pygame.mixer.Sound('./assets/music/fire.wav')
                bullet_sound.play()
                bulletX = player.playerX
                fire_bullet(bulletX, bulletY)
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
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 10
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -10
            enemyY[i] += enemyY_change[i]
        # collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            collision_sound = pygame.mixer.Sound('./assets/music/explosion.wav')
            collision_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(0, 150)
        # drawing the enemies
        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # drawing the player
    player.show_player(screen=screen, x=player.playerX, y=player.playerY)
    # displaying the score
    display_score(0, 0)
    # updating the window(state)
    pygame.display.update()
