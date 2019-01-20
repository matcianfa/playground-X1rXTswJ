import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from math import *


temps = np.linspace(0, 50,1000)
g=9.81

# On ne considere que la pesanteur
def eq_mouvement(mobile,temps):
    x,y,dx,dy=mobile
    return [dx,dy,0,-g]

X,Y,dX,dY=odeint(eq_mouvement, (0, 30,10,10), temps).T
# On ne garde que les valeurs de Y positives
indice=0
for y in Y :
    if y<0:
        break
    indice+=1

plt.plot(X[:indice+1],Y[:indice+1], label="Sans frottement")

# Si on considere des frottements -Cv*vec(v)
C=0.001
def eq_mouvement_frottement(mobile,temps):
    x,y,dx,dy=mobile
    v=sqrt(dx**2+dy**2)
    return [dx,dy,-C*v*dx,-g-C*v*dy]

Xf,Yf,dXf,dYf=odeint(eq_mouvement_frottement, (0, 30,10,10), temps).T
# On ne garde que les valeurs de Yf positives
indice=0
for y in Yf :
    if y<0:
        break
    indice+=1

plt.plot(Xf[:indice+1],Yf[:indice+1],label="Avec frottement")
plt.legend()
plt.show()
