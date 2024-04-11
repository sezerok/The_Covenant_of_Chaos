import pygame

class Tile(pygame.sprite.Sprite):
    # TODO: загрузить текстуры шипов
    def __init__(self, pos, size, type_of_tile):
        super().__init__()
        # self.image = pygame.Surface((size, size)) # основа-плитка
        # self.image.fill('grey') # заливка плитки платформы
        # self.main_ground_image = pygame.image.load('levels/res/ground_main.png').convert()
        # self.image = pygame.transform.scale(self.main_ground_image, (size, size))
        self.select_image(type_of_tile, size)
        self.rect = self.image.get_rect(topleft=pos) # определение расположения

    def select_image(self, type_of_tile, size):
        if type_of_tile == "thorn":
            self.image = pygame.Surface((size, size))
            self.image.fill((255, 0, 0))
        elif type_of_tile == "heal_bottle":
            self.image = pygame.Surface((size, size))
            self.image.fill((0, 0, 255))
        else:
            self.main_ground_image = pygame.image.load(f'levels/res/{type_of_tile}.png').convert_alpha()
            self.image = pygame.transform.scale(self.main_ground_image, (size, size))

    def update(self, x_shitf):
        self.rect.x += x_shitf

class Thorn(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)
    def damage(self):
        return 10

class Heal(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)
        self.flag = 2
    def healing(self,hp):
        if self.flag != 0 and hp+10 <= 100:
            self.flag -= 1
            self.image.fill((0, 0, 100))
            return 10
        else:
             return 0