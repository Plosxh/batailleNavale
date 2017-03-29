class Player:

    def __init__ (self,nom,bateau):
        self._score = 0
        self._nom = nom
        self._bateaux = bateau

    def gagne(self):
        self._score += 1

    def perd(self):
        if self._score > 0:
            self._score -= 1

    def get_Score(self):
        return self._score

    def get_Nom(self):
        return self._nom

    def get_Bateau(self):
        return self._bateaux





















