CONST_TRUE = -1
CONST_FALSE = -2

class Grille:
    def __init__(self,nbCase):
        self._grille = {}
        for i in range(nbCase):
            rows = {}
            for j in range(nbCase):
                rows[j]=CONST_FALSE
            self._grille[i]=rows

    def get_Case(self,x,y):
        try:
            return self._grille[x][y]
        except KeyError:
            return "Error Out Of Bound"

    def ajout_Bateau(self,caseX,caseY,bateau):
        try:
            for i in range(bateau.get_Largeur()):
                for j in range(bateau.get_Longueur()):
                    if self._grille[caseX+i][caseY+j] == CONST_FALSE:
                        self._grille[caseX+i][caseY+j] = bateau.get_ID() #bateau.get_ID()
                    elif self._grille[caseX+i][caseY+j] == CONST_TRUE:
                        print("Il y a deja un bâteau ici !")



        except TypeError:
            #print(self._grille)
            print("Couldn't place Boat")
