import time

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        #инициализация
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill((0,250,0))
        self.rect = self.image.get_rect(topleft = pos)
        #движение игрока
        self.direction = pygame.math.Vector2(0,0)
        self.speed_player = 1
        self.gravity = 0.8
        self.jump = -16
    #фуккция перемещения
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            self.direction.x=1
        elif keys[pygame.K_a]:
            self.direction.x=-1
        else:
            self.direction.x = 0
        if keys[pygame.K_o]:
            self.speed_player = 16
        else:
            self.speed_player = 8

        if keys[pygame.K_SPACE]:
            self.jumping()
        else:
            self.gravity_apply()


    def gravity_apply(self):
        self.direction.y += self.gravity
        self.rect.y +=self.direction.y

    def jumping(self):
        self.direction.y = self.jump
        self.rect.y += self.direction.y
        self.direction.y = 0

    def update(self):
        self.move()
        self.rect.x+=self.direction.x*self.speed_player
