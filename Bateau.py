class Bateau:

    
    # bon point : les attributs privés commencent par "_"
    def __init__(self,largeur,longueur):
        self._bateau = {} # attribut = nom de classe -> pas top
        self._largeur = largeur
        self._longueur = longueur
        self._coordX = 0
        self._coordY = 0
        for i in range(largeur):
            rows = {}
            for j in range(longueur):
                rows[j] = False
            self._bateau[i] = rows
        #ici, bateau est un dictionnaire de dictionnaires, il aurait mieux valu un tableau de tableau

        # cette fonction est nommée comme un getter, mais a une action sur l'objet
        # principe à respecter : getter -> voix passive (est_touché, a_du_carburant, get_height...) ; setter -> voix active (toucher, remplir_reservoir, set_flag...)
    def est_Touche(self,x,y):
        try: # <---- très bien ça, c'est pythonique !
            self._bateau[x][y] = True
        except KeyError:
            return "Error Out Of Bound"

    def est_Coule(self):
        for i in range(self._largeur):
            for j in range(self._longueur):
                if self._bateau[i][j] == False:
                    return False
        return True

    # il faut choisir une norme de noms : soit vous écrivez "ma_fonction" (la façon standard en python), soit "maFonction", mais si vous faites les deux au final vous ne respectez plus aucun standard
    def set_Coords(self,x,y):
        self._coordX = x
        self._coordY = y

    def get_Coords(self):
        return self._coordX, self._coordY

    def get_Largeur(self):
        return self._largeur

    def get_Longueur(self):
        return self._longueur
