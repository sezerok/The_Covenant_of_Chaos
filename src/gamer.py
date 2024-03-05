import pygame
pygame.init()

class Gamer:
    def __init__(self, width, height, o_x, o_y, surface):
        self.o_x = o_x
        self.o_y = o_y
        self.surface = surface
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.o_x, self.o_y, self.width, self.height)
    def draw(self):
        self.rect = pygame.Rect(self.o_x, self.o_y, self.width, self.height)
        pygame.draw.rect(self.surface, (0, 0, 0), self.rect)
        pygame.display.flip()

    def move(self,event,func):

        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.o_x-=100
                self.draw()
                print(self.o_x)

            elif event.key==pygame.K_d:
                self.o_x+=100
                self.draw()
                print(self.o_x)

            elif event.key==pygame.K_w:
                for i in range(100):
                    self.o_y-=1
                    self.draw()
                    func((198, 50, 100))
                print(self.o_y)
                for i in range(100):
                    self.o_y+=1
                    self.draw()
                    func((198, 50, 100))
                print(self.o_y)
            elif event.key==pygame.K_s:
                for i in range(100):
                    self.o_y+=1
                    self.height-=1
                    self.draw()
                    func((198, 50, 100))
                for i in range(100):
                    self.o_y-=1
                    self.height+=1
                    self.draw()
                    func((198, 50, 100))