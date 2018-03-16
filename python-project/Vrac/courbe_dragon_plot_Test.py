#Ne pas oublier de changer le module à importer
from courbe_dragon_plot import *
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import io
import numpy as np
from math import *

input_output=[\
(1,(1,0)),\
(3,(0,1)),\
(5,(-1,2)),\
(10,(-3,1)),\
(20,(-4,-2)),\
(100,(4,-6))\
]

#valeur de n pour la représentation de la courbe
n_dessin=10000

#message d'aide si besoin
help="N'oublie pas d'utiliser return x_f,y_f pour afficher le resultat"

    

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ index.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      for n,rep in input_output:
        res=mon_programme(n)
        assert rep==res , "Les coordonnées obtenues sont {} au lieu de {}".format(str(res),str(rep))
      mon_programme(i)
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
