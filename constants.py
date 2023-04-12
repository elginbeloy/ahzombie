import pygame

pygame.mixer.pre_init(44100, -16, 5, 512)
pygame.init()
gunshot_sound = pygame.mixer.Sound('./assets/bang.wav')
gunshot_sound.set_volume(0.2)

GAME_WIDTH = 1200
GAME_HEIGHT = 800
FPS = 40
BG_COLOR = (90, 40, 0)

zombie_image_1 = pygame.image.load("./assets/zombie_right.png")
zombie_image_1 = pygame.transform.scale(zombie_image_1, (40, 40))
zombie_image_2 = pygame.image.load("./assets/zombie_left.png")
zombie_image_2 = pygame.transform.scale(zombie_image_2, (40, 40))
zombie_image_3 = pygame.image.load("./assets/zombie.png")
zombie_image_3 = pygame.transform.scale(zombie_image_3, (40, 40))
dead_zombie_image = pygame.image.load("./assets/dead_zombie.png")
dead_zombie_image = pygame.transform.scale(dead_zombie_image, (40, 40))

gun_icon_image = pygame.image.load("./assets/gun_icon.png")
gun_icon_image = pygame.transform.scale(gun_icon_image, (300, 100))

crosshair_image = pygame.image.load("./assets/crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (200, 200))

MAX_AMMO = 40
RELOADING_TIME = 20
reloading_bar_height = 20
reloading_bar_color = (255, 0, 0)
ammo_bar_color = (255, 215, 0)

BLAST_DURATION = 2
MAX_SHOTS = 80
blast_image = pygame.image.load("./assets/blast.png")
blast_image = pygame.transform.scale(blast_image, (120, 120))