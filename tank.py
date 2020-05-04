import pygame
from math import *
import random


from bullet import Bullet

WHITE = (255, 255, 255)


class Tank(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.

    def move(self, direction):
        if direction != 0:
            self.control(round(cos(radians(self.dir)) * direction * 5), -round(sin(radians(self.dir)) * direction * 5))
        else:
            self.control(0, 0)

    def setangle(self, angle):
        self.dir += 3*angle
        self.angle = angle


    def control(self, x, y):
        '''
        control player movement
        '''
        self.movex = x
        self.movey = y

    def shoot(self):
        return Bullet(self.rect.centerx+30*cos(radians(self.dir)), self.rect.centery+30*-sin(radians(self.dir)), self.dir, self.name, self.walls,
                      self.game, self.wallbreak)






    def getType(self):
        return "tank"

    def update(self):
        '''
        Update sprite position
        '''

        if self.shrink:
            self.stime = self.stime + 1

        if self.stime == 1:
            self.base_image = pygame.transform.scale(self.base_image, (40,20))
        elif self.stime > 500:
            self.shrink = False
            self.stime = 0
            self.base_image = pygame.transform.scale(pygame.image.load("car.png"), (60, 30))

        if self.wallbreak:
            self.wtime = self.wtime + 1

        if self.wtime > 500:
            self.wallbreak = False
            self.wtime = 0


        self.rotate()
        self.rect.x = self.rect.x + self.movex
        if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
            self.rect.x = self.rect.x - self.movex
        self.rect.y = self.rect.y + self.movey
        if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
            self.rect.y = self.rect.y - self.movey

    def contains(self, x,y):
        if x<self.rect.x or x>self.rect.x+self.rect.w or y<self.rect.y or y>self.rect.y+self.rect.h:
            return False
        return True

    def RAIdir(self, grid, enemy):
        targetx = enemy.rect.centerx
        targety = enemy.rect.centery
        angles = []
        for i in range(8):
            angle = i*45
            startx = self.rect.centerx+30*cos(radians(angle))
            starty = self.rect.centery+30*-sin(radians(angle))
            x = startx
            y = starty

            xm = round(6*cos(radians(angle)))
            ym = round(-6*sin(radians(angle)))
            for j in range(150):
                xn = int(x // 100)
                yn = int(y // 100)

                x += xm
                if (x % 100 > 90 and xm > 0) or (x % 100 < 10 and xm < 0):
                    if yn == 6 or yn == 7:
                        yn = 5
                    if yn == -1:
                        yn == 0
                    if xn == -1:
                        xn == 0
                    if xn == 11:
                        xn = 10
                    try:
                        if grid[yn*2+1][xn] == 1:
                            xm = xm*-1
                    except:
                        print(yn*2+1)
                        print(xn)
                y += ym
                if (y % 100 > 90 and ym > 0) or (y % 100 < 10 and ym < 0):
                    if xn == 10:
                        xn = 9
                    if yn == 7:
                        yn = 6
                    if yn == -1:
                        yn == 0
                    if xn == -1:
                        xn == 0
                    try:
                        if grid[yn*2][xn] == 1:
                            ym = ym*-1
                    except:
                        print(yn*2)
                        print(xn)
                if abs(x - targetx) < 30 and abs(y - targety) < 30:
                    if angle%90 == 0:
                        return angle
                    else:
                        angles.append(angle)
        if angles:
            return angles[0]
        return -1



    def AIMove(self, grid, enemy, last):
        if last == 0:
            worst = 1
        elif last == 180:
            worst = 2
        elif last == 90:
            worst = 4
        else:
            worst = 3
        order = [1,2,3,4]
        order.remove(worst)
        random.shuffle(order)
        order.append(worst)
        xn = self.rect.x // 100
        yn = self.rect.y // 100
        for item in order:
            if item < 3:
                if grid[2*yn+1][xn + item - 1] == 0:
                    if item == 1:
                        return 180
                    if item == 2:
                        return 0
            else:
                if grid[2*yn+2*(item-3)][xn] == 0:
                    if item == 3:
                        return 90
                    if item == 4:
                        return 270

    def getdirection(self):

        num = random.randint(0,1)
        if num == 0:
            return 1
        return 3



    def rotate(self):
        rot_image = pygame.transform.rotate(self.base_image, self.dir)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        self.image = rot_image.convert_alpha()
        self.rect = rot_rect
        if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
            rot_rect.x +=2
            self.rect = rot_rect
            if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
                rot_rect.x -= 4
                self.rect = rot_rect
            if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
                rot_rect.x += 2
                rot_rect.y += 2
                self.rect = rot_rect
            if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
                rot_rect.y -= 4
                self.rect = rot_rect
            if len(pygame.sprite.spritecollide(self, self.walls, False)) != 0:
                rot_rect.y +=2
                self.dir -= 3*self.angle
                self.rect = rot_rect
            rot_image = pygame.transform.rotate(self.base_image, self.dir)
            self.image = rot_image.convert_alpha()
        else:
            self.image = rot_image.convert_alpha()
            self.rect = rot_rect

    def setPowerup(self,item):
        if item.name == "shrink":
            self.shrink = True
        elif item.name == "wallbreak":
            self.wallbreak = True

    def __init__(self, x, y, name, game):
        # Call the parent class (Sprite) constructor
        super().__init__()
        self.base_image = pygame.transform.scale(pygame.image.load("car.png"), (60,30))
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.dir = 0
        self.image = self.base_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.walls = pygame.sprite.Group()
        self.angle = 0
        self.game = game
        self.shrink = False
        self.stime = 0
        self.wallbreak = False
        self.wtime = 0