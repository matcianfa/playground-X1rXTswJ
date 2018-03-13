#Ne pas oublier de changer le module à importer
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import sys
import io
import numpy as np
from math import *
from Tracer_une_courbe import mon_programme

input_output=[\
((lambda x:x**2,0,4,5),"x²"),\
((lambda x:x**2,0,4,100),"x²"),\
((lambda x:sqrt(1-x**2),-1,1,10),"racine(1-x²)"),\
((lambda x:sqrt(1-x**2),-1,1,100),"racine(1-x²)"),\
((lambda x:exp(-x**2/2)/sqrt(2*pi),-3,3,10),"exp(-x²/2)"),\
((lambda x:exp(-x**2/2)/sqrt(2*pi),-3,3,100),"exp(-x²/2)"),\
((lambda x:x*(1-x)*(sin(200*x*(1-x)))**2,0,1,20),"x(1-x)sin²(200*x*(1-x))"),\
((lambda x:x*(1-x)*(sin(200*x*(1-x)))**2,0,1,500),"x(1-x)sin²(200*x*(1-x))"),\
((lambda x:(cos(20*pi*x)),0,10,100),"cos(20*pi*x)"),\
((lambda x:(cos(20*pi*x)),0,10,1000),"cos(20*pi*x)"),\
]

#message d'aide si besoin
help="N'oublie pas d'utiliser return pour afficher le resultat"

    
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
      compteur=0
      fig=plt.figure()
      for (f,a,b,n),txt in input_output:
          compteur+=1
          ax = plt.subplot(5,2,compteur)
          #Dessin de la courbe
          rep_l_x = list(np.linspace(a,b, n+1))
          rep_l_y=[f(x) for x in rep_l_x]
          l_x,l_y=mon_programme(f,a,b,n)
          xmin,xmax=plt.xlim()
          plt.xlim(xmin-0.1*(xmax-xmin),xmax+0.1*(xmax-xmin))
          ymin,ymax=plt.ylim()
          plt.ylim(min(0,ymin)-0.1*(ymax-ymin),ymax+0.1*(ymax-ymin)) 
          repere(ax)
          if compteur%2==1 : plt.ylabel(txt)
          assert all(round(x-r,5)==0.0 for x,r in zip(l_x,rep_l_x)) and all(round(y-r,5)==0.0 for y,r in zip(l_y,rep_l_y)) , "En testant les valeurs f(x)={}, a={}, b={} et n={} les listes obtenues sont {} et {} au lieu de {} et {}".format(str(txt),str(a),str(b),str(n),str(l_x),str(l_y),str(rep_l_x),str(rep_l_y))
          send_msg("Tests validés","En testant les valeurs f(x)={}, a={}, b={} et n={}, Vous avez obtenu les bonnes listes de valeurs.".format(str(txt),str(a),str(b),str(n)))
      fig.savefig('output.png', dpi=fig.dpi)
      success()
    except AssertionError as e:
      fail()
      send_msg("Oops! ", e)
      if help:
        send_msg("Aide 💡", help)


if __name__ == "__main__": test()
