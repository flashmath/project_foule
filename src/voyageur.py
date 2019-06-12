class Point():
    """
    une classe pour les points
    """
    def __init__(self,x,y):
        self.x = x         
        self.y = y       

    def __str__(self):
        return 'Coordonnées du point : ' + '(' + str(self.x) + ";" + str(self.y) + ')'
        
class Vecteur():
    """
    une classe pour le vecteur vitesse
    """
    def __init__(self,vx,vy):
        self.vx = vx         
        self.vy = vy       

    def __str__(self):
        return 'Vecteur vitesse : ' + '(' + str(self.vx) + ";" + str(self.vy) + ')'
        
class Element():
    """
    une classe pour définir les éléments sur la carte
    """
    def __init__(self,positionX,positionY):     # Position de l'objet dans la carte
        self.posX = positionX         
        self.posY = positionY     
    
    def __str__(self):
        return 'Position : ' + '(' + str(self.posX) + ";" + str(self.posY) + ')'

class Obstacle(Element):
    """
    une classe pour définir un Obstacle sur la carte
    """
    
class Voyageur(Element):
    """
    une classe pour définir un Voyageur sur la carte
    """
    def __init__(self,positionX,positionY,destinationX,destinationY):     # Position courante et destination
        self.posX = positionX         
        self.posY = positionY
        self.destX = destinationX         
        self.destY = destinationY     
    
    def __str__(self):
        return 'Position courante : ' + '(' + str(self.posX) + ";" + str(self.posY) + ')' + '\n' + 'Destination : ' + '(' + str(self.destX) + ";" + str(self.destY) + ')'

v=Voyageur(10,11,12,13)
print(v)
