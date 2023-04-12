import random
import pygame
from constants import *

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = random.choice([zombie_image_1, zombie_image_2, zombie_image_3])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, avatar):
        if random.choice([True, False]):
            if self.rect.x < avatar.rect.x:
              self.rect.x += 1
            elif self.rect.x > avatar.rect.x:
              self.rect.x -= 1
        else:
            if self.rect.y < avatar.rect.y:
              self.rect.y += 1
            elif self.rect.y > avatar.rect.y:
              self.rect.y -= 1

class ZombieGroup(pygame.sprite.Group):
    def __init__(self, zombie_amount=20):
        super().__init__()
        self.zombie_amount = zombie_amount
        for i in range(zombie_amount):
            x = random.randint(0, GAME_WIDTH)
            y = random.randint(0, GAME_HEIGHT)
            zombie = Zombie(x, y)
            self.add(zombie)

    def update(self, avatar):
        if len(self) < self.zombie_amount:
            x = random.choice([-100, GAME_WIDTH+100])
            y = -100 + random.randrange(0, GAME_HEIGHT+200)
            zombie = Zombie(x, y)
            self.add(zombie)
        for zombie in self.sprites():
            zombie.update(avatar)
