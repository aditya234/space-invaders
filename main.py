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


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


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

    # drawing the player
    player(playerX, playerY)
    # drawing the enemy
    enemy(enemyX, enemyY)
    # updating the window(state)
    pygame.display.update()
