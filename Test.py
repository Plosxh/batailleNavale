import unittest
from Grille import *
from player import * # Player -> player (attention, windows est tolérant avec la casse, mais votre projet n'était du coup plus portable)
from Jeu import *
from Bateau import *

# à séparer en plusieurs classes (une pour chaque fonctionnalité)
class TestBataille(unittest.TestCase):

    def test_Base(self):
        nbCase = 10
        jeu = Grille(nbCase) # j'ai mis 30 secondes à comprendre comment votre code pouvait s'éxecuter alors que la classe "Jeu" ne comporte pas de méthode "get_Grille" : attention aux noms !
        self.assertEqual(False,jeu.get_Grille(1,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Grille(1,nbCase +1))

    def test_Bateau(self):
        bateau = Bateau(1,2)
        bateau.est_Touche(0,0)
        self.assertEqual(False, bateau.est_Coule())
        bateau.est_Touche(0,1)
        self.assertEqual(True,bateau.est_Coule())
        # c'est une bonne première étape, vous testez le cas général. Il faudrait également tester les cas limites : bateau.est_Touche(-1,-1), batau.est_Touche(Math.pi, 8000), etc

        
    def test_Player(self):
        # ce test n'est pas unitaire ;) il faudrait le découper :
        bateaux = {}
        joueur = Player("Olivier",bateaux,1,10)
        self.assertEqual("Olivier",joueur.get_Nom())
        # là
        joueur.gagne() 
        self.assertEqual(1, joueur.get_Score())
        # ici
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())
        # et éventuellement là (dans un test séparé qui effectue plusieurs fois l'action)
        joueur.perd() 
        self.assertEqual(0, joueur.get_Score())

    def test_Ajout_Bateau(self):
        nbCase = 10
        jeu = Grille(nbCase) # /repeat "attention aux noms" !
        bateau = Bateau(1,2)
        jeu.ajout_Bateau(1,1,bateau)
        self.assertEqual(True,jeu.get_Grille(1,1))
        self.assertEqual(False,jeu.get_Grille(3,2))

    def test_Creation_Joueur(self):
        nomJ1 = "Toto"
        nomJ2 = "Albert"
        nbBateaux = 3
        bateaux = {}

        for i in range(nbBateaux):
            bateau = Bateau(2,2)
            bateaux[i]=bateau

        p1 = Player(nomJ1,bateaux,1,10)
        p2 = Player(nomJ2,bateaux,2,10)

        self.assertEqual("Toto",p1.get_Nom()) # vous avez déjà fait ce test plus haut, il faut lui faire confiance et tester une autre fonctionnalité
        self.assertEqual("Albert",p2.get_Nom())
        self.assertEqual(2,p1.get_Bateaux()[0].get_Largeur())
        self.assertEqual(2,p2.get_Bateaux()[0].get_Largeur())
        #print(p1.get_Bateaux()[0])

    def test_Jeu(self):
        jeu = Jeu()

        self.assertEqual(True,jeu.init_Jeu()) # cette fonction retourne forcément True si elle termine, vous auriez pu faire une fonction void et simplement l'appeler

unittest.main()
