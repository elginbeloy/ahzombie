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
                if self.desired_loot.image == wood_image:
                    game_state.wood += 1
                elif self.desired_loot.image == metal_image:
                    game_state.metal += 1
                elif self.desired_loot.image == ammo_image:
                    game_state.total_ammo += MAX_AMMO
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