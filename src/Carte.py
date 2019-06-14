from project_foule.src.voyageur import *
from project_foule.src.Element import *
from project_foule.src.coord import *
from project_foule.src.subgrille import *

class Carte:

    def __init__(self,x,y):
        # sous-grille de la carte
        self.grille = [[[] for i in range(10)] for j in range(10)]
        # ensemble des éléments de la grille
        self.elements = []
        # ensemble des voyageurs
        self.voyageurs = []
        # ensemble des obstacles
        self.meubles = []
        # dimensions de la carte
        self.width = x
        self.height = y
        # grille des obstacles
        self.obstacles = [[0 for i in range(100)] for j in range(100)]

    def addElement(self,element):
        self.elements.append(element)
        self.deplaceElement(element)

    def addMeubles(self,element):
        self.meubles.append(element)
        self.elements.append(element)
        self.deplaceElement(element)
        element.inscrit_obstacle(self.obstacles)

    def addVoyageurs(self,element):
        self.voyageurs.append(element)
        self.elements.append(element)
        self.deplaceElement(element)

    def positionGrille(self, element):
        '''
        Renvoie la position dans la grille
        :param element:
        :return:
        '''
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
        for i in range(len(self.elements)):
            retour.append(self.elements[i])
        return retour

    def nouveau_pas(self):
        for j in range(len(self.voyageurs)):
            voyageur = self.voyageurs[j]

            # Détection de l'environnement
            xgrille,ygrille=self.positionGrille(voyageur)
            minx = max(0,xgrille-1)
            miny = max(0,ygrille-1)
            maxx = min(9,xgrille+1)
            maxy = min(9,xgrille+1)
            subgrille = SubGrille(self.obstacles,Coord(minx*10,miny*10),(maxx-minx)*10,(maxy-miny)*10)


            obstacles = self.detectElements(voyageur)
            obstacles.remove(voyageur)

            for o in obstacles:
                if o is Voyageur:
                    o.getobstacle(subgrille)

            # décide du mouvement
            newCoord = voyageur.decideMovement(obstacles)

            #  Mouvement en cours
            # newCoord = voyageur.decideMovement2(subgrille)

            # effectue son mouvement
            voyageur.deplace(newCoord)
        # endTime=time()
        # time.sleep(1/25-(endTime-beginTime))

    def obtenir_sous_grille(self,elt):
        '''
        Obtenir la sous-grille d'au maximum 9 cases contenant l'obstacle
        :param elt: voyageur
        :return: les coordonnées des points haut-gauche et bas-droite
        '''
        xgrille,ygrille=self.positionGrille(elt)
        xlefttop=max(0,(xgrille-1)*10)
        ylefttop=max(0,(ygrille-1)*10)
        xrightbottom=min(100,(xgrille+1)*10)
        yrightbottom=min(100,(xgrille+1)*10)
        return xlefttop,ylefttop,xrightbottom,yrightbottom

