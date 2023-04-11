import random
import pygame

pygame.init()

GAME_WIDTH = 1200
GAME_HEIGHT = 800
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("AHZOMBIE!")
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 40

BG_COLOR = (90, 40, 0)

zombie_image = pygame.image.load("./zombie.png")
zombie_image = pygame.transform.scale(zombie_image, (40, 40))
dead_zombie_image = pygame.image.load("./dead_zombie.png")
dead_zombie_image = pygame.transform.scale(dead_zombie_image, (40, 40))

gun_icon_image = pygame.image.load("./gun_icon.png")
gun_icon_image = pygame.transform.scale(gun_icon_image, (300, 100))

crosshair_image = pygame.image.load("./crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (100, 100))

ammo = 10 # should take this into account before making reload
RELOADING_TIME = 20
reloading_progress = 0
reloading_bar_height = 20
reloading_bar_color = (255, 0, 0)


class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = zombie_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

zombie_group = pygame.sprite.Group()
dead_zombie_group = pygame.sprite.Group()
for i in range(160):
    x = random.randint(0, GAME_WIDTH)
    y = random.randint(0, GAME_HEIGHT)
    zombie = Zombie(x, y)
    zombie_group.add(zombie)

blast_image = pygame.image.load("./blast.png")
blast_image = pygame.transform.scale(blast_image, (40, 40))
blast_position = None
blast_timer = 0
BLAST_DURATION = 4

class Blast(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = blast_image
        self.rect = self.image.get_rect(center=pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if reloading_progress == RELOADING_TIME:
                # Reset reloading progress after shooting
                reloading_progress = 0
                cur_pos = pygame.mouse.get_pos()
                blast_position = cur_pos
                blast_timer = BLAST_DURATION

                # Check for collisions between blast and zombies
                blast = Blast(blast_position)
                collided_zombies = pygame.sprite.spritecollide(
                    blast, zombie_group, dokill=True, collided=None
                )
                for zombie in collided_zombies:
                    zombie.image = dead_zombie_image
                dead_zombie_group.add(collided_zombies)

    window.fill(BG_COLOR)

    mouse_position = pygame.mouse.get_pos()
    crosshair_rect = crosshair_image.get_rect()
    crosshair_rect.center = mouse_position
    window.blit(crosshair_image, crosshair_rect)

    zombie_group.draw(surface=window)
    dead_zombie_group.draw(surface=window)

    # Render the blast effect if it's active
    if blast_position and blast_timer > 0:
        window.blit(blast_image, blast.rect)
        blast_timer -= 1

    # Draw gun icon and reloading bar
    window.blit(gun_icon_image, (GAME_WIDTH - 300, 0))
    reloading_bar_width = int((reloading_progress / RELOADING_TIME) * 300)
    pygame.draw.rect(window, reloading_bar_color, (GAME_WIDTH - 300, 100, reloading_bar_width, reloading_bar_height))

    # Update reloading progress
    if reloading_progress < RELOADING_TIME:
        reloading_progress += 1
        
    pygame.display.update()
    clock.tick(FPS)
