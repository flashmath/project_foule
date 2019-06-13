class Point():
    """
    une classe pour les points
    """
    def __init__(self,x,y):
        self.x = x         
        self.y = y       

    def __str__(self):
        return 'Coordonnées du point : ' + '(' + str(self.x) + ";" + str(self.y) + ')'
                
                
class Element():
    """
    une classe pour définir les éléments sur la carte
    """
    def __init__(self,position):     # Position de l'objet dans la carte
        self.pos = position         
    
    def __str__(self):
        return 'Position : ' + '(' + str(self.pos.x) + ";" + str(self.pos.y) + ')'


class Obstacle(Element):
    """
    une classe pour définir un Obstacle sur la carte
    """
    

class Voyageur(Element):
    """
    une classe pour définir un Voyageur sur la carte
    """
    def __init__(self,position,destination):     # Position courante et destination
        self.pos = position         
        self.dest = destination
    
    def __str__(self):
        return 'Position courante : ' + '(' + str(self.pos.x) + ";" + str(self.pos.y) + ')' + '\n' + 'Destination : ' + '(' + str(self.dest.x) + ";" + str(self.dest.y) + ')'

    def setPos(self,newPosition):               # Méthode permettant de changer la position du voyageur
        self.pos=newPosition


class Carte():
    """
    une classe pour la carte qui va contenir les éléments (obstacles et voyageurs) de la carte
    ainsi que la grille (matrice) positionnant les éléments
    """
    def __init__(self,dimensionsCarte,dimensionsGrille):
        self.dimCarte = dimensionsCarte          # dimension (largeur et hauteur) de la carte en pixels
        self.dimGrille = dimensionsGrille        # dimension (nombre de lignes et nombre de colonnes) de la grille
        self.elements = []                      # liste qui va contenir tous les élements de la carte
        self.grille = dimensionsGrille.x*[dimensionsGrille.y*[False]]  # Matrice dont chaque élément vaut true (si un élément) ou false sinon 
        
    def ajouter_element(self,element):  # Méthode pour ajouter un élément à la carte
        self.grille[element.pos.x][element.pos.y]=True    # On indique dans grille qu'un élément est présent en (x,y)
        self.elements.append(element)                   # On ajoute cet élément à la liste des éléments de la carte 
        
    def retirer_element(self,element):  # Méthode pour retirer un élément de la carte
        self.grille[element.pos.x][element.pos.y]=False  # On indique dans grille que l'élément n'est plus présent en (x,y) 
        self.elements.remove(element) # On retire cet élément de la liste des éléments de la carte

    def deplacer_element(self,element):    # Fonction qui déplace un élément dans la carte
        pass                               # A faire

    def __str__(self):
        return 'Carte=' + '(' + str(self.dimCarte.x) + ";" + str(self.dimCarte.y) + ')' + '\n' + 'Grille=' + '(' + str(self.dimGrille.x) + ";" + str(self.dimGrille.y) + ')' + '\n' + 'Nb éléments : ' + str(len(self.elements))
     
        
p=Point(2,3)
d=Point(5,6)
v=Voyageur(p,d)
print(v)
np=Point(8,9)
v.setPos(np)
print(v)
dimensions=Point(10,10)
g=Carte(dimensions,dimensions)
g.ajouter_element(v)
print(g)
g.retirer_element(v)
print(g)
