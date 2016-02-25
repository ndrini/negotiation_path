# -*- coding: utf-8 -*-
"""                   """
import unittest 
import os
import numpy as np
import matplotlib.pyplot as plt
import negot_path as nepa


class circa_la_esecuzione(unittest.TestCase):

    def test_fench_files(self):
        """ Can the program fench files from the test directory? """
        all_files = nepa.fench_files("test")   # relative path
        # print all_files
        self.assertTrue("file_2.txt" in all_files)


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

    def test_numero_di_fasi(self):
        """ Are there enough "stato" for number of phases?"""
        punti = [nepa.stato("Mike", (90,6), "interessato solo"),
                nepa.stato("Rocky", (20,40), "spaventato e "),
                "una visita inaspettata ed una proposta troppo rapida ed egoista", 
                nepa.stato("Mike", (10,6), "non trova "), 
                nepa.stato("Mike", (90,80), "Rocky lo"),
                "Rocky chiude la comunicazione rifugiandosi in bagno", ]
        p = nepa.dynamic(punti)        
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

    def test_estrai_punti(self):
        punti = [nepa.stato("Mike", (90,6), "interessato solo"),
                nepa.stato("Rocky", (20,40), "spaventato e "),
                "una visita inaspettata ed una proposta troppo rapida ed egoista", 
                nepa.stato("Mike", (10,6), "non trova "), 
                nepa.stato("Mike", (90,80), "Rocky lo"),
                "Rocky chiude la comunicazione rifugiandosi in bagno", ]
        p = nepa.dynamic(punti)        
        self.assertEqual( p.estrai_punti()[0], ([90, 10, 90],[6, 6, 80]))
        pass

def main():
    unittest.main()

# Esecuzione ========================================
if __name__ == "__main__":
    
    print "Ciao, \n\tinizia il test"
    main()
    print "Arrivederci"
