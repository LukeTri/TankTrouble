import pygame
import twoplayers
import oneplayer

pygame.init()

SCREENWIDTH = 1000
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)

image = pygame.image.load("tank.png").convert_alpha()

b1 = pygame.image.load("button1.png").convert_alpha()

b2 = pygame.image.load("button2.png").convert_alpha()

title = pygame.image.load("intropic.png").convert_alpha()

clock = pygame.time.Clock()
done = False

brect = b1.get_rect()
r1 = b1.get_rect()
r2 = b2.get_rect()
trect = title.get_rect()

game = 0
while not done:
    screen.fill((255, 255, 255))

    x= 150
    y=470

    screen.blit(b1, (x, y))
    screen.blit(b2, (1000-x-brect[2], y))

    rect = image.get_rect()
    screen.blit(image, ((1000-rect[2])//2,140))
    screen.blit(title, ((1000-trect[2])//2, 50))




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP and pos[0]>x and pos[0]<x+r1[2] and pos[1]>y and pos[1]<y+r1[3]:
            game = 2
            done = True
        if event.type == pygame.MOUSEBUTTONUP and pos[0]>1000-r2[2]-x and pos[0]<1000-x and pos[1]>y and pos[1]<y+r2[3]:
            game = 1
            done = True

    pygame.display.flip()
    clock.tick(60)

if game == 1:
    twoplayers.game()

elif game == 2:
    oneplayer.game()