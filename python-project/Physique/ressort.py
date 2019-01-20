import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# On fixe nos constantes
longueur_vide= 0.40
k=20
longueur_initiale=0.5
duree=10 # durée de l'animation

fps=30 # 30 images par secondes en général
dt=1/fps # ecart de temps entre chaque image
g=9.81
y0=-longueur_initiale
v0=0
Dt=np.array([0,dt]) # l'intervalle de temps entre 2 mises à  jour

def eq_mouvement(mobile,temps):
    y,dy=mobile
    return [dy,-g+k*(-y-longueur_vide)]

#initialisation du graphique
t=0
line,=plt.plot([],[],"o-")
plt.ylim(-2,0.1) # On fixe notre axe y
texte = plt.text(-0.05, -0.01, '')

# Toutes les dt sec, on calcule les nouvelles coordonnees a  partir des anciennes et on l'affiche
while t<duree:

    #On part d'une longueur_0 et d'une vitesse nulle
    L,DL=odeint(eq_mouvement, (y0,v0), Dt).T
    y0=L[1]
    v0=DL[1]
    line.set_data([0,0],[0,y0])
    texte.set_text("temps = {:0.3f} s".format(t))
    plt.pause(dt)
    t+=dt

plt.show()
