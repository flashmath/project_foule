class Point():
    """
    une classe pour les points
    """
    def __init__(self,x,y):
        self.x = x         
        self.y = y       

    def __str__(self):
        return '(' + str(self.x) + ";" + str(self.y) + ')'
        
class Vecteur():
    """
    une classe pour le vecteur vitesse
    """
    def __init__(self,vx,vy):
        self.vx = vx         
        self.vy = vy       

    def __str__(self):
        return '(' + str(self.vx) + ";" + str(self.vy) + ')'
        
class Element():
    """
    une classe pour définir les éléments sur la carte
    """
    def __init__(self,positionX,positionY):     # Position courante de l'objet dans la carte
        self.posX = positionX         
        self.posY = positionY     
    
    def __str__(self):
        return '(' + str(self.posX) + ";" + str(self.posY) + ')'

class Obstacle(Element):
    """
    une classe pour définir un Obstacle sur la carte
    """