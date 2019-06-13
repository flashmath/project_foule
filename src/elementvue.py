import pygame

class ElementVue(pygame.sprite.Sprite):

    def __init__(self,ui,modele):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([10,10])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))

        pygame.draw.ellipse(self.image,(255,0,0),[0,0,10,10],5)
        self.rect = self.image.get_rect()
        self.observe = modele
        self.ui = ui

        modele.attach_observateur(self)


    def mise_a_jour(self):
        xcentre,ycentre,cote =self.ui.conversion_coord(self.observe)
        self.rect.x=xcentre-cote
        self.rect.y=ycentre-cote
