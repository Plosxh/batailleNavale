
class Grille:
    def __init__(self,nbCase):
        self._grille = {} # CF Bateau.py
        for i in range(nbCase):
            rows = {}
            for j in range(nbCase):
                rows[j]=False
            self._grille[i]=rows

    def get_Grille(self,x,y):
        try:
            return self._grille[x][y]
        except KeyError:
            return "Error Out Of Bound"

    def ajout_Bateau(self,caseX,caseY,bateau):
        try:
            for i in range(bateau.get_Largeur()):
                self._grille[caseX+i][caseY] = True

            for i in range(bateau.get_Longueur()):
                self._grille[caseX][caseY+i] = True
        except TypeError:
            #print(self._grille)
            print("Couldn't place Boat") # encore mieux si vous faites un print sur la sortie d'erreur : print("...", file=sys.stderr)
