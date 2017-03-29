import unittest
from Bataille import *
from player import *
from Bateau import *

class TestBataille(unittest.TestCase):

    def test_Base(self):
        nbCase = 10
        jeu = Jeu(nbCase)
        self.assertEqual(False,jeu.get_Grille(1,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Grille(1,nbCase +1))

    def test_Bateau(self):
        bateau = Bateau(2,1)
        bateau.est_Touche(0,0)
        self.assertEqual(False, bateau.est_Coule())
        self.assertEqual("Error Out Of Bound", bateau.est_Touche(1, 1))
        bateau.est_Touche(1,0)
        self.assertEqual(True,bateau.est_Coule())

    def test_Player(self):
        joueur = Player("Olivier")
        self.assertEqual("Olivier",joueur.get_Nom())
        joueur.gagne()
        self.assertEqual(1, joueur.get_Score())
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())

    #def test_Ajout_Bateau(self):
        #nbCase = 10
        #jeu = Jeu(nbCase)
        #bateau = Bateau(x,y)
        #self.assertEqual(True,jeu.ajout_Bateau(1,1,bateau))
        #self.assertEqual(True,jeu.ajout_Bateau(1,nbCase+1,bateau))


unittest.main()
