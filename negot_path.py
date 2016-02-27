# -*- coding: utf-8 -*-
# Goal: draw the evolution of a negotiation
""" disegno 
    posizione in /home/ca/Dropbox/Dojo_Python/negotiation/    
    """
# import unittest 
import os
from os import path
import matplotlib.pyplot as plt
import numpy as np
# import ML


# global 
HERE = os.path.dirname(os.path.realpath(__file__))

def fench_files(relative_path):   # relative path

    # files = [f for f in os.listdir(HERE+"/"+relative_path) if path.isfile(f)]
    files = [f for f in os.listdir(HERE+"/"+relative_path) \
             if os.path.isfile(os.path.join(HERE +"/"+relative_path, f))]
    # print "trovato: ", files
    return files

def from_text_to_objects(lista):
    """from text list to a text and object list"""
    content = []
    for i in lista:     # ex. stato("Actor A", (10,10), "caption a") 
        # print i[:7]
        """
        if i[:7] == 'stato("': 
            print "» tranform text in a object due from_text_to_objects"
            print i #str(i) 
            parts = i.split(",")
            # parts[1] have to be a tupla of integer, not a str
            no_brack = parts[1].strip("() ")
            coords = tuple( [int(x) for x in no_brack.split(",")]  )
            content.append(stato(parts[6:-1], coords, parts[1][:-1]) )
        else:
            content.append(i)
    # print content
           """
    # content = [["pippo"], "Actor A: satisfaction"]   
    # content = [["pippo"], stato("Actor A", (10,10), "caption a")]
    
    # parts[1] have to be a tupla of integer, not a str
    
    i = '- "Actor A", (10,10), "caption a"'

    parts = i.split('"') 
    # parts = ['"stato("Actor A"', '(10,10)', '"caption a"']
    # parts[1]
    parts_one = parts[2]
    # parts_one = " ( 10 , 10 )"
    no_brack = parts_one.strip("() ,")
    coords = tuple( [int(x) for x in no_brack.split(",")]  )
    # coords = tuple( [int(10), int(10)]) 
    content = [["pippo"], stato("Actor A", coords, "caption a")]

    return content  # 

class stato():
    def __init__(self, nome, coppia, commento):  # commento obbligatorio
        self.nome = nome
        # print type(self.nome)
        self.coppia = coppia        # a tuple
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
            stringa += "; \n\tComment: " + str(self.comment)
            """print "".join(str(self.comment))
            print type(self.comment)"""
        return stringa       

class dynamic():
    """ The aim is to write in almost human style the dynamic, 
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

    def estrai_punti(self):
        atr = [ attore[1] for attore in self.state_list()]
        # print atr
        coord_x =  [[ coppia[0] for coppia in lista] for lista in atr]
        coord_y  = [[ coppia[1] for coppia in lista] for lista in atr]
        coord = zip(coord_x, coord_y)
        return coord

    def elenca_fasi(self):
        # recupero una lista degli attori nella negoziazione
        fasi = []
        i = 1
        for punto in self.punti:
            if not(isinstance(punto, stato)):
                fasi.append(str(i) + ". " + punto)
                i += 1
        return fasi

    def draw_dynamic(self):
        """ Disegna, affiancate, due liste
        http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
        """
        coordinate_di_tutti = self.estrai_punti()
        actrs = [x[0] for x in self.state_list()]
        print coordinate_di_tutti, actrs
        j = 0 
        for i in coordinate_di_tutti:
            plt.plot(i[0], i[1], '-o', label=actrs[j])
            j+=1
            plt.text(i[0][0], i[1][0], 'Start', style='italic',
                 bbox={'facecolor':'red', 'alpha':0.3, 'pad':6})
            plt.text(i[0][-1], i[1][-1], 'End', style='italic',
                 bbox={'facecolor':'green', 'alpha':0.3, 'pad':6})
            # http://matplotlib.org/1.3.1/users/text_intro.html
            # http://matplotlib.org/users/annotations_guide.html

        plt.title('The negotiation dynamic in a figure')
        plt.xlabel("Actor's sadisfaction")        #  axis {acses} (sing.); axes {acsis} (plur.)
        plt.ylabel("Actor's cooperation")
        plt.legend(loc='upper center', shadow=True)
        value_min = -20
        value_max = 120
        axes = plt.gca()
        axes.set_xlim([value_min, value_max])
        axes.set_ylim([value_min, value_max])
        ax = plt.gca()
        ax.grid(True)
        plt.show()

# Esecuzione ========================================
if __name__ == "__main__":
    
    passo = ["Movie: 'Romeo & Giulietta'",
             'stato("Romeo", ( 3 , 33 ), "Their love ...")',]


    from_text_to_objects(passo)
    
    """for case in fench_files("dynamics"):
        with open(  HERE+"/dynamics/"+ case, 'r') as data:
            data_list = [line for line in data.readlines()]  
            
            print data_list
            dinamica = dynamic(data_list)
            dinamica.draw_dynamic()
    """

    st = stato("Mike", (90,6),
               "A Mike interessa ...solo la sua rivincita, \
               per interposta persona")
    print st


    Rocky = [stato("Mike", (90,6), "interessato solo a una sua rivincita"),
             stato("Rocky", (20,40), "spaventato e senza incentivi"),
             stato("Adriana", (80,80), "she is not aware of the negotiation"),
             "una visita inaspettata ed una proposta troppo rapida ed egoista", 
             stato("Rocky", (10,20), "Rocky di chiude in se stesso e nel bagno"),
             stato("Mike", (10,6), "non trova il modo di dialogo"), 
             "Parole in libertá", 
             stato("Mike", (90,77), "Rocky lo accetta"),
             stato("Rocky", (70,70), "Rocky di chiude in sè stesso e nel bagno"), 
             "",
             stato("Adriana", (90,88), "she's happy about the coach"), 
               ]
    
    n_Rocky = dynamic(Rocky)
    
    n_Rocky.draw_dynamic()           