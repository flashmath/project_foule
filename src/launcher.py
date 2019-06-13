from project_foule.src.ui import *
from project_foule.src.voyageur import  *

if __name__ == '__main__':
    dimensions = Coord(10, 10)

    # Création de la carte
    carte = Carte(dimensions, dimensions)
    #carte.afficher_grille()

    # Création des 10 voyageurs
    # for i in range(2):
    #    carte.ajouter_element(Voyageur(Coord(randint(0,9),randint(0,9)),Coord(0,0)))
    carte.ajouter_element(Voyageur(Coord(4, 0), Coord(4, 9)))
    carte.ajouter_element(Voyageur(Coord(4, 9), Coord(4, 0)))
    carte.ajouter_element(Voyageur(Coord(3, 0), Coord(3, 9)))
    carte.ajouter_element(Voyageur(Coord(3, 9), Coord(3, 0)))
    carte.ajouter_element(Voyageur(Coord(5, 0), Coord(5, 9)))
    carte.ajouter_element(Voyageur(Coord(5, 9), Coord(5, 0)))

    root = Root(carte)
    root.mainloop()