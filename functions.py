import pygame
from blast import Blast
from constants import *

def create_opacity_overlay(crosshair_rect, opacity=192):
    overlay = pygame.Surface((GAME_WIDTH, GAME_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, opacity))
    circle_pos = crosshair_rect.center
    circle_radius = crosshair_rect.width // 2
    pygame.draw.circle(overlay, (0, 0, 0, 0), circle_pos, circle_radius)
    return overlay

def handle_mouse_click(game_state, zombie_group, dead_zombie_group):
    if game_state.ammo > 0:
        game_state.ammo -= 1
        game_state.gunshot_channels[game_state.current_channel].play(gunshot_sound)
        game_state.current_channel = (game_state.current_channel + 1) % game_state.num_channels
        cur_pos = pygame.mouse.get_pos()
        game_state.shots.append(cur_pos)
        if len(game_state.shots) > MAX_SHOTS:
            game_state.shots.pop(0)
        game_state.blast_position = cur_pos
        game_state.blast_timer = BLAST_DURATION
        tiny_blast_rect = pygame.Rect(cur_pos[0] - 4, cur_pos[1] - 4, 8, 8)
        collided_zombies = [zombie for zombie in zombie_group if tiny_blast_rect.colliderect(zombie.rect)]
        for zombie in collided_zombies:
            zombie.image = dead_zombie_image
            zombie_group.remove(zombie)
        dead_zombie_group.add(collided_zombies)

    if game_state.ammo == 0 and game_state.reloading_progress == RELOADING_TIME:
        game_state.ammo = MAX_AMMO
        game_state.reloading_progress = 0

def render(window, game_state, zombie_group, dead_zombie_group):
    window.fill(BG_COLOR)

    mouse_position = pygame.mouse.get_pos()
    crosshair_rect = crosshair_image.get_rect()
    crosshair_rect.center = mouse_position

    zombie_group.draw(surface=window)
    dead_zombie_group.draw(surface=window)

    # draw shots
    for pos in game_state.shots:
        pygame.draw.circle(window, (0, 0, 0, 100), pos, 4)

    opacity_overlay = create_opacity_overlay(crosshair_rect)
    window.blit(opacity_overlay, (0, 0))

    window.blit(crosshair_image, crosshair_rect)

    # Render the blast effect if it's active
    if game_state.blast_position and game_state.blast_timer > 0:
        blast = Blast(game_state.blast_position)
        window.blit(blast_image, blast.rect)
        game_state.blast_timer -= 1

    # Draw gun icon and reloading bar
    window.blit(gun_icon_image, (GAME_WIDTH - 300, 0))
    reloading_bar_width = int((game_state.reloading_progress / RELOADING_TIME) * 300)
    if reloading_bar_width > 0:
        pygame.draw.rect(window, reloading_bar_color, (GAME_WIDTH - 300, 100, reloading_bar_width, reloading_bar_height))
    else:
        ammo_bar_width = int((game_state.ammo / MAX_AMMO) * 300)
        pygame.draw.rect(window, ammo_bar_color, (GAME_WIDTH - 300, 100, ammo_bar_width, reloading_bar_height))

    pygame.display.update()

def update_game_state(game_state, zombie_group, dead_zombie_group):
    if game_state.reloading_progress < RELOADING_TIME and game_state.ammo == 0:
        game_state.reloading_progress += 1
