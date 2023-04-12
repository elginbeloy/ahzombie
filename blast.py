import pygame
from constants import *

class Blast(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = blast_image
        self.rect = self.image.get_rect(center=pos)
