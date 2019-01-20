import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from math import *

# Constantes
m1,m2,m3,xi1,yi1,xi2,yi2,vix1,viy1,vix2,viy2,duree=10**13,10**13,2*10**13,1,0,0,1,0,20,-20,0,20
G=6.6742*10**(-11)
temps = np.linspace(0, duree,300*duree)

def donner_force(m1,x1,y1,m2,x2,y2):
    """
    donne les coordonnées de la force qu'exerce l'objet 2 sur l'objet 1
    """
    temp=G*m1*m2/((x2-x1)**2+(y2-y1)**2)**1.5 # C'est juste pour éviter deux fois le même calcul
    return (x2-x1)*temp,(y2-y1)*temp


# Equation vérifiée par les 3 objets
def eq_mouvement(mobile,temps):
    x1,y1,x2,y2,dx1,dy1,dx2,dy2=mobile
    # Comme on est dans le repère barycentrique, on peut déduire les  coordonnées de l'objet 3 :
    x3=-(m1*x1+m2*x2)/m3
    y3=-(m1*y1+m2*y2)/m3
    # Les différentes forces exercées sur 1:
    F12x,F12y=donner_force(m1,x1,y1,m2,x2,y2)
    F13x,F13y=donner_force(m1,x1,y1,m3,x3,y3)
    # Les différentes forces exercées sur 2:
    F21x,F21y=-F12x,-F12y
    F23x,F23y=donner_force(m2,x2,y2,m3,x3,y3)
    return [dx1,dy1,dx2,dy2,(F12x+F13x)/m1,(F12y+F13y)/m1,(F21x+F23x)/m2,(F21y+F23y)/m2]

X1,Y1,X2,Y2,dX1,dY1,DX2,DY2=odeint(eq_mouvement, (xi1,yi1,xi2,yi2,vix1,viy1,vix2,viy2), temps).T
X3=-(m1*X1+m2*X2)/m3
Y3=-(m1*Y1+m2*Y2)/m3
line,=plt.plot([0,0,0],[0,0,0],".")
#plt.plot(0,0,"ro")
plt.xlim(min(min(X1),min(X2),min(X3))-5,max(max(X1),max(X2),max(X3))+5)
plt.ylim(min(min(Y1),min(Y2),min(Y3))-5,max(max(Y1),max(Y2),max(Y3))+5)
#On dessine les points
for i in range(len(X1)):
    line.set_data([X1[i],X2[i],X3[i]],[Y1[i],Y2[i],Y3[i]])
    plt.pause(1/30) # Pour faire une pause entre chaque image

plt.show()
