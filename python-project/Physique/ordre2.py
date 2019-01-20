import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

a=-1
temps = np.linspace(0, 50,1000)

# L'équation différentielle sous forme de fonction
def equation(Y,temps):
    # On décompose notre Y en (y,dy) :
    (y,dy)=Y
    # On renvoie ce que vaut Y' :
    return [dy,a*y]

# Pour que odeint renvoit séparément les valeurs de Y et de Y', il faut rajouter .T à la fin
Y,dY=odeint(equation, [1,0], temps).T
plt.plot(temps,Y)
plt.show()
