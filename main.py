import pygame
from constants import *
from functions import *
from game_state import GameState

pygame.init()

def main():
    window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
    pygame.display.set_caption("AHZOMBIE!")
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    game_state = GameState()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                handle_mouse_click(game_state)

        render(window, game_state)
        update_game_state(game_state)

        clock.tick(FPS)

if __name__ == '__main__':
    main()
