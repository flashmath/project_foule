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

    def collision(self, p):
        return False


