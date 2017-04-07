from random import randint
from player import * # Player -> player
from Bateau import *

class Jeu:

    def __init__(self):
        self._current_player = randint(1,2)
        self._nbBateaux = 3
        self._joueurs = {}

    def get_Current_Player(self):
        return self._current_player

    def init_Jeu(self):

        nbBateaux = 3
        bateaux = {} # il faudrait utiliser l'attribut déclaré plus haut
        print("Le nombre de bateaux de cette partie est : " + str(nbBateaux))

        for i in range(nbBateaux):
            bateaux[i]= Bateau(2,2)
            print("Bateau de "+str(bateaux[i].get_Largeur())+"*"+str(bateaux[i].get_Longueur())+" ajouté.")

        self._joueurs[1] = Player("Toto",bateaux,1,10)
        self._joueurs[2] = Player("Albert",bateaux,2,10)
        for i in range(len(bateaux)):
            print(str(self._current_player)+" à vous de placer un bateau : ")
            print("Veuillez placer votre bateau de "+str(bateaux[i].get_Largeur())+"*"+str(bateaux[i].get_Longueur())+".")
            if i == 1:
                self._joueurs[1].get_Grille().ajout_Bateau(1,1,bateaux[i])
                self._joueurs[2].get_Grille().ajout_Bateau(1,1,bateaux[i])
            elif i == 2:
                self._joueurs[1].get_Grille().ajout_Bateau(1,6,bateaux[i])
                self._joueurs[2].get_Grille().ajout_Bateau(1,6,bateaux[i])
            else:
                self._joueurs[1].get_Grille().ajout_Bateau(5,1,bateaux[i])
                self._joueurs[2].get_Grille().ajout_Bateau(5,1,bateaux[i])


        return True
