import pygame
import random

# initialize pygame

pygame.init()

# creating screen of width 800 and height 600
screen = pygame.display.set_mode((800, 600))

# Title and logo
pygame.display.set_caption("Space war")
icon = pygame.image.load('./assets/project_logo.png')
pygame.display.set_icon(icon)

# background
background = pygame.image.load('./assets/background.jpg')

# player
playerImg = pygame.image.load('./assets/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# enemy invader
enemyImg = pygame.image.load('./assets/space_invader.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(0, 150)
enemyX_change = 10
enemyY_change = 40

# bullet
# ready state - you can't see the bullet on the screen
# fire state - the bullet is currently in motion
bulletImg = pygame.image.load('./assets/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 20
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # x+12 will get the bullet to the center of our spaceship
    # y+10 will get the bullet to the notch of the spaceship
    screen.blit(bulletImg, (x + 12, y + 10))


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
                playerX_change = 10
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0
    # moving player horizontally
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # moving the enemy
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 10
        enemyY += enemyY_change
    if enemyX >= 736:
        enemyX_change = -10
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bullet_state = "ready"
        bulletY = 480
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    # drawing the player
    player(playerX, playerY)
    # drawing the enemy
    enemy(enemyX, enemyY)
    # updating the window(state)
    pygame.display.update()
