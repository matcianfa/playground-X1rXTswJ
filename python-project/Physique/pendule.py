import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from math import *

longueur=1
angle= 60
vitesse=0
duree=10

fps=30 # 30 images par secondes en general
dt=1/fps # ecart de temps entre chaque image
angle=angle_s=radians(angle) # conversion en radians
vitesse=vitesse_s=radians(vitesse)
Dt=np.array([0,dt]) # l'intervalle de temps entre 2 mises à  jour

#constantes physiques
g=9.81
omega2=g/longueur
omega=(omega2)**0.5
periode=2*np.pi/omega

# equation differentielle generale (avec sinus)
def eq_pendule(Theta,t):
    theta,dtheta=Theta
    return [dtheta,-omega2*np.sin(theta)]

# equation differentielle simplifiee (sin(theta)= theta)
def eq_pendule_simp(Theta,t):
    theta,dtheta=Theta
    return [dtheta,-omega2*theta]

#initialisation du graphique
t=0
line,=plt.plot([],[],"o-",label="Equation generale")
line_s,=plt.plot([],[],"o-",label="Equation simplifiee")
plt.xlim(-1.1*longueur,1.1*longueur)
plt.ylim(-1.1*longueur,1.1*longueur) # On fixe notre axe y
plt.legend()
plt.gca().set_aspect("equal")

# Toutes les dt sec, on calcule les nouvelles coordonnees à  partir des anciennes et on l'affiche
while t<duree:

    #On resout l'equadiff entre t et t+dt
    Theta,dTheta=odeint(eq_pendule, (angle,vitesse), Dt).T
    Theta_s,dTheta_s=odeint(eq_pendule_simp, (angle_s,vitesse_s), Dt).T
    angle,vitesse=Theta[1],dTheta[1]
    angle_s,vitesse_s=Theta_s[1],dTheta_s[1]
    line.set_data([0,longueur*sin(angle)],[0,-longueur*cos(angle)])
    line_s.set_data([0,longueur*sin(angle_s)],[0,-longueur*cos(angle_s)])
    plt.pause(dt)
    t+=dt

plt.show()
