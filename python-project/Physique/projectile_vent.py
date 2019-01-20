import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint
from math import *
from mpl_toolkits import mplot3d

axes=plt.axes(projection='3d')
temps = np.linspace(0, 20,5000)
g=9.81

def eq_mouvement(mobile,temps):
    x,y,z,dx,dy,dz=mobile
    return [dx,dy,dz,sin(2*np.pi*temps),0,-g]

X,Y,Z,dX,dY,dZ=odeint(eq_mouvement, (0,0, 30,0,10,10), temps).T
# On ne garde que les valeurs de Y positives
indice=0
for z in Z :
    if z<0:
        break
    indice+=1

axes.plot3D(X[:indice+1],Y[:indice+1],Z[:indice+1])
plt.show()
