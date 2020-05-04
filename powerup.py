import pygame


shrink_image = pygame.transform.scale(pygame.image.load("shrink.png"), (30,30))
wallbreak_image = pygame.transform.scale(pygame.image.load("wallbreak.jpg"), (45,40))

class Powerup(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        if name == "shrink":
            self.image = shrink_image.convert_alpha()
        if name == "wallbreak":
            self.image = wallbreak_image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def getType(self):
        return "powerup"

    def hit(self, p1, p2):
        if pygame.sprite.collide_rect(self, p1):
            return "1"
        elif pygame.sprite.collide_rect(self, p2):
            return "2"
        else:
            return "0"
