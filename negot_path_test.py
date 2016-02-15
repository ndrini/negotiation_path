# -*- coding: utf-8 -*-
"""                   """
import unittest 
import os
import numpy as np
# import ML
import matplotlib.pyplot as plt
import negot_path as nepa

class circa_lo_stato(unittest.TestCase):

    def test_giudizio_da_matrice(self):
        """valuto se uno stato - coppia di valori - 
        ha la giusta dimensione """
        
        inizio = nepa.stato("Rocky", (30, 50), "")        # Rocky era impaurito e desideroso di una guida
        self.assertTrue(inizio.dimensione_ok())
        # self.assertEqual(a1.giudizio_da_matrice([[1, 1, 1], [1, 1, 1], [1, 1, 1]])[2, 0], 1./3)
        # errore se input int !!!

        inizio_fulanito = nepa.stato("Fulanito", (30,), "")        
        self.assertFalse(inizio_fulanito.dimensione_ok())

        inizio_fulanito = nepa.stato("Fulanito", (30,31,31,33), "troppi numeri iniziali!!")
        self.assertFalse(inizio_fulanito.dimensione_ok())

    def test_rende_il_nome(self):
        """traduco umanamente leggibile """
        st = nepa.stato("Mike", (90,6), "interessato solo ...")
        self.assertEqual(str(st), "Mike: satisfaction = 90; cooperation = 06; Comment: ")


class Circa_la_dinamica(unittest.TestCase):

    def setUp(self):
        pass # plt.close('all') # closes all the figure windows

    def tearDown(self):    
        pass # plt.close('all') # closes all the figure windows

    def test_numero_di_fasi(self):
        """ Are there enougt "stato" for number of fasi?"""
        punti = [nepa.stato("Mike", (90,6), "interessato solo"),
                nepa.stato("Rocky", (20,40), "spaventato e "),
                "una visita inaspettata ed una proposta troppo rapida ed egoista", 
                nepa.stato("Mike", (10,6), "non trova "), 
                nepa.stato("Mike", (90,80), "Rocky lo"),
                "Rocky chiude la comunicazione rifugiandosi in bagno", ]
        p = nepa.dinamic(punti)        
        self.assertEqual( p.state_list(),
                        [ 
                            ["Mike", [(90,6), (10,6), (90,80)] ,
                                ["interessato solo",
                                "non trova ", 
                                "Rocky lo"]], 
                            ["Rocky", [(20,40)], 
                                ["spaventato e "]
                                ]
                                ])
        self.assertEqual( p.elenca_fasi(),
                        [ "1. una visita inaspettata ed una proposta troppo rapida ed egoista", 
                          "2. Rocky chiude la comunicazione rifugiandosi in bagno", 
                          ])


def main():
    unittest.main()

# Esecuzione ========================================
if __name__ == "__main__":
    
    print "ciao"
    main()
    print "arrivederci"
