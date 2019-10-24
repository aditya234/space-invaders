import math


class Mechanics:
    def is_collision(self, enemyX, enemyY, bulletX, bulletY):
        distance = math.sqrt(math.pow(bulletX - enemyX, 2) + math.pow(bulletY - enemyY, 2))
        if distance < 27:
            return True
        return False
