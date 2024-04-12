import pygame


# Класс плиток (статичные объекты)
class Tile(pygame.sprite.Sprite):
    # TODO: загрузить текстуры шипов
    def __init__(self, pos, size, type_of_tile):
        super().__init__()
        self.select_image(type_of_tile, size)
        self.start_pos = pos
        self.rect = self.image.get_rect(topleft=self.start_pos)  # определение расположения

    def select_image(self, type_of_tile, size):
        # плитки, текстуры которых в разработке
        if type_of_tile in ["thorn", "heal_bottle", "spawnpoint", "final"]:
            color_map = {"thorn": (255, 0, 0), "heal_bottle": (0, 0, 255),
                         "spawnpoint": (0, 255, 255), "final": (255, 255, 255)}
            self.image = pygame.Surface((size, size))
            self.image.fill(color_map[type_of_tile])
        else:
            self.main_ground_image = pygame.image.load(f'levels/res/{type_of_tile}.png').convert_alpha()
            self.image = pygame.transform.scale(self.main_ground_image, (size, size))

    def return_rect(self):
        return self.rect.x, self.rect.y

    def spawnpoint(self, pos):
        self.start_pos = pos

    def restart(self):
        self.rect = self.image.get_rect(topleft=self.start_pos)

    def update(self, x_shift):
        self.rect.x += x_shift


# Класс шипов, наносящих урон
class Thorn(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)

    def damage(self):
        return 10


# Класс объектов, восстанавливающих хп
class HealBottle(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)
        self.flag = 1

    def healing(self, hp):
        # возможность единичного использования
        if self.flag != 0 and hp + 10 <= 100:
            self.flag -= 1
            self.image.fill((0, 0, 100))
            return 10
        else:
            return 0


# Класс объекта респавна
class SpawnPoint(Tile):
    def __init__(self, pos, size, type_of_tile):
        super().__init__(pos, size, type_of_tile)
        self.pos = pos
        self.flag = False

    def spawn(self):
        self.flag = True
        return self.pos


# Класс объекта завершения уровня
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
