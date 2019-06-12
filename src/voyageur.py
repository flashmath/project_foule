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

p=Point(10,11)
d=Point(12,13)
v=Voyageur(p,d)
print(v)
