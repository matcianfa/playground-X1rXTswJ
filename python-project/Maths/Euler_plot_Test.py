#Ne pas oublier de changer le module à importer
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import io
import numpy as np
from math import *
from Euler_plot import mon_programme,pas,n

input_output=[\
((1,3),[1, 2, 4, 8]),\
((0.1,10),[1, 1.1, 1.2100000000000002, 1.3310000000000004, 1.4641000000000006, 1.6105100000000008, 1.771561000000001, 1.9487171000000014, 2.1435888100000016, 2.357947691000002, 2.5937424601000023]),\
((-0.1,10),[1, 0.9, 0.81, 0.7290000000000001, 0.6561000000000001, 0.5904900000000002, 0.5314410000000002, 0.47829690000000014, 0.43046721000000016, 0.38742048900000015, 0.34867844010000015] )\
]

#message d'aide si besoin
help=""
    
#pour afficher les axes
def repere(ax):
    xmin, xmax = ax.get_xlim()
    dx = xmax - xmin
    ax.annotate('', (xmax-0.005*dx, 0), xytext=(xmin, 0),
                arrowprops=dict(arrowstyle="->"))
    ymin, ymax = ax.get_ylim()
    dy = ymax - ymin
    ax.annotate('', (0, ymax-0.005*dy), xytext=(0, ymin),
arrowprops=dict(arrowstyle="->"))

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ index_grossissant.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      #On vérifie quelques valeurs
      for inp,rep in input_output:
        liste_y=mon_programme(*inp)
        assert all([abs(y-y_r)<0.000001 for y,y_r in zip(liste_y,rep)]), "Pour pas= {} et n= {}, vous obtenez {} au lieu de {}".format(str(inp[0]), str(inp[1]),str(liste_y),str(rep))
      #On trace la courbe
      fig=plt.figure()
      ax = plt.subplot(111)
      #Dessin de la courbe exp
      l_x = np.linspace(pas_negatif*n,pas*n, 100)
      l_y=np.array([exp(x) for x in l_x])
      plt.plot(l_x,l_y, color="red")
      #dessins des segments de la méthode d'Euler
      mon_programme(pas,n)
      xmin,xmax=plt.xlim()
      plt.xlim(xmin-0.1*(xmax-xmin),xmax+0.1*(xmax-xmin))
      ymin,ymax=plt.ylim()
      plt.ylim(min(0,ymin)-0.1*(ymax-ymin),ymax+0.1*(ymax-ymin)) 
      repere(ax)
      fig.savefig('output.png', dpi=fig.dpi)
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
