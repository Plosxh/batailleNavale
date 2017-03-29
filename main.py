import unittest
from Bataille import *

class TestBataille(unittest.TestCase):

    def test_Base(self):
        nbCase = 10
        jeu = Jeu(nbCase)
        self.assertEqual(False,jeu.get_Grille(1,1))
        self.assertEqual("Error Out Of Bound",jeu.get_Grille(1,nbCase +1))
        
        
       


unittest.main()    
