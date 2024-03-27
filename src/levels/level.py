import pygame
from levels.tiles import Tile
from levels.settings import tile_size
from levels.player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface # поверхность, на которой отображается уровень
        self.setup_level(level_data) # установка разметки
        self.map_shift = 0 # насколько сместить по оси х

    # метод установления разметки
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        # перебор данных разметки
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                if value == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if value == 'P':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    player = Player((x, y))
                    self.player_sprite.add(player)
    def OX_colliding(self):
        player = self.player_sprite.sprite
        player.rect.x += player.direction.x * player.speed_player
        for sprites in self.tiles.sprites():

            if sprites.rect.colliderect(player.rect):
                if player.direction.x<0:
                    player.rect.left=sprites.rect.right

                elif player.direction.x>0:
                    player.rect.right=sprites.rect.left

    def OY_colliding(self):
        player = self.player_sprite.sprite
        player.gravity_apply()
        # player.direction.y += player.gravity
        # player.rect.y += player.direction.y
        for sprites in self.tiles.sprites():
            if sprites.rect.colliderect(player.rect):
                if player.direction.y<0:
                    player.rect.top=sprites.rect.bottom
                    player.direction.y = 0
                elif player.direction.y>0:
                    player.rect.bottom=sprites.rect.top
                    player.direction.y = 0
    def run(self):
        self.tiles.update(self.map_shift) # отвечает за смещение карты по оси x
        self.tiles.draw(self.display_surface)

        self.player_sprite.update()
        self.OX_colliding()
        self.OY_colliding()
        self.player_sprite.draw(self.display_surface)