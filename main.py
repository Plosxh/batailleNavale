import unittest
from Bataille import *

class TestBataille(unittest.TestCase):

    def Test_Base(self):
        nbCase = 10
        jeu = Jeu(nbCase)
        self.assertEqual(true,jeu.getGrille(1,1))
        self.assertEqual("Error out of bound",jeu.getGrille(1,nbCase +1))
    


unittest.main()    
