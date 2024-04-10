import pygame
# TODO поставить текстурки
class Heal(pygame.sprite.Sprite):
    def __init__(self,size,pos):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((0,0,255))
        self.flag = 2
        self.rect = self.image.get_rect(topleft=pos)
    def healing(self,hp):
        if self.flag != 0 and hp+10 <= 100:
            self.flag -= 1
            self.image.fill((0, 0, 100))
            return 10
        else:
             return 0
    def update(self, x_shitf):
        self.rect.x += x_shitf