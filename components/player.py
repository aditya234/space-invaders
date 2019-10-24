import pygame


class Player:

    def __init__(self, screen):
        self.playerImg = pygame.image.load('./assets/spaceship.png')
        self.playerX = 370
        self.playerY = 480
        self.playerX_change = 0
        self.screen = screen

    def show_player(self, x, y):
        self.screen.blit(self.playerImg, (x, y))
