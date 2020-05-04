import pygame
from math import *


base_image = pygame.image.load("ball.png")
base_image = pygame.transform.scale(base_image, (10,10))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, tank, walls, game, wallbreak):
        super().__init__()
        self.walls = walls
        self.dir = angle
        self.image = base_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tank = tank
        self.xdir = round(cos(radians(self.dir)) * 6)
        self.ydir = -round(sin(radians(self.dir)) * 6)
        self.bounces = 0
        self.time = 0
        self.game = game
        self.wb = wallbreak

    def getType(self):
        return "bullet"

    def hit(self, group, group1, group2):
        if self.tank == "1":
            pygame.sprite.spritecollide(self, group2, True)
        elif self.tank == "2":
            pygame.sprite.spritecollide(self, group1, True)
        else:
            pygame.sprite.spritecollide(self, group, True)

    def update(self):
        self.time += 1
        if self.time == 300:
            self.kill()
        self.rect.x += self.xdir
        if not self.wb:
            if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
                self.xdir = self.xdir * -1
                self.rect.x += self.xdir
                if self.game == 1:
                    if not self.tank == "2":
                        self.tank = ''
                else:
                    self.tank = ''
        self.rect.y += self.ydir
        if not self.wb:
            if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
                self.ydir = self.ydir * -1
                self.rect.y += self.ydir
                if self.game == 1:
                    if not self.tank == "2":
                        self.tank = ''
                else:
                    self.tank = ''