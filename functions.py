import pygame
import random
from loot import Loot
from blast import Blast
from constants import *
from gun import *

pygame.font.init()
font = pygame.font.SysFont("Roboto", 24)

def create_opacity_overlay(crosshair_rect, opacity=192):
    overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, opacity))
    circle_pos = crosshair_rect.center
    circle_radius = crosshair_rect.width // 2
    pygame.draw.circle(overlay, (0, 0, 0, 0), circle_pos, circle_radius)
    return overlay

def handle_mouse_click(game_state):
    reload_time = game_state.current_gun.reload_time_sec * FPS
    if game_state.ammo > 0:
        game_state.ammo -= 1
        game_state.current_channel = (game_state.current_channel + 1) % game_state.num_channels
        shot_sound = gunshot_sound
        shot_sound.set_volume(game_state.current_gun.volume)
        game_state.gunshot_channels[game_state.current_channel].play(gunshot_sound)
        cur_pos = pygame.mouse.get_pos()
        game_state.shots.append({"pos": cur_pos, "size": game_state.current_gun.bullet_size})
        if len(game_state.shots) > MAX_SHOTS:
            game_state.shots.pop(0)
        game_state.blast_position = cur_pos
        game_state.blast_timer = BLAST_DURATION
        bullet_size = game_state.current_gun.bullet_size
        collision_blast_rect = pygame.Rect(cur_pos[0] - (bullet_size / 2), cur_pos[1] - (bullet_size / 2), bullet_size, bullet_size)
        collided_zombies = [zombie for zombie in game_state.zombie_group if collision_blast_rect.colliderect(zombie.rect)]
        for zombie in collided_zombies:
            zombie.image = dead_zombie_image
            game_state.zombie_group.remove(zombie)
            if random.randrange(0, LOOT_CHANCE) == 1:
                game_state.loot.append(Loot(random.choice(LOOT), *zombie.rect.center))
        game_state.dead_zombie_group.add(collided_zombies)
        if game_state.ammo == 0:
            game_state.current_channel = (game_state.current_channel + 1) % game_state.num_channels
            game_state.gunshot_channels[game_state.current_channel].play(reload_sound)
    if game_state.ammo == 0 and game_state.reloading_progress == reload_time and game_state.total_ammo > 0:
        game_state.current_channel = (game_state.current_channel + 1) % game_state.num_channels
        game_state.gunshot_channels[game_state.current_channel].play(reload_sound)
        game_state.ammo = game_state.current_gun.clip_size
        game_state.total_ammo -= game_state.current_gun.clip_size
        game_state.reloading_progress = 0

def render(window, game_state):
    window.fill(BG_COLOR)

    mouse_position = pygame.mouse.get_pos()
    crosshair_rect = game_state.current_gun.crosshair.get_rect()
    crosshair_rect.center = mouse_position

    game_state.dead_zombie_group.draw(surface=window)
    # draw loot
    for loot in game_state.loot:
        window.blit(loot.image, loot.rect)
    # draw shots
    for shot in game_state.shots:
        pygame.draw.circle(window, (0, 0, 0), shot["pos"], shot["size"] / 2)
    # drive alive zombies
    game_state.zombie_group.draw(surface=window)
    # draw avatar
    window.blit(game_state.avatar.image, game_state.avatar.rect)

    reload_time = game_state.current_gun.reload_time_sec * FPS
    if game_state.ammo > 0 or game_state.reloading_progress >= reload_time:
      opacity_overlay = create_opacity_overlay(crosshair_rect)
      window.blit(opacity_overlay, (0, 0))
      window.blit(game_state.current_gun.crosshair, crosshair_rect)

    # Render the blast effect if it's active
    if game_state.blast_position and game_state.blast_timer > 0:
        blast = Blast(game_state.blast_position)
        window.blit(blast_image, blast.rect)
        game_state.blast_timer -= 1

    window.blit(game_state.current_gun.big_image, (GAME_WIDTH - 300, 0))
    window.blit(game_state.secondary_gun.small_image, (GAME_WIDTH - 150, 140))
    # Draw amm and reloading bar
    reloading_bar_width = int((game_state.reloading_progress / reload_time) * 300)
    if reloading_bar_width > 0:
        pygame.draw.rect(window, reloading_bar_color, (GAME_WIDTH - reloading_bar_width, 100, reloading_bar_width, reloading_bar_height))
    else:
        ammo_bar_width = int((game_state.ammo / game_state.current_gun.clip_size) * 300)
        pygame.draw.rect(window, ammo_bar_color, (GAME_WIDTH - ammo_bar_width, 100, ammo_bar_width, reloading_bar_height))

    # Draw resource amounts
    ammo_amount_text = font.render(str(game_state.total_ammo), True, (255, 255, 255))
    metal_amount_text = font.render(str(game_state.metal), True, (255, 255, 255))
    wood_amount_text = font.render(str(game_state.wood), True, (255, 255, 255))
    window.blit(ammo_image, (10, 20))
    window.blit(metal_image, (10, 60))
    window.blit(wood_image, (10, 100))
    window.blit(ammo_amount_text, (50, 25))
    window.blit(metal_amount_text, (50, 65))
    window.blit(wood_amount_text, (50, 105))

    pygame.display.update()

def update_game_state(game_state):
    game_state.avatar.update(game_state)
    game_state.zombie_group.update(game_state.avatar)
    reload_time = game_state.current_gun.reload_time_sec * FPS
    if game_state.reloading_progress < reload_time and game_state.ammo == 0:
        game_state.reloading_progress += 1
