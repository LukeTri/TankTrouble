import pygame, random
# Let's import the Car Class
from tank import Tank
from wall import Wall
from powerup import Powerup
from bullet import Bullet
from pygame.locals import *
from math import *

def game(game):
    pygame.init()
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    one = pygame.image.load("one.jpg").convert_alpha()
    two = pygame.image.load("two.jpg").convert_alpha()
    three = pygame.image.load("three.png").convert_alpha()
    one = pygame.transform.scale(one, (30, 60))
    two = pygame.transform.scale(two, (45, 60))
    three = pygame.transform.scale(three, (40, 60))

    walls = pygame.sprite.Group()
    walls.add(Wall(0, 0, 5, 600))
    walls.add(Wall(0, 0, 1000, 5))
    walls.add(Wall(1000, 0, 5, 600))
    walls.add(Wall(0, 600, 1000, 5))
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
    wlist = walls.sprites()

    grid = []

    for i in range(13):
        curli = []
        if i % 2 == 0:
            for j in range(10):
                curli.append(0)
                for item in wlist:
                    if item.contains(j * 100 + 30, i / 2 * 100):
                        curli[j] = 1
        else:
            for j in range(11):
                curli.append(0)
                for item in wlist:
                    if item.contains(j * 100, (i - 1) * 50 + 30):
                        curli[j] = 1
        grid.append(curli)
    print(grid)

    SCREENWIDTH = 1005
    SCREENHEIGHT = 605
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

    var = True
    while var:
        xpos2 = 100 * random.randint(0, 9) + 20
        ypos2 = 100 * random.randint(0, 5) + 35
        xn = xpos2 // 100
        yn = ypos2 // 100
        count = 0
        if grid[yn * 2][xn] == 1:
            count += 1
        if grid[yn * 2 + 2][xn] == 1:
            count += 1
        if grid[yn * 2 + 1][xn] == 1:
            count += 1
        if grid[yn * 2+1][xn + 1] == 1:
            count += 1
        if count < 2:
            var = False


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
    shrinkTime = random.randint(0,1000)





    all_sprites_list.add(walls)
    player.walls = walls
    player2.walls = walls


    carryOn = True
    MOVE_RIGHT = 1
    MOVE_LEFT = -1
    direction = 0
    direction2 = 0
    SPIN_UP = 1
    SPIN_DOWN = -1
    angle = 0
    angle2 = 0
    score= 0
    ais = True
    p2angle = 0
    AIdir = -1
    m = 0
    last = 0
    resetAngle = False
    CLOCK = 0

    while carryOn:
        CLOCK+=1
        screen.fill(WHITE)
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
        shots = 0
        if game == 1:

            for item in all_sprites_list.sprites():
                if item.getType() == "bullet":
                    if item.tank == "2":
                        shots += 1

            if ais:
                olda = p2angle
                p2angle = player2.RAIdir(grid,player)
                if olda != p2angle:
                    tic = 0
                if p2angle != -1:
                    if (p2angle - player2.dir) % 360 < 2 or (player2.dir - p2angle) % 360 < 2:
                        if tic % 50 == 15 and shots <= 5:
                            if player2.alive():
                                bullet = player2.shoot()
                                all_sprites_list.add(bullet)
                    elif (p2angle - player2.dir) % 360 < 180:
                        player2.setangle(1)
                    else:
                        player2.setangle(-1)
                else:
                    ais = False

            else:
                if AIdir == -1:
                    AIdir = player2.AIMove(grid, player, last)
                if (AIdir - player2.dir) % 360 < 2 or (player2.dir - AIdir) % 360 < 2:
                    if m < 20:
                        player2.move(1)
                        m += 1
                    else:
                        player2.move(0)
                        last = AIdir
                        AIdir = -1
                        m = 0
                        ais = True
                elif (AIdir - player2.dir) % 360 < 180:
                    player2.setangle(1)
                else:
                    player2.setangle(-1)
        tic += 1

        if game == 2:
            if CLOCK%1000 == shrinkTime:
                xpos2 = 100 * random.randint(0, 9) + 20
                ypos2 = 100 * random.randint(0, 5) + 35
                all_sprites_list.add(Powerup("shrink", 100 * random.randint(0, 9) + 20, 100 * random.randint(0, 5) + 35))

        if game == 2:
            player2.setangle(angle2)
            player2.move(direction2)
        num = 0
        for item in all_sprites_list:
            if item.getType() == "bullet":
                num = item.hit(players, p1, p2)
            elif item.getType() == "powerup":
                num = item.hit(player, player2)
                if num == "1":
                    all_sprites_list.remove(item)
                    player.setShrink()
                elif num == "2":
                    all_sprites_list.remove(item)
                    player2.setShrink()

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
            cd += 1
            if cd < 25:
                screen.blit(three, (930, 20))
            elif 75 > cd > 50:
                screen.blit(two, (930, 20))
            elif 100 < cd < 125:
                screen.blit(one, (930, 20))
            if cd == 150:
                cd = 0
                if not player.alive() and not player2.alive():
                    s1 += 1
                    s2 += 1
                elif not player.alive():
                    s2 += 1
                elif not player2.alive():
                    s1 += 1

                d = random.randint(0, 3)
                d2 = random.randint(0, 3)
                xpos1 = 100 * random.randint(0, 9) + 20
                ypos1 = 100 * random.randint(0, 5) + 35
                var = True
                while var:
                    xpos2 = 100 * random.randint(0, 9) + 20
                    ypos2 = 100 * random.randint(0, 5) + 35
                    xn = xpos2 // 100
                    yn = ypos2 // 100
                    count = 0
                    if grid[yn * 2][xn] == 1:
                        count += 1
                    if grid[yn * 2 + 2][xn] == 1:
                        count += 1
                    if grid[yn * 2 + 1][xn] == 1:
                        count += 1
                    if grid[yn * 2 + 1][xn + 1] == 1:
                        count += 1
                    if count < 2:
                        var = False
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
                CLOCK = 0




        pygame.display.set_caption("Player 1 - " + str(s1) + "  Player 2 - " + str(s2))
        all_sprites_list.draw(screen)

        pygame.display.flip()

    pygame.quit()