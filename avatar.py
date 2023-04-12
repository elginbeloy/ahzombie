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
        self.desired_loot = None

    def update(self, game_state):
        if self.desired_loot != None:
            if self.rect.colliderect(self.desired_loot):
                game_state.loot.remove(self.desired_loot)
                self.desired_loot = None
            else:
                if self.rect.x < self.desired_loot.rect.x:
                  self.rect.x += 1
                elif self.rect.x > self.desired_loot.rect.x:
                  self.rect.x -= 1
                
                if self.rect.y < self.desired_loot.rect.y:
                  self.rect.y += 1
                elif self.rect.y > self.desired_loot.rect.y:
                  self.rect.y -= 1