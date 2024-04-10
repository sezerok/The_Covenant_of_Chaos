import time

import pygame
from src.levels.tiles import Tile
from src.levels.settings import tile_size, screen_width
from src.levels.player import Player
from src.levels.thorns import Thorn
from src.levels.heal import Heal
from src.levels.health_bar import HealthBar


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface # поверхность, на которой отображается уровень

        self.setup_level(level_data) # установка разметки
        self.map_shift = 0 # насколько сместить по оси х

    # метод установления разметки
    #
    def setup_level(self, layout):
        self.hearth_bar = HealthBar(10, 10, 300, 40, 100)
        self.tiles = pygame.sprite.Group()
        self.player_sprite = pygame.sprite.GroupSingle()
        self.enemy_sprite = pygame.sprite.Group()
        self.heal_sprite = pygame.sprite.Group()

        # перебор данных разметки
        for row_index, row in enumerate(layout):
            for col_index, value in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if value == 'X':
                    tile = Tile((x, y), tile_size, 'ground_main')
                    self.tiles.add(tile)

                if value == 'G':
                    type_of_tile = 'ground_top'
                    if layout[row_index][col_index-1] == ' ':
                        type_of_tile += '_left'
                    elif layout[row_index][col_index+1] == ' ':
                        type_of_tile += '_right'
                    tile = Tile((x, y), tile_size, type_of_tile)
                    self.tiles.add(tile)

                if value == 'P':
                    player = Player((x, y))
                    self.player_sprite.add(player)

                if value == 'T':
                    thorn = Thorn(tile_size,(x,y))
                    self.enemy_sprite.add(thorn)

                if value == 'H':
                    heal = Heal(tile_size,(x,y))
                    self.heal_sprite.add(heal)



    def OX_colliding_pl(self):
        player = self.player_sprite.sprite
        player.rect.x += player.direction.x * player.speed_player

        for sprites in self.heal_sprite.sprites():
            if player.return_hp != 100:
                if sprites.rect.colliderect(player.rect):
                    player.healing_player(sprites.healing(player.return_hp()))
                    self.hearth_bar.hp = player.return_hp()

        for sprites in self.enemy_sprite.sprites():
            if sprites.rect.colliderect(player.rect):
                player.take_damage(sprites.damage())
                self.hearth_bar.hp = player.return_hp()

        for sprites in self.tiles.sprites():
            if sprites.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprites.rect.right

                elif player.direction.x > 0:
                    player.rect.right = sprites.rect.left




    def OY_colliding_pl(self):
        player = self.player_sprite.sprite
        player.gravity_apply()

        for sprites in self.tiles.sprites():
            if sprites.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprites.rect.bottom
                    player.direction.y = 0

                elif player.direction.y > 0:
                    player.rect.bottom = sprites.rect.top
                    player.j()
                    player.direction.y = 0


    # движение камеры
    def cameraScroll_X(self):
        player = self.player_sprite.sprite
        player_coord_x = player.rect.centerx
        direction = player.direction.x

        if player_coord_x < screen_width / 4 and direction < 0:

            self.map_shift = 8
            player.speed_player = 0

        elif player_coord_x > screen_width - (screen_width / 4) and direction > 0:
            self.map_shift = -8
            player.speed_player = 0

        else:
            self.map_shift = 0
            player.start()


    def run(self):
        #враг
        self.enemy_sprite.update(self.map_shift)
        self.enemy_sprite.draw(self.display_surface)

        #хиллка
        self.heal_sprite.update(self.map_shift)
        self.heal_sprite.draw(self.display_surface)

        #шкала здоровья
        self.hearth_bar.draw(self.display_surface)

        # платформы уровня
        self.tiles.update(self.map_shift) # отвечает за смещение карты по оси x
        self.tiles.draw(self.display_surface)

        # движение камеры
        self.cameraScroll_X()

        # игрок
        self.player_sprite.update()
        self.OX_colliding_pl()
        self.OY_colliding_pl()
        self.player_sprite.draw(self.display_surface)

