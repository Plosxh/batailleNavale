import unittest
from Bataille import *
from player import *
class TestBataille(unittest.TestCase):

    def test_Base(self):
        nbCase = 10
        jeu = Jeu(nbCase)
        self.assertEqual(False,jeu.get_Grille(1,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Grille(1,nbCase +1))

    def test_Player(self):
        joueur = Player("Olivier")
        self.assertEqual("Olivier",joueur.get_Nom())
        joueur.gagne()
        self.assertEqual(1, joueur.get_Score())
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())
        joueur.perd()
        self.assertEqual(0, joueur.get_Score())

        
       


unittest.main()    
