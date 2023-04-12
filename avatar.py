import random
import pygame
from constants import *

class Avatar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = avatar_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
      pass
      #if random.randrange(0, 5) == 2:
      #  self.rect.x -= 1
      #if random.randrange(0, 5) == 2:
      #  self.rect.y -= 1
