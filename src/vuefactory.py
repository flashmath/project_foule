from project_foule.src.obstaclevue import *
from project_foule.src.elementvue import *

#################
# Pattern Factory pour la création des différentes vues
#################

class VueFactory:
    '''
        Classe factory
    '''
    def get_factory(self,typeobject):
        if typeobject=="Element":
            return ElementVueFactory()
        if typeobject=="Voyageur":
            return VoyageurVueFactory()


class ElementVueFactory:
    '''
        Classe Factory pour les obstacles
    '''
    def createVue(self,ui,modele):
        return ObstacleVue(ui,modele)

class VoyageurVueFactory:
    '''
        Classe Factory pour les voyageurs
    '''
    def createVue(self,ui,modele):
        return ElementVue(ui,modele)