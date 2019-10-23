import pygame

# initialize pygame

pygame.init()

# creating screen of height 800 and width 600
screen = pygame.display.set_mode((800, 600))

# Title and logo
pygame.display.set_caption("Space war")
icon = pygame.image.load('./assets/project_logo.png')
pygame.display.set_icon(icon)
# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # filling rgb color on the screen
    screen.fill((0, 0, 0))
    # updating the window(state)
    pygame.display.update()
