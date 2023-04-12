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
      if random.randrange(0, 4) == 1:
        if self.rect.x < avatar.rect.x:
          self.rect.x += 1
        elif self.rect.x > avatar.rect.x:
          self.rect.x -= 1
        
        if self.rect.y < avatar.rect.y:
          self.rect.y += 1
        elif self.rect.y > avatar.rect.y:
          self.rect.y -= 1

class ZombieGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        for i in range(20):
            x = random.randint(0, GAME_WIDTH)
            y = random.randint(0, GAME_HEIGHT)
            zombie = Zombie(x, y)
            self.add(zombie)

    def update(self, avatar):
        for zombie in self.sprites():
            zombie.update(avatar)
