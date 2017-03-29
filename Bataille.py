
class Jeu:
    def __init__(self,nbCase):
        self._grille = {}
        for i in range(nbCase):
            rows = {}
            for j in range(nbCase):
                rows[j]=False
            self._grille[i]=rows

    def jouer(self):
        print ("toto")

    def get_Grille(self,x,y):

        try:
            return self._grille[x][y]
        except KeyError:
            return "Error Out Of Bound"

    def ajout_Bateau(self,caseX,caseY,bateau):

        try:
