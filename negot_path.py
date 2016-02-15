# -*- coding: utf-8 -*-
# Goal: draw the evolution of a negotiation
""" disegno 
    posizione in /home/ca/Dropbox/Dojo_Python/negotiation/    
    """
# import unittest 
import os
import matplotlib.pyplot as plt
import numpy as np
# import ML

class stato():

    def __init__(self, nome, coppia, commento):  # commento obbligatorio
        self.nome = nome
        # print type(self.nome)
        self.coppia = coppia 
        self.comment = commento
        # print type(self.comment)

    def stop(self):
        raw_input("»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»»\n\n")
        pass

    def dimensione_ok(self, ):
        """max(mylist, key=len)"""
        if len(self.coppia) == 2:
            return True
        else:
            return False

    def __str__(self,):
        
        stringa = self.nome + ": satisfaction = " + \
                  str( '%02d' % self.coppia[0]) + "; cooperation = "\
                  + str('%02d' % self.coppia[1]) 
        if self.comment:
            stringa += "; Comment: " # + str(self.comment)
            """print "".join(str(self.comment))
            print type(self.comment)"""
        return stringa       

class dinamic():
    """ The aim is to write in almost human style the dinamic, 
        by join the states and the phases in a list,
        and then have the plot and the list by character """
    def __init__(self, punti):
        self.punti = punti

    def select_actors(self):
        lista = []
        for punto in self.punti:
            if isinstance(punto, stato):    # isinstance(obj, MyClass)
                lista.append(punto.nome) 
            actors = list(set(lista))    
        # actors = list(set([x[0] for x in self.punti if isinstance(x,stato) ]))
        # print actors    
        return actors

    def state_list(self):
        # recupero una lista degli attori nella negoziazione
        actors = self.select_actors() 
        lista_coordinate = []
        for actor in actors:
            coordinate = []
            commenti   = []
            for punto in self.punti:
                if isinstance(punto, stato):
                    if punto.nome == actor:
                        coordinate.append(punto.coppia)
                        commenti.append(punto.comment)
            estrazione = [actor, coordinate, commenti]        
            lista_coordinate.append(estrazione)
        return lista_coordinate

    def elenca_fasi(self):
        # recupero una lista degli attori nella negoziazione
        fasi = []
        i = 1
        for punto in self.punti:
            if not(isinstance(punto, stato)):
                fasi.append(str(i) + ". " + punto)
                i += 1
        return fasi


# Esecuzione ========================================
if __name__ == "__main__":
    st = stato("Mike", (90,6),
               "A Mike interessa ...solo la sua rivincita, \
               per interposta persona")
    print st

    stati = [ stato("Mike", (90,6), "interessato solo a una sua rivincita"),
               stato("Rocky", (20,40), "spaventato e senza incentivi"),
                # "una visita inaspettata ed una proposta troppo rapida ed egoista", 
               stato("Mike", (10,6), "non trova il modo di dialogo"), 
               stato("Mike", (90,80), "Rocky lo accetta"),]
    