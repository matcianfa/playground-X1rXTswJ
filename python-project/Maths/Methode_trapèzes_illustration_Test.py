#Ne pas oublier de changer le module à importer
from Methode_trapèzes_illustration import f,a,b,n
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import io
import numpy as np
from math import *

#Je transforme f quiest en texte en fonction
f2=lambda x : eval(str(f))

#message d'aide si besoin
help="N'oublie pas d'utiliser print pour afficher le resultat"

#Calcul de l'aire par la méthode des rectangles
def trapezes(f,a,b,n):
    pas=(b-a)/n
    x=a+pas
    somme=f(a)+f(b)
    for _ in range(n-1):
        somme+=f(x)/2
        x+=pas
    return  somme*pas
    
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
    print("TECHIO> open -s /project/target/ index.html")
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

def test():
    try:
      fig=plt.figure()
      ax = plt.subplot(111)
      #Dessin de la courbe
      l_x = np.linspace(a,b, 500)
      l_y=np.array([f2(x) for x in l_x])
      plt.plot(l_x,l_y, color="blue")
      #Dessin des rectangles
      x=a
      pas = (b-a)/n
      for _ in range(n):
          ax.add_artist(matplotlib.patches.Polygon(list(zip([x,x+pas,x+pas,x],[0,0,f2(x+pas),f2(x)])),closed=True, facecolor = 'cyan', edgecolor='black'))
          x+=pas
      xmin,xmax=plt.xlim()
      plt.xlim(xmin-0.2,xmax+0.2)
      ymin,ymax=plt.ylim()
      plt.ylim(min(0,ymin)-0.2,ymax+0.3) 
      repere(ax)
      fig.savefig('output.png', dpi=fig.dpi)
      #J'affiche la valeur de l'approximation de l'aire
      send_msg("Calcul de l'aire", "La valeur approchée de l'aire calculée avec ces rectangles est {}".format(trapezes(f2,a,b,n)))
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
