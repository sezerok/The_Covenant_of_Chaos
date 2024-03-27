import pygame
from sys import exit
from levels.settings import *
from levels.level import Level

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("TheCovenantOfChaos")

clock = pygame.time.Clock()
level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60) # fps control



