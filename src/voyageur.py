from project_foule.src.Element import *
from project_foule.src.coord import *
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
        self.type = "Voyageur"

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

    def decideMovement2(self,grille):
        xgrille = self.position.x-grille.lefttop.x
        ygrille = self.position.y-grille.lefttop.y
        grille[xgrille][ygrille]='x'
        #self.minDistanceGrille(grille)
        self.calcul_distances(0,grille,xgrille,ygrille)
        # TODO : calcul des distances minimales sur les bords de la grille par rapport au point d'arrivée
        # TODO : recherche de la plus courte distance sur les bords de la grille
        # TODO : renvoi du chemin le plus court
        # TODO : retour du point d'arrivée

    def calcul_distances(self,i,grille,x,y):
        if grille[x][y]!='x':
            grille[x][y]=i
    




    def minDistanceGrille(self,grille):
        for i in range(30):
            for col in range(grille.width):
                for row in range(grille.height):
                    if (i==0 and grille[col][row]=='x') or (i!=0 and grille[col][row]==i):
                        for deltax in range(-1,2):
                            for deltay in range(-1,2):
                                newx,newy = col+deltax,row+deltay
                                if newx>=0 and newx<len(grille.width) and newy>=0 and newy<len(grille.height):
                                    if grille[col][row]==0:
                                        grille[col][row]==i









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
        self.notifier()

    def getobstacle(self,grille):
        '''
        Inscrit ses points obstacles dans la grille
        :param grille:
        :return:
        '''
        for i in range(-5,6):
            for j in range(-5,6):
                xpos = self.position.x-grille.lefttop.x
                ypos = self.position.y-grille.lefttop.y
                if xpos>=0 and xpos<grille.width and ypos>=0 and ypos<grille.height:
                    grille[xpos,ypos]=-1
