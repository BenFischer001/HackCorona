import pygame
# Character class
class player(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.Surface([20, 20])
            self.image.fill((255, 0, 0))
            self.rect = self.image.get_rect()
            self.x = 12
            self.y = 9
            self.rect.center = (self.x*20+10,self.y*20+10)
            self.id = None
            self.inf = 0
            self.hunger = 100
            self.rr = 100
            self.roadBlock = False
            self.qlvl = 0
            self.infeclvl = 100
            self.sneez = False
            self.out = False


        def update(self):
            self.rect.center = (self.x*20+10, self.y*20+10)

        def setColor(self,color):
            self.image.fill(color)




