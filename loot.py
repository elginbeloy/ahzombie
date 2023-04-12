import pygame
import math
from constants import *

class Loot(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def distance_to(self, rect):
      return math.sqrt((self.rect.x - rect.x)**2 + (self.rect.y - rect.y)**2)