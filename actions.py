import pygame, random
# Let's import the Car Class
from tank import Tank
from wall import Wall
from bullet import Bullet
from pygame.locals import *
from math import *

def game(game):
    pygame.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    SCREENWIDTH = 1000
    SCREENHEIGHT = 600
    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)

    cd = 0
    tic = 0
    s1 = 0
    s2 = 0
    pygame.display.set_caption("Player 1 - " + str(s1) + "  Player 2 - " + str(s2))

    d = random.randint(0,3)
    d2 = random.randint(0,3)
    xpos1 = 100*random.randint(0, 9) + 20
    ypos1 = 100*random.randint(0, 5) + 35
    xpos2 = 100*random.randint(0, 9) + 20
    ypos2 = 100*random.randint(0, 5) + 35


    if game == 2:
        player = Tank(xpos1, ypos1, "1", 0)
        player2 = Tank(xpos2, ypos2, "2", 0)
    if game == 1:
        player = Tank(xpos1, ypos1, "1", 1)
        player2 = Tank(xpos2, ypos2, "2", 1)

    player.setangle(d*30)
    player.setangle(0)
    player2.setangle(d2*30)
    player2.setangle(0)


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
                    if player.alive():
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
                    if player2.alive():
                        bullet = player2.shoot()
                        all_sprites_list.add(bullet)


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

        if game == 1:
            if tic % 20 == 0:
                p2angle = player2.getangle()
                p2dir = player2.getdirection()
            if tic % 100 == 0:
                if player2.alive():
                    bullet = player2.shoot()
                    all_sprites_list.add(bullet)
            tic += 1
            player2.setangle(p2angle)
            player2.move(p2dir)
        if game == 2:
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

        if (not player2.alive()) or (not player.alive()):
            cd+=1
            if cd == 200:
                cd=0
                if not player.alive() and not player2.alive():
                    s1+=1
                    s2+=1
                elif not player.alive():
                    s2 += 1
                elif not player2.alive():
                    s1 += 1

                d = random.randint(0, 3)
                d2 = random.randint(0, 3)
                xpos1 = 100 * random.randint(0, 9) + 20
                ypos1 = 100 * random.randint(0, 5) + 35
                xpos2 = 100 * random.randint(0, 9) + 20
                ypos2 = 100 * random.randint(0, 5) + 35


                if game == 2:
                    player = Tank(xpos1, ypos1, "1", 0)
                    player2 = Tank(xpos2, ypos2, "2", 0)
                if game == 1:
                    player = Tank(xpos1, ypos1, "1", 1)
                    player2 = Tank(xpos2, ypos2, "2", 1)

                player.setangle(d * 30)
                player.setangle(0)
                player2.setangle(d2 * 30)
                player2.setangle(0)

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

        screen.fill(WHITE)

        pygame.display.set_caption("Player 1 - " + str(s1) + "  Player 2 - " + str(s2))
        all_sprites_list.draw(screen)

        pygame.display.flip()

    pygame.quit()