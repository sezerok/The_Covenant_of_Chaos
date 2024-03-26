import pygame
from levels.tiles import Tile
from levels.settings import tile_size

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface # поверхность, на которой отображается уровень
        self.setup_level(level_data) # установка разметки
        self.map_shift = 0 # насколько сместить по оси х

    # метод установления разметки
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        # перебор данных разметки
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                # if value == 'P':
                #     отображение игрока

    def run(self):
        self.tiles.update(self.map_shift) # отвечает за смещение карты по оси x
        self.tiles.draw(self.display_surface)