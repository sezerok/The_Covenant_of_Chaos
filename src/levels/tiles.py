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
        self.start_pos = pos
        self.rect = self.image.get_rect(topleft = self.start_pos) # определение расположения


    def return_rect(self):

        return (self.rect.x, self.rect.y)

    def spawnpoint(self, pos):
        #print((self.rect.x, self.rect.y))
        #print((int(self.rect.x), int(self.rect.y)))
        self.start_pos = pos
        #print(pos)

    def restart(self):
        self.rect = self.image.get_rect(topleft = self.start_pos)

    def select_image(self, type_of_tile, size):
        if type_of_tile == "thorn":
            self.image = pygame.Surface((size, size))
            self.image.fill((255, 0, 0))
        elif type_of_tile == "heal_bottle":
            self.image = pygame.Surface((size, size))
            self.image.fill((0, 0, 255))
        elif type_of_tile == "spawnpoint":
            self.image = pygame.Surface((size, size))
            self.image.fill((0, 255, 255))
        elif type_of_tile == "final":
            self.image = pygame.Surface((size, size))
            self.image.fill((255, 255, 255))
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

class HealBottle(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)
        self.flag = 1
    def healing(self,hp):
        if self.flag != 0 and hp + 10 <= 100:
            self.flag -= 1
            self.image.fill((0, 0, 100))
            return 10
        else:
             return 0

class SpawnPoint(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)
        self.pos = pos
        self.flag = False
    def spawn(self):
        self.flag = True
        return self.pos

class FinalTile(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)

    def draw_popup(self, screen, msg):
        popup_rect = pygame.Rect((200, 200), (320, 100))
        pygame.draw.rect(screen, (255, 255, 255), popup_rect)
        font = pygame.font.SysFont(None, 48)
        text = font.render(msg, True, (0, 0, 0))
        screen.blit(text, (popup_rect.x + 20, popup_rect.y + 20))
        pygame.display.flip()