from project_foule.src.Carte import *

class Element:
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
        self.map = map
        self.position = depart
        self.map.addElement(self)

    def collision(self, p):
        return False


