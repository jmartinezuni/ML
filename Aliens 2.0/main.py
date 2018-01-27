import pygame
import sys
import os
from process import *

def main_loop(game_creen_base, game_clock, FPS):
    running = True
    while running:
        for event in pygame.event.get():     
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RETURN:
                    game_loop(game_screen_base, game_clock, FPS)
                #elif event.key == pygame.K_ESCAPE:
                    #running = False
        draw_title(game_screen_base)
        game_clock.tick(FPS)

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '0'
    FPS = 60
    pygame.init() 
    game_screen_base = pygame.display.set_mode((500, 650))
    pygame.display.set_caption("SpaceCraft")
    game_clock = pygame.time.Clock()
    main_loop(game_screen_base, game_clock, FPS)
    pygame.quit()
