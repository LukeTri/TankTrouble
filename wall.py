import pygame

class Wall(pygame.sprite.Sprite):
    def __init__(self, t, l, w, h):
        super().__init__()
        self.height = h
        self.width = w
        self.top = t
        self.left = l
        self.rect = pygame.Rect(t, l, w, h)
        self.image = pygame.Surface((w, h))

    def draw(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)

    def contains(self, x,y):
        if x<self.rect.x or x>self.rect.x+self.rect.w or y<self.rect.y or y>self.rect.y+self.rect.h:
            return False
        return True

    def getType(self):
        return "wall"