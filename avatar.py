import random
import pygame
import math
from constants import *
from loot import Loot

class Avatar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = avatar_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.desired_loot = None
        self.speed = 1

    def distance_to(self, rect):
      return math.sqrt((self.rect.x - rect.x)**2 + (self.rect.y - rect.y)**2)

    def update(self, game_state):
        if len(game_state.loot) > 1:
            game_state.avatar.desired_loot = min(game_state.loot, key=lambda loot: loot.distance_to(game_state.avatar.rect))

        if self.desired_loot != None:
            if self.rect.colliderect(self.desired_loot):
                game_state.loot.remove(self.desired_loot)
                if self.desired_loot.image == wood_image:
                    game_state.wood += self.speed
                elif self.desired_loot.image == metal_image:
                    game_state.metal += self.speed 
                elif self.desired_loot.image == ammo_image:
                    game_state.total_ammo += MAX_AMMO
                self.desired_loot = None
            else:
                if self.rect.x < self.desired_loot.rect.x:
                  self.rect.x += self.speed
                elif self.rect.x > self.desired_loot.rect.x:
                  self.rect.x -= self.speed
                
                if self.rect.y < self.desired_loot.rect.y:
                  self.rect.y += self.speed
                elif self.rect.y > self.desired_loot.rect.y:
                  self.rect.y -= self.speed
        else:
          if len(game_state.loot) == 1:
            game_state.avatar.desired_loot = game_state.loot[0]
          else:
            game_state.loot.append(Loot(ammo_image, random.randint(0, GAME_WIDTH), random.randint(0, GAME_HEIGHT)))