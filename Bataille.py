
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
