import pygame
import sys

def choose_resolution():

    pygame.init()

    modes = pygame.display.list_modes()

    best_mode = modes[0] if modes else (800, 600)
    return best_mode