import pygame
import time
from project_foule.src.elementvue import *
from project_foule.src.vuefactory import *

class UI:

    def __init__(self,carte):
        self.vuefactory = VueFactory()
        self.largeur = 800
        self.title = "Foule"

        self.carte = carte

        pygame.init()

        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((self.largeur,self.largeur))
        self.sprites = pygame.sprite.Group()
        self.initialisation_graphiqe()

    def mainloop(self):
        pas=0
        carryOn = True
        clock = pygame.time.Clock()
        while carryOn:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    carryOn = False

            self.carte.nouveau_pas()

            self.screen.fill((255,255,255))

            self.sprites.draw(self.screen)
            pygame.display.flip()
            clock.tick(60)

    def quit(self):
        pygame.quit()

    def initialisation_graphiqe(self):
        for elt in self.carte.elements:
            # utilisation du design-pattern fabrique de classe envisageable
            factory = self.vuefactory.get_factory(elt.type)
            elt_vue = factory.createVue(self,elt)
            xcentre, ycentre, cote = self.conversion_coord(elt)
            elt_vue.rect.x = xcentre - cote
            elt_vue.rect.y = ycentre - cote
            self.sprites.add(elt_vue)
        #self.sprites.draw(self.screen)
        #pygame.display.flip()

    def conversion_coord(self,c):
        xcentre = c.position.x * self.largeur / c.map.width
        ycentre = c.position.y * self.largeur / c.map.height
        cote = 5
        return xcentre, ycentre, cote
