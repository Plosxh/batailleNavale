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

    def tire(self,x,y,joueur):

        case_visee = joueur.get_Grille().get_Case(x,y)
        if case_visee >= 0:
            try:
               bateau = joueur.get_Bateaux()[case_visee]
               caseX,caseY = bateau.get_Coords()
               bateau.est_Touche(x-caseX,y-caseY)
               print("Touché !")
               if bateau.est_Coule():
                   print("Coulé !")
                   joueur.get_Bateaux().pop(bateau.get_ID())

            except ValueError:
               if case_visee== CONST_TRUE:
                   print("Vous avez touché une île !")
               else:
                   print("Coup dans l'eau !")
