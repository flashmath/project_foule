from project_foule.src.ui import *
from project_foule.src.Carte import *
from project_foule.src.voyageur import *
import time

if __name__ == '__main__':

    carte = Carte(100,100)
    voyageur = Voyageur(Coord(20,10),Coord(20,30),carte,0.3)
    carte.addVoyageurs(voyageur)
    voyageur = Voyageur(Coord(40, 10), Coord(20, 30), carte, 0.3)
    carte.addVoyageurs(voyageur)
    meuble = Element(Coord(40,35),carte)
    carte.addMeubles(meuble)

    ui = UI(carte)
    ui.mainloop()

    ui.quit()
