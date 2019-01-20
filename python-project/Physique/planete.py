import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

temps = np.linspace(0, 100,10000)

# On considère un force en 1/r² avec des conditions initiales non réalistes
def eq_mouvement(mobile,temps):
    x,y,dx,dy=mobile
    return [dx,dy,-x/(x**2+y**2)**1.5,-y/(x**2+y**2)**1.5]

X,Y,dX,dY=odeint(eq_mouvement, (1,0,0,0.5), temps).T
plt.plot(X,Y)
plt.grid()
plt.show()
