import pygame

pygame.mixer.pre_init(44100, -16, 5, 512)
pygame.init()
gunshot_sound = pygame.mixer.Sound('./assets/bang.wav')
gunshot_sound.set_volume(0.2)

reload_sound = pygame.mixer.Sound('./assets/reload.mp3')
reload_sound.set_volume(1.0)

GAME_WIDTH = 1200
GAME_HEIGHT = 800
FPS = 40
BG_COLOR = (90, 40, 0)
LOOT_CHANCE = 4 # 1 / LOOT_CHANCE

avatar_image = pygame.image.load("./assets/avatar.png")
avatar_image = pygame.transform.scale(avatar_image, (40, 40))

wood_image = pygame.image.load("./assets/wood.png")
wood_image = pygame.transform.scale(wood_image, (25, 25))

ammo_image = pygame.image.load("./assets/ammo.png")
ammo_image = pygame.transform.scale(ammo_image, (25, 25))

metal_image = pygame.image.load("./assets/metal.png")
metal_image = pygame.transform.scale(metal_image, (25, 25))

LOOT = [ammo_image, wood_image, metal_image]

zombie_image_1 = pygame.image.load("./assets/zombie_right.png")
zombie_image_1 = pygame.transform.scale(zombie_image_1, (40, 40))
zombie_image_2 = pygame.image.load("./assets/zombie_left.png")
zombie_image_2 = pygame.transform.scale(zombie_image_2, (40, 40))
zombie_image_3 = pygame.image.load("./assets/zombie.png")
zombie_image_3 = pygame.transform.scale(zombie_image_3, (40, 40))
dead_zombie_image = pygame.image.load("./assets/dead_zombie.png")
dead_zombie_image = pygame.transform.scale(dead_zombie_image, (40, 40))

MAX_AMMO = 20
RELOADING_TIME = 20
reloading_bar_height = 20
reloading_bar_color = (255, 0, 0)
ammo_bar_color = (255, 215, 0)

BLAST_DURATION = 2
MAX_SHOTS = 80
blast_image = pygame.image.load("./assets/blast.png")
blast_image = pygame.transform.scale(blast_image, (120, 120))