#Ne pas oublier de changer le module à importer
from Monte_carlo_plot import mon_programme,f,a,b,nombre_de_points_affichés
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np
from math import *
import sys
import io

#Je transforme f quiest en texte en fonction
f=lambda x : eval(str(f))

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

#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"



def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> open -s /project/target/ index.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      fig=plt.figure()
      #Dessin de la courbe
      l_x = np.linspace(a,b, 100)
      l_y=np.array([f(x) for x in l_x])
      plt.plot(l_x,l_y, color="blue")
      #Dessin des points calculés par mon_programme
      l_x,l_y=mon_programme(f,a,b)
      l_x,l_y=l_x[:nombre_de_points_affichés],l_y[:nombre_de_points_affichés]
      for i in range(nombre_de_points_affichés):
        if f(l_x[i])>l_y[i]:
          plt.plot(l_x[i],l_y[i],".", color="cyan")
        else:
          plt.plot(l_x[i],l_y[i], ".", color="grey")      
      fig.savefig('output.png', dpi=fig.dpi)
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
