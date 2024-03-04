import pygame
import sys

import screen_resolution

pygame.init()

screen_resol = screen_resolution.choose_resolution()

screen = pygame.display.set_mode(screen_resol, pygame.FULLSCREEN)

running = True
while running:
    for event in pygame.event.get():
        screen.fill((0,0,0))
        myfont = pygame.font.SysFont("Britannic Bold", 40)
        nlabel = myfont.render("Welcome Start Screen", 1, (255, 0, 0))
        if event.type == pygame.MOUSEBUTTONDOWN:
            quit()
        screen.blit(nlabel, (screen_resol[0]/2, screen_resol[1]/2))
        pygame.display.flip()




pygame.quit()
sys.exit()

def quit():
    pygame.quit()
    sys.exit()

def start_game():
    print("halo")

def razraby_ne_dauni():
    print("halo")