import pygame, random
# Let's import the Car Class
from tank import Tank
from wall import Wall
from bullet import Bullet
from pygame.locals import *
from math import *


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREENWIDTH = 1000
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)




s1 = 0
s2 = 0
pygame.display.set_caption("Player 1 - " + str(s1) + "  Player 2 - " + str(s2))

player = Tank(200, 300, "1")
player2 = Tank(0, 100, "2")

all_sprites_list = pygame.sprite.Group()
players = pygame.sprite.Group()
p1 = pygame.sprite.Group()
p1.add(player)
p2 = pygame.sprite.Group()
p2.add(player2)
all_sprites_list.add(player)
all_sprites_list.add(player2)
players.add(player)
players.add(player2)
walls = pygame.sprite.Group()
walls.add(Wall(0, 0, 5, 600))
walls.add(Wall(0, 0, 1000, 5))
walls.add(Wall(995, 0, 5, 600))
walls.add(Wall(0, 595, 1000, 5))
walls.add(Wall(100, 100, 400, 5))
walls.add(Wall(100, 200, 5, 300))
walls.add(Wall(200, 100, 5, 200))
walls.add(Wall(200, 400, 5, 100))
walls.add(Wall(300, 200, 100, 5))
walls.add(Wall(200, 400, 400, 5))
walls.add(Wall(600, 200, 5, 200))
walls.add(Wall(300, 500, 400, 5))
walls.add(Wall(600, 0, 5, 100))
walls.add(Wall(500, 200, 5, 100))
walls.add(Wall(300, 300, 200, 5))
walls.add(Wall(800, 200, 5, 300))
walls.add(Wall(700, 100, 5, 100))
walls.add(Wall(700, 300, 5, 100))
walls.add(Wall(700, 100, 200, 5))
walls.add(Wall(800, 500, 100, 5))
walls.add(Wall(900, 200, 5, 200))

all_sprites_list.add(walls)
player.walls = walls
player2.walls = walls


carryOn = True
MOVE_RIGHT = 3
MOVE_LEFT = 1
direction = 0
direction2 = 0
SPIN_UP = 1
SPIN_DOWN = -1
angle = 0
angle2 = 0

score= 0

while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        if event.type == KEYDOWN:
            if event.key == K_DOWN:
                direction = MOVE_LEFT
            elif event.key == K_UP:
                direction = MOVE_RIGHT
            elif event.key == K_LEFT:
                angle = SPIN_UP
            elif event.key == K_RIGHT:
                angle = SPIN_DOWN
            elif event.key == K_SPACE:
                bullet = player.shoot()
                all_sprites_list.add(bullet)
            elif event.key == K_s:
                direction2 = MOVE_LEFT
            elif event.key == K_w:
                direction2 = MOVE_RIGHT
            elif event.key == K_a:
                angle2 = SPIN_UP
            elif event.key == K_d:
                angle2 = SPIN_DOWN
            elif event.key == K_q:
                bullet = player2.shoot()
                all_sprites_list.add(bullet)
            elif event.key == K_TAB:
                if score ==1:
                    s1+=1
                if score ==-1:
                    s2+=1
                player = Tank(200, 300, "1")
                player2 = Tank(0, 100, "2")
                all_sprites_list = pygame.sprite.Group()
                players = pygame.sprite.Group()
                p1 = pygame.sprite.Group()
                p1.add(player)
                p2 = pygame.sprite.Group()
                p2.add(player2)
                all_sprites_list.add(player)
                all_sprites_list.add(player2)
                players.add(player)
                players.add(player2)
                all_sprites_list.add(walls)
                player.walls = walls
                player2.walls = walls


        elif event.type == KEYUP:
            if event.key == K_UP:
                direction = 0
            elif event.key == K_DOWN:
                direction = 0
            elif event.key == K_RIGHT:
                angle = 0
            elif event.key == K_LEFT:
                angle = 0
            elif event.key == K_w:
                direction2 = 0
            elif event.key == K_s:
                direction2 = 0
            elif event.key == K_d:
                angle2 = 0
            elif event.key == K_a:
                angle2 = 0

    player.setangle(angle)
    player.move(direction)
    player2.setangle(angle2)
    player2.move(direction2)
    num = 0
    for item in all_sprites_list:
        if item.getType() == "bullet":
            num = item.hit(players, p1, p2)

    if not(player in all_sprites_list.sprites()):
        if not score == 1:
            score = -1
    elif not(player2 in all_sprites_list.sprites()):
        if not score == -1:
            score = 1
    else:
        score = 0

    all_sprites_list.update()
    screen.fill(WHITE)

    pygame.display.set_caption("Player 1 - " + str(s1) + "  Player 2 - " + str(s2))
    all_sprites_list.draw(screen)

    pygame.display.flip()

pygame.quit()