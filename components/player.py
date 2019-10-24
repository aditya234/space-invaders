import pygame


class Player:

    def __init__(self):
        self.playerImg = pygame.image.load('./assets/spaceship.png')
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0

    def show_player(self, screen, x, y):
        screen.blit(self.playerImg, (x, y))
