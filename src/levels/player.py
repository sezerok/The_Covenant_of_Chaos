import time
import pygame
from src.properties.settings import tile_size

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        # инициализация
        super().__init__()
        self.image = pygame.Surface((tile_size // 2, tile_size))
        self.image.fill((0,250,0))
        self.start_position = pos
        self.rect = self.image.get_rect(topleft=self.start_position)

        # движение игрока
        self.direction = pygame.math.Vector2(0,0)
        self.speed_player = 8
        self.gravity = 0.8
        self.jump = -16
        self.j_val = False
        self.attack = False
        self.health = 100
        self.death = False
        self.invincible = False
        self.invincibility_timer = 0
        self.invincibility_duration = 1  # секунды

    def take_spawn(self, rect):
        self.start_position = rect

    def attack_player(self):
        self.attack = True

    def healing_player(self,heal):
        self.health = self.health + heal

    def return_hp(self):
        return self.health

    def take_damage(self, damage):
        if not self.invincible:
            # применяем урон только если игрок не неуязвим
            self.health -= damage
            self.invincible = True
            self.invincibility_timer = time.time()

        if self.health <= 0:
            self.death = True
            self.stop()


    # функция перемещения
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
        # if keys[pygame.K_LSHIFT]:
        #     self.speed_player = 12
        # else:
        #     self.speed_player = 8

        if keys[pygame.K_SPACE] and self.j_val == False:
            self.jumping()
            self.j_val = True

    def start(self):
        self.speed_player = 8

    def stop(self):
        if self.health == 0:
            time.sleep(0.5)
            self.death = True
            #self.respawn()
    def return_death(self):
        return self.death

    def respawn(self):
        self.rect = self.image.get_rect(topleft=self.start_position)
        self.death = False
        self.health = 100
        self.invincible = False

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
        if self.rect.y > 4000:
            self.death = True
        if self.invincible:
            # обновляем таймер неуязвимости
            current_time = time.time()
            if current_time - self.invincibility_timer >= self.invincibility_duration:
                self.invincible = False
        # self.rect.x+=self.direction.x*self.speed_player
