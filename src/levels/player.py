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
        self.speed_player = 8
        self.gravity = 0.8
        self.jump = -16
        self.j_val = False

    #фуккция перемещения
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # TODO: испроавить баг с камерой и передвижением
        # если закомментить блок ускорения, то камера фиксится
        # НО отваливается скорость при прыжке
        if keys[pygame.K_LSHIFT]:
            self.speed_player = 16
        else:
            self.speed_player = 8

        if keys[pygame.K_SPACE] and self.j_val==False:
            self.jumping()
            self.j_val=True

    def j(self):
        self.j_val = False
    def gravity_apply(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jumping(self):
        self.direction.y = self.jump
        self.rect.y += self.direction.y


    def update(self):
        self.move()
        # self.rect.x+=self.direction.x*self.speed_player
