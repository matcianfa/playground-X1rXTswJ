#Ne pas oublier de changer le module à importer
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import io
import numpy as np
from math import *
from courbe_dragon_plot import *

input_output=[\
(1,([0, 1], [0, 0])),\
(5,([0, 1, 1, 0, 0, -1], [0, 0, 1, 1, 2, 2])),\
(20,([0, 1, 1, 0, 0, -1, -1, -2, -2, -3, -3, -2, -2, -3, -3, -4, -4, -5, -5, -4, -4], [0, 0, 1, 1, 2, 2, 1, 1, 2, 2, 1, 1, 0, 0, -1, -1, 0, 0, -1, -1, -2]))\
]

#valeur de n pour la représentation de la courbe
n_dessin=100000

#message d'aide si besoin
help="N'oublie pas d'utiliser return x_f,y_f pour afficher le resultat"

    

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ index_grossissant.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for n,rep in input_output:
        res=mon_programme(n)
        assert rep==res , "Les coordonnées obtenues pour n={} sont {} au lieu de {}".format(str(n),str(res),str(rep))
        send_msg("Résultats validés", "Les coordonnées du dernier point pour n ={} sont bien {}".format(str(n),str(res)))
      fig=plt.figure()
      mon_programme(n_dessin)
      plt.axis('equal')
      plt.axis('off')
      fig.savefig('output.png', dpi=fig.dpi)
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
