from project_foule.src.coord import *

class SubGrille:

    def __init__(self,grille, lefttop, width=3,height=3):
        self.lefttop = lefttop
        self.width = width
        self.height = height
        self.grille = [[grille[lefttop.x+i][lefttop.y+j] for i in range(10*width)] for j in range(10*height)]
