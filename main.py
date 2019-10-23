import pygame

# initialize pygame

pygame.init()

# creating screen of width 800 and height 600
screen = pygame.display.set_mode((800, 600))

# Title and logo
pygame.display.set_caption("Space war")
icon = pygame.image.load('./assets/project_logo.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('./assets/spaceship.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# game loop
running = True
while running:
    # filling rgb color on the screen
    screen.fill((0, 0, 0))
    # capturing events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # drawing the player
    player()
    # updating the window(state)
    pygame.display.update()
