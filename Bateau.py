class Bateau:

    def __init__(self,largeur,longueur):
        self._bateau = {}
        self._largeur = largeur
        self._longueur = longueur
        for i in range(largeur):
            rows = {}
            for j in range(longueur):
                rows[j] = False
            self._bateau[i] = rows

    def est_Touche(self,x,y):
        self._bateau[x][y] = True

    def est_Coule(self):
        for i in range(self._largeur):
            for j in range(self._longueur):
                if self._bateau[i][j] == False:
                    return False
        return True