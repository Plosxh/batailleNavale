import unittest
from Grille import *
from player import *
from Jeu import *
from Bateau import *

class TestBataille(unittest.TestCase):

    def test_Base(self):
        nbCase = 10
        jeu = Grille(nbCase)
        self.assertEqual(False,jeu.get_Case(1,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Case(1,nbCase +1))

    def test_Bateau(self):
        bateau = Bateau(1,2,1)
        bateau.est_Touche(0,0)
        self.assertEqual(False, bateau.est_Coule())
        bateau.est_Touche(0,1)
        self.assertEqual(True,bateau.est_Coule())

    def test_Player(self):
        bateaux = {}
        joueur = Player("Olivier",bateaux,1,10)
        self.assertEqual("Olivier",joueur.get_Nom())
        joueur.gagne()
        self.assertEqual(1, joueur.get_Score())
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())

    def test_Ajout_Bateau(self):
        nbCase = 10
        jeu = Grille(nbCase)
        bateau = Bateau(1,2,1)
        jeu.ajout_Bateau(1,1,bateau)
        self.assertEqual(True,jeu.get_Case(1,1))
        self.assertEqual(False,jeu.get_Case(3,2))

    def test_Creation_Joueur(self):
        nomJ1 = "Toto"
        nomJ2 = "Albert"
        nbBateaux = 3
        bateaux = {}

        for i in range(nbBateaux):
            bateau = Bateau(2,2,i)
            bateaux[i]=bateau

        p1 = Player(nomJ1,bateaux,1,10)
        p2 = Player(nomJ2,bateaux,2,10)

        self.assertEqual("Toto",p1.get_Nom())
        self.assertEqual("Albert",p2.get_Nom())
        self.assertEqual(2,p1.get_Bateaux()[0].get_Largeur())
        self.assertEqual(2,p2.get_Bateaux()[0].get_Largeur())
        #print(p1.get_Bateaux()[0])

    def test_Jeu(self):
        jeu = Jeu(3)

        self.assertEqual(True,jeu.init_Jeu())
        self.assertEqual(1,jeu.get_Joueurs()[1].get_Grille().get_Case(1,1))
        self.assertEqual(1,jeu.get_Joueurs()[2].get_Grille().get_Case(1,1))

        self.assertEqual(2,jeu.get_Joueurs()[1].get_Grille().get_Case(1,6))
        self.assertEqual(2,jeu.get_Joueurs()[2].get_Grille().get_Case(1,6))

        self.assertEqual(0,jeu.get_Joueurs()[1].get_Grille().get_Case(5,1))
        self.assertEqual(0,jeu.get_Joueurs()[2].get_Grille().get_Case(5,1))

        self.assertEqual("Error Out Of Bound",jeu.get_Joueurs()[1].get_Grille().get_Case(40,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Joueurs()[2].get_Grille().get_Case(40,1))


    def test_tir(self):

        jeu= Jeu(3)
        jeu.init_Jeu()
        joueurs = jeu.get_Joueurs()
        joueurs[1].tire(1,1,joueurs[2])
        self.assertEqual(False, joueurs[2].get_Bateaux()[1].est_Coule())



unittest.main()
