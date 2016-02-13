# -*- coding: utf-8 -*-
"""                   """
import unittest 
import os
import numpy as np
# import ML
import matplotlib.pyplot as plt

import negot_path as nepa



# a1 = ahp.ahp()

class LearningCase(unittest.TestCase):

    def setUp(self):
        pass # plt.close('all') # closes all the figure windows

    def tearDown(self):    
        pass # plt.close('all') # closes all the figure windows

    """def test_input_leggi(self):
        # valuto se prende casualmente un numero
        self.assertEqual(a1.input(), ['a', 's'])"""

    def test_giudizio_da_matrice(self):
        """valuto se uno stato - coppia di valori - 
        ha la giusta dimensione """
        
        inizio = nepa.stato("Rocky", (30, 50))        # Rocky era impaurito e desideroso di una guida

        self.assertTrue(inizio.dimensione_ok())
        # self.assertEqual(a1.giudizio_da_matrice([[1, 1, 1], [1, 1, 1], [1, 1, 1]])[2, 0], 1./3)
        # errore se input int !!!

        inizio_fulanito = nepa.stato("Fulanito", (30,))        
        self.assertFalse(inizio_fulanito.dimensione_ok())

        inizio_fulanito = nepa.stato("Fulanito", (30,31,31,33))
        self.assertFalse(inizio_fulanito.dimensione_ok())


def main():
    unittest.main()

# Esecuzione ========================================
if __name__ == "__main__":
    
    print "ciao"
    main()
    print "arrivederci"
