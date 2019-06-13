from math import *

class Coord:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def longueur(self):
        return sqrt(self.x**2+self.y**2)