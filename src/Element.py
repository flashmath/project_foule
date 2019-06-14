from project_foule.src.Carte import *
from project_foule.src.Observable import *

class Element(Observable):
    """
            Classe gérant les éléments d'une carte
        """

    def __init__(self, depart, map):
        """
                    Initialise un voyageur

                    :param depart : position de l element
                    :param map : position de la map
                    :type depart: Coord
                    :type map: Carte
                    :return: retourne le voyageur

                    .. warning:: classe peu implémentée à finir
                """
        Observable.__init__(self)
        self.map = map
        self.position = depart
        self.map.addElement(self)
        self.type = "Element"

    def collision(self, p):
        return False

    def inscrit_obstacle(self,grille):
        # a l'arrache, on détermine un carré
        for i in range(-5,6):
            for j in range(-5,6):
                x=self.position.x+i
                y=self.position.y+j
                if x>=0 and x<=99 and y>=0 and y<=99:
                    grille[x][y]=1
