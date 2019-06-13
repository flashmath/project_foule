#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from project_foule.src.Observable import *

class Coord():
    """
    une classe pour les coordonnées d'un point de la carte
    """
    def __init__(self,x,y):
        self.x = x         
        self.y = y       

    def __str__(self):
        return 'Coordonnées du point : ' + '(' + str(self.x) + ";" + str(self.y) + ')'
                
                
class Element(Observable):
    """
    une classe pour définir les éléments sur la carte
    """
    def __init__(self,position):     # Position de l'objet dans la carte
        Observable.__init__(self)
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
        Element.__init__(self,position)
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
        self.grille = [[False for i in range(dimensionsGrille.x)] for j in range(dimensionsGrille.x)]  # Matrice dont chaque élément vaut true (si un élément) ou false sinon
        self.compteurVoyageurs = 0     # Compte le nombre de voyageur 
        
    def ajouter_element(self,element):  # Méthode pour ajouter un élément à la carte
        self.grille[element.pos.x][element.pos.y]=True    # On indique dans grille qu'un élément est présent en (x,y)
        self.elements.append(element)                   # On ajoute cet élément à la liste des éléments de la carte 
        self.compteurVoyageurs += 1
        
    def retirer_element(self,element):  # Méthode pour retirer un élément de la carte
        self.grille[element.pos.x][element.pos.y]=False  # On indique dans grille que l'élément n'est plus présent en (x,y) 
        self.elements.remove(element) # On retire cet élément de la liste des éléments de la carte
        self.compteurVoyageurs -= 1

    def afficher_grille(self):
        for i in range(self.dimGrille.x):
            print(self.grille[i])
    
    def deplacer_voyageur(self,voyageur):
        direction=Coord(voyageur.dest.x-voyageur.pos.x,voyageur.dest.y-voyageur.pos.y) # Vecteur direction
        dvect=Coord(0,0)                            # Vecteur déplacement
        if direction.x > 0 and direction.y > 0:
            dvect.x = 1
            dvect.y = 1

        if direction.x < 0 and direction.y > 0:
            dvect.x = -1
            dvect.y = 1
        
        if direction.x > 0 and direction.y < 0:
            dvect.x = 1
            dvect.y = -1
        
        if direction.x < 0 and direction.y < 0:
            dvect.x = -1
            dvect.y = -1
            
        if direction.x == 0 and direction.y > 0:
            dvect.x = 0
            dvect.y = 1
    
        if direction.x == 0 and direction.y < 0:
            dvect.x = 0
            dvect.y = -1
            
        if direction.x > 0 and direction.y == 0:
            dvect.x = 1
            dvect.y = 0

        if direction.x < 0 and direction.y == 0:
            dvect.x = -1
            dvect.y = 0
        
        # Mise à jour de la grille et de la position du voyageur
        # 1ère solution : Si la case où doit se déplacer le voyageur n'ait pas libre, le voyageur ne se déplace pas
        # if self.grille[voyageur.pos.x+dvect.x][voyageur.pos.y+dvect.y]==False:
        #    self.grille[voyageur.pos.x][voyageur.pos.y]=False
        #    voyageur.pos.x += dvect.x
        #    voyageur.pos.y += dvect.y
        #    self.grille[voyageur.pos.x][voyageur.pos.y]=True
        
        # 2ème solution : Si la case où doit se déplacer le voyageur n'est pas libre, on cherche un case de libre et on choisit la meilleur (celle qui minime la distance au point de destination)
        if self.grille[voyageur.pos.x+dvect.x][voyageur.pos.y+dvect.y]==True: # Cas où la cas est occupée
            liste_cases_vide=[]        # liste des cases vides autour du voyageur
            if self.grille[voyageur.pos.x-1][voyageur.pos.y-1]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x-1,voyageur.pos.y-1))
            if self.grille[voyageur.pos.x-1][voyageur.pos.y]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x-1,voyageur.pos.y))
            if self.grille[voyageur.pos.x-1][voyageur.pos.y+1]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x-1,voyageur.pos.y+1))
            if self.grille[voyageur.pos.x+1][voyageur.pos.y-1]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x+1,voyageur.pos.y-1))
            if self.grille[voyageur.pos.x+1][voyageur.pos.y]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x+1,voyageur.pos.y))
            if self.grille[voyageur.pos.x+1][voyageur.pos.y+1]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x+1,voyageur.pos.y+1))               
            if self.grille[voyageur.pos.x][voyageur.pos.y-1]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x,voyageur.pos.y-1))
            if self.grille[voyageur.pos.x][voyageur.pos.y+1]==False:
                liste_cases_vide.append(Coord(voyageur.pos.x,voyageur.pos.y+1))
            if liste_cases_vide != []:   # Si la liste n'est pas vide, on cherche le déplacement optimal
                distances=[]
                for point in liste_cases_vide:
                    distance2=point.x*voyageur.dest.x+point.y*voyageur.dest.y
                    distances.append(distance2)
                i_minimum=distances.index(min(distances)) # Indice de la distance minimum
                dvect=Coord(voyageur.pos.x-liste_cases_vide[i_minimum].x,voyageur.pos.y-liste_cases_vide[i_minimum].y)
            else:                      # Toutes les cases alentours sont occupées : on ne déplace pas le voyageur
                dvect=Coord(0,0) 
        # Cas où la case où veut se déplacer le voyageur est vide
        self.grille[voyageur.pos.x][voyageur.pos.y]=False
        voyageur.pos.x += dvect.x
        voyageur.pos.y += dvect.y
        self.grille[voyageur.pos.x][voyageur.pos.y]=True
        # Fin de la 2ème solution
        
        # Suppression du voyageur de la carte dans le cas où il a atteint sa destination
        if voyageur.pos.x==voyageur.dest.x and voyageur.pos.y==voyageur.dest.y:
            self.retirer_element(voyageur)
    
    def move(self):                             # Méthode qui déplace tous les voyageurs
        while self.compteurVoyageurs != 0:       # Tant qu'il y a un voyageur dans la carte
            for elem in self.elements:
                self.deplacer_voyageur(elem)
                #self.afficher_grille()
                #print('\n')
       
    def __str__(self):
        return 'Carte=' + '(' + str(self.dimCarte.x) + ";" + str(self.dimCarte.y) + ')' + '\n' + 'Grille=' + '(' + str(self.dimGrille.x) + ";" + str(self.dimGrille.y) + ')' + '\n' + 'Nb éléments : ' + str(len(self.elements))
     
from random import randint

# Dimension de la grille
dimensions=Coord(10,10)

# Création de la carte
carte=Carte(dimensions,dimensions)

# Création des 10 voyageurs
#for i in range(2):
#    carte.ajouter_element(Voyageur(Coord(randint(0,9),randint(0,9)),Coord(0,0)))
carte.ajouter_element(Voyageur(Coord(4,0),Coord(4,9)))
carte.ajouter_element(Voyageur(Coord(4,9),Coord(4,0)))
carte.ajouter_element(Voyageur(Coord(3,0),Coord(3,9)))
carte.ajouter_element(Voyageur(Coord(3,9),Coord(3,0)))
carte.ajouter_element(Voyageur(Coord(5,0),Coord(5,9)))
carte.ajouter_element(Voyageur(Coord(5,9),Coord(5,0)))
