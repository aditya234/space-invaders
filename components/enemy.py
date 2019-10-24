import pygame
import random


class Enemies:
    def __init__(self, number_of_enemies, screen):
        self.enemyImg = []
        self.enemyX = []
        self.enemyY = []
        self.enemyX_change = []
        self.enemyY_change = []
        self.num_of_enemies = number_of_enemies
        self.screen = screen

    def init_enemies(self):
        for i in range(self.num_of_enemies):
            self.enemyImg.append(pygame.image.load('./assets/space_invader.png'))
            self.enemyX.append(random.randint(0, 736))
            self.enemyY.append(random.randint(0, 150))
            self.enemyX_change.append(10)
            self.enemyY_change.append(40)

    def show_enemy(self, x, y, i):
        self.screen.blit(self.enemyImg[i], (x, y))
