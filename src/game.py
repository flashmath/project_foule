import pygame
import time
import datetime
from project_foule.src.voyageur import *
from project_foule.src.Element import *
from project_foule.src.Carte import *


def draw(ecran,carte):
    pygame.draw.rect(ecran,(255,255,255),pygame.Rect(0,0,800,600),0)

    print(len(carte.movents))

    for i in range(len(carte.movents)):
        movent = carte.movents[i]
        movent.draw(ecran)

    pygame.display.flip()


def main():
    carte = Carte(800,600)
    voyageur1 = Voyageur(Coord(10,200),Coord(700,200),carte,10)
    carte.addMovent(voyageur1)

    pygame.init()

    ecran = pygame.display.set_mode((800,600))

    for i in range(100):
        # beginTime=time()
        for j in range(len(carte.movents)):
            voyageur = carte.movents[j]

            # Détection de l'environnement
            obstacles = carte.detectElements(voyageur)
            obstacles.remove(voyageur)

            # décide du mouvement
            newCoord = voyageur.decideMovement(obstacles)

            # effectue son mouvement
            voyageur.deplace(newCoord)
        # endTime=time()
        # time.sleep(1/25-(endTime-beginTime))
        draw(ecran,carte)

    pygame.quit()


main()