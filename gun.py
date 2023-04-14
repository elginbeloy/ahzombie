import pygame

class Gun():
  def __init__(self, name, bullet_size, clip_size, reload_time_sec, auto_fire_rate, image, crosshair_image, volume):
    self.name = name
    self.bullet_size = bullet_size
    self.clip_size = clip_size
    self.reload_time_sec = reload_time_sec
    self.auto_fire_rate = auto_fire_rate
    self.image = image
    self.big_image = pygame.transform.scale(self.image, (300, 100))
    self.small_image = pygame.transform.scale(self.image, (150, 50))
    self.crosshair = crosshair_image
    self.volume = volume

handgun_crosshair_image = pygame.image.load("./assets/smg_crosshair.png")
handgun_crosshair_image = pygame.transform.scale(handgun_crosshair_image, (200, 200))

rifle_crosshair_image = pygame.image.load("./assets/crosshair.png")
rifle_crosshair_image = pygame.transform.scale(rifle_crosshair_image, (200, 200))

smg_crosshair_image = pygame.image.load("./assets/rifle_crosshair2.png")
smg_crosshair_image = pygame.transform.scale(smg_crosshair_image, (200, 200))

shotgun_crosshair_image = pygame.image.load("./assets/rifle_crosshair3.png")
shotgun_crosshair_image = pygame.transform.scale(shotgun_crosshair_image, (200, 200))

handgun_image = pygame.image.load("./assets/handgun.png")
rifle_image = pygame.image.load("./assets/rifle.png")
smg_image = pygame.image.load("./assets/smg.png")
shotgun_image = pygame.image.load("./assets/shotgun.png")

handgun = Gun("Handgun", 4, 8, 2, False, handgun_image, handgun_crosshair_image, 0.5)
rifle = Gun("Assault Rifle", 10, 4, 4, False, rifle_image, rifle_crosshair_image, 0.75)
smg = Gun("SMG", 4, 40, 2, 10, smg_image, smg_crosshair_image, 0.5)
shotgun = Gun("Shotgun", 20, 2, 3, False, shotgun_image, shotgun_crosshair_image, 1)