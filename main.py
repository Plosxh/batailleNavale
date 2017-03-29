import unittest
from Bataille import *
from Bateau import *

class TestBataille(unittest.TestCase):

    def test_Base(self):
        nbCase = 10
        jeu = Jeu(nbCase)
        self.assertEqual(False,jeu.get_Grille(1,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Grille(1,nbCase +1))

    def test_Bateau(self):
        bateau = Bateau(1,2)
        bateau.est_Touche(0,0)
        self.assertEqual(False, bateau.est_Coule())
        bateau.est_Touche(0,1)
        self.assertEqual(True,bateau.est_Coule())
       


unittest.main()    
