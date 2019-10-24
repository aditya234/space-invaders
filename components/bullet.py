import pygame


# bullet
# ready state - you can't see the bullet on the screen
# fire state - the bullet is currently in motion
class Bullet:
    def __init__(self, screen):
        self.bulletImg = pygame.image.load('./assets/bullet.png')
        self.bulletX = 0
        self.bulletY = 480
        self.bulletX_change = 0
        self.bulletY_change = 20
        self.bullet_state = "ready"
        self.screen = screen

    def fire_bullet(self, x, y):
        self.bullet_state = "fire"
        # x+12 will get the bullet to the center of our spaceship
        # y+10 will get the bullet to the notch of the spaceship
        self.screen.blit(self.bulletImg, (x + 12, y + 10))
