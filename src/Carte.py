from project_foule.src.voyageur import *
from project_foule.src.Element import *
from project_foule.src.coord import *

class Carte:

    def __init__(self,x,y):
        self.grille = [[[] for i in range(10)] for j in range(10)]
        self.elements = []
        self.voyageurs = []
        self.movents = []
        self.width = x
        self.height = y

    def addElement(self,element):
        self.elements.append(element)
        self.deplaceElement(element)

    def addMovent(self,element):
        self.movents.append(element)
        self.deplaceElement(element)

    def positionGrille(self, element):
        xgrille = int(element.position.x / self.width * 10)
        ygrille = int(element.position.y / self.height * 10)
        return xgrille,ygrille

    def removeFromMap(self,element):
        x,y=self.positionGrille(element)
        self.grille[x][y].remove(element)

    def deplaceElement(self, element):
        x,y=self.positionGrille(element)
        self.grille[x][y].append(element)

    def detectElements(self,element):
        retour = []
        for i in range(len(self.movents)):
            retour.append(self.movents[i])
        return retour





