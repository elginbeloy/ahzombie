# TODO: Guy in middle of screen
# TODO: zombies drop things guy goes to grab them you must kill zombies to protect him
# TODO: You can build a base and upgrade it to protect him

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

zombie_image = pygame.image.load("./zombie_right.png")
zombie_image = pygame.transform.scale(zombie_image, (40, 40))
dead_zombie_image = pygame.image.load("./dead_zombie.png")
dead_zombie_image = pygame.transform.scale(dead_zombie_image, (40, 40))

gun_icon_image = pygame.image.load("./gun_icon.png")
gun_icon_image = pygame.transform.scale(gun_icon_image, (300, 100))

crosshair_image = pygame.image.load("./crosshair.png")
crosshair_image = pygame.transform.scale(crosshair_image, (200, 200))

MAX_AMMO = 10
ammo = MAX_AMMO
RELOADING_TIME = 20
reloading_progress = 0
reloading_bar_height = 20
reloading_bar_color = (255, 0, 0)
ammo_bar_color = (255, 215, 0)

def create_opacity_overlay(crosshair_rect, opacity=192):
    overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, opacity))
    circle_pos = crosshair_rect.center
    circle_radius = crosshair_rect.width // 2
    pygame.draw.circle(overlay, (0, 0, 0, 0), circle_pos, circle_radius)
    return overlay

class Zombie(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = zombie_image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

zombie_group = pygame.sprite.Group()
dead_zombie_group = pygame.sprite.Group()
for i in range(40):
    x = random.randint(0, GAME_WIDTH)
    y = random.randint(0, GAME_HEIGHT)
    zombie = Zombie(x, y)
    zombie_group.add(zombie)

blast_image = pygame.image.load("./blast.png")
blast_image = pygame.transform.scale(blast_image, (120, 120))
blast_position = None
blast_timer = 0
BLAST_DURATION = 2
shots = []

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
            if ammo > 0:
                ammo -= 1
                cur_pos = pygame.mouse.get_pos()
                shots.append(cur_pos)
                if len(shots) > 20:
                    shots.pop(0)
                blast_position = cur_pos
                blast_timer = BLAST_DURATION
                blast = Blast(blast_position)
                tiny_blast_rect = pygame.Rect(cur_pos[0] - 4, cur_pos[1] - 4, 8, 8)
                collided_zombies = [zombie for zombie in zombie_group if tiny_blast_rect.colliderect(zombie.rect)]
                for zombie in collided_zombies:
                    zombie.image = dead_zombie_image
                    zombie_group.remove(zombie)
                dead_zombie_group.add(collided_zombies)
                
            if ammo == 0 and reloading_progress == RELOADING_TIME:
                ammo = MAX_AMMO
                reloading_progress = 0

    window.fill(BG_COLOR)

    mouse_position = pygame.mouse.get_pos()
    crosshair_rect = crosshair_image.get_rect()
    crosshair_rect.center = mouse_position

    zombie_group.draw(surface=window)
    dead_zombie_group.draw(surface=window)

    # draw shots
    for pos in shots:
        pygame.draw.circle(window, (0, 0, 0, 100), pos, 4)

    opacity_overlay = create_opacity_overlay(crosshair_rect)
    window.blit(opacity_overlay, (0, 0))

    window.blit(crosshair_image, crosshair_rect)

    # Render the blast effect if it's active
    if blast_position and blast_timer > 0:
        window.blit(blast_image, blast.rect)
        blast_timer -= 1

    # Draw gun icon and reloading bar
    window.blit(gun_icon_image, (GAME_WIDTH - 300, 0))
    reloading_bar_width = int((reloading_progress / RELOADING_TIME) * 300)
    if reloading_bar_width > 0:
        pygame.draw.rect(window, reloading_bar_color, (GAME_WIDTH - 300, 100, reloading_bar_width, reloading_bar_height))
    else:
        ammo_bar_width = int((ammo / MAX_AMMO) * 300)
        pygame.draw.rect(window, ammo_bar_color, (GAME_WIDTH - 300, 100, ammo_bar_width, reloading_bar_height))
    
    # Update reloading progress
    if reloading_progress < RELOADING_TIME and ammo == 0:
        reloading_progress += 1
        
    pygame.display.update()
    clock.tick(FPS)