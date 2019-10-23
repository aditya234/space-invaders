import pygame

# initialize pygame

pygame.init()

# creating screen of height 800 and width 600
screen = pygame.display.set_mode((800, 600))

running = True
# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
