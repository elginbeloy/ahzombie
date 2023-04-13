import pygame
from zombie import Zombie, ZombieGroup
from avatar import Avatar
from constants import *
from gun import main_rifle, smg

class GameState:
    def __init__(self):
        self.avatar = Avatar(GAME_WIDTH / 2, GAME_HEIGHT / 2)
        self.zombie_group = ZombieGroup()
        self.dead_zombie_group = pygame.sprite.Group()

        self.ammo = main_rifle.clip_size
        self.total_ammo = 40
        self.wood = 0
        self.metal = 0
        self.reloading_progress = 0
        self.current_channel = 0
        self.num_channels = 5
        self.gunshot_channels = [pygame.mixer.Channel(i) for i in range(self.num_channels)]
        self.blast_position = None
        self.blast_timer = 0
        self.shots = []
        self.loot = []
        self.current_gun = main_rifle
        self.secondary_gun = smg
