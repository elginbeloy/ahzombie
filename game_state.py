import pygame
from constants import *

class GameState:
    def __init__(self):
        self.ammo = MAX_AMMO
        self.reloading_progress = 0
        self.current_channel = 0
        self.num_channels = 5
        self.gunshot_channels = [pygame.mixer.Channel(i) for i in range(self.num_channels)]
        self.blast_position = None
        self.blast_timer = 0
        self.shots = []
