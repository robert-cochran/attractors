import os
import pygame
import config_view


def setup(config):
    os.environ["SDL_VIDEO_CENTERED"]='1'
    pygame.init()
    pygame.display.set_caption(config.SET_CAPTION)
    screen = pygame.display.set_mode(config.SIZE)
    pygame.time.Clock().tick(config.FPS)
    screen.fill(config.BLACK)
    return screen
