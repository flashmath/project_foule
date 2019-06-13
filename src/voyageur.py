from project_foule.src.Element import *
import pygame

class Voyageur(Element):
    """
        Classe gérant un voyageur.
    """

    def __init__(self, depart, final, map, vitesse):
        """
            Initialise un voyageur

                    :param depart : position du voyageur
                    :param map : carte
                    :param final : arrivée du voyageur
                    :type depart: Coord
                    :type map: Carte
                    :type final : Coord
                    :return: retourne le voyageur

            .. warning:: classe peu implémentée à finir
        """
        # TODO: finir la définition de la classe voyageur
        Element.__init__(self, depart, map)
        self.final = final
        self.vitesse = vitesse

    def direction(self):
        v1 = Coord(self.final.x-self.position.x, self.final.y-self.position.y)
        dis = v1.longueur()
        if dis>0:
            v1.x = v1.x / dis * self.vitesse
            v1.y = v1.y / dis * self.vitesse
        else:
            v1.x=0
            v1.y=0
        return v1

    def decideMovement(self, obstacles):
        directionOrigin = self.direction()
        newCoord = Coord(self.position.x + directionOrigin.x, self.position.y + directionOrigin.y)
        possible = True
        for k in range(len(obstacles)):
            if obstacles[k].collision(newCoord):
                possible = False
                break
        return newCoord

    def deplace(self,newCoord):
        self.map.removeFromMap(self)
        self.position.x = newCoord.x
        self.position.y = newCoord.y
        self.map.deplaceElement(self)


    def draw(self,surface):
        pygame.draw.circle(surface,(255,0,0),(int(self.position.x),int(self.position.y)),5,5)
