from Grille import *

class Player:

    def __init__ (self,nom,bateaux, id, tailleGrille):
        self._score = 0
        self._nom = nom
        self._id = id
        self._bateaux = bateaux
        self._grille = Grille(tailleGrille)

    def gagne(self):
        self._score += 1

    def perd(self):
        if self._score > 0:
            self._score -= 1

    def get_Score(self):
        return self._score

    def get_Nom(self):
        return self._nom

    def get_Bateaux(self):
        return self._bateaux

    def get_ID(self):
        return self._id

    def get_Grille(self):
        return self._grille
