from random import randint
from main import *
from Player import *
from Bateau import *

CONST_TRUE = -1
CONST_FALSE = -2

class Jeu:

    def __init__(self):
        self._current_player = 0
        self._nbBateaux = 0
        self._joueurs = {}

    def get_Current_Player(self):
        return self._current_player

    def set_Bateau(self,x):
        self._nbBateaux = x

    def test_int(self,valueX,valueY=0):
        try:
            x = int(valueX)
            y = int(valueY)
            return True , x , y
        except ValueError:
            print("Les valeurs rentrées ne sont pas des chiffres")
            return False, 0, 0

    def get_Joueurs(self):
        return self._joueurs

    def init_Jeu(self):
        self._current_player = randint(1,2)
        bateaux = {}
        print("Le nombre de bateaux de cette partie est : " + str(self._nbBateaux))

        for i in range(self._nbBateaux):
            bateaux[i]= Bateau(2,2,i)
            print("Bateau de "+str(bateaux[i].get_Largeur())+"*"+str(bateaux[i].get_Longueur())+" ajouté.")

        self._joueurs[1] = Player("Toto",bateaux,1,10)
        self._joueurs[2] = Player("Albert",bateaux,2,10)
        for i in range(len(self._joueurs)):
            for i in range(len(bateaux)):
                print("==================================================================")
                print(str(self._current_player)+" à vous de placer un bateau : ")
                print("Veuillez placer votre bateau de "+str(bateaux[i].get_Largeur())+"*"+str(bateaux[i].get_Longueur())+".")

                while True:
                    line = input('Entrez les coordonnées du bâteau sous forme: x,y : ')
                    coord = line.split(',')
                    if len(coord)>2:
                        print("Mauvais nombre de carractères")
                    else:
                        test,x,y = self.test_int(coord[0],coord[1])
                        if test:
                            self._joueurs[self._current_player].get_Grille().ajout_Bateau(x,y,bateaux[i])
                            break
            if self._current_player == 1:
                self._current_player = 2
            else:
                self._current_player = 1

        return True

    def tour(self):
        print("==================================================================")
        print(self._joueurs[self._current_player].get_Nom()+" c'est votre tour !")
        line = input('Entrez les coordonnées du tir sous forme: x,y : ')
        coord = line.split(',')
        if len(coord)>2:
            print("Mauvais nombre de carractères")
        else:
            try:
                x = int(coord[0])
                y = int(coord[1])
                if self._current_player == 1:
                    self._joueurs[1].tire(x,y,self._joueurs[2])
                    self._current_player = 2
                else:
                    self._joueurs[2].tire(x,y,self._joueurs[1])
                    self._current_player = 1
            except ValueError:
                print("Les valeurs rentrées ne sont pas des chiffres")


jeu= Jeu()
line = input('Bienvenue dans la bataille navale entrez un nombre de bâteaux sous forme d\'entier : ')
test,x,y = jeu.test_int(line)
jeu.set_Bateau(x)
jeu.init_Jeu()
j1 = jeu.get_Joueurs()[1]
j2 = jeu.get_Joueurs()[2]

while len(j1.get_Bateaux())>0 and len(j1.get_Bateaux())>0:
    jeu.tour()


if len(j1.get_Bateaux())==0:
    print(j2.get_Nom() + " a gagné !")
else:
    print(j1.get_Nom() + " a gagné !")
