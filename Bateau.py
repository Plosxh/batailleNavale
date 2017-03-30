class Bateau:

    def __init__(self,largeur,longueur):
        self._bateau = {}
        self._largeur = largeur
        self._longueur = longueur
        self._coordX = 0
        self._coordY = 0
        for i in range(largeur):
            rows = {}
            for j in range(longueur):
                rows[j] = False
            self._bateau[i] = rows

    def est_Touche(self,x,y):
        try:
            self._bateau[x][y] = True
        except KeyError:
            return "Error Out Of Bound"

    def est_Coule(self):
        for i in range(self._largeur):
            for j in range(self._longueur):
                if self._bateau[i][j] == False:
                    return False
        return True

    def set_Coords(self,x,y):
        self._coordX = x
        self._coordY = y

    def get_Coords(self):
        return self._coordX, self._coordY

    def get_Largeur(self):
        return self._largeur

    def get_Longueur(self):
        return self._longueur
