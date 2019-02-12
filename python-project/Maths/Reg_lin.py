import matplotlib.pyplot as plt
import numpy as np

# Les listes des abscisses et ordonnées :
x=np.array([ 5.13 ,  5.7,  5.48,  5.7,  5.66, 5.84,  5.5,  5.69,  5.44,  5.84, 5.82,  5.88,  5.61,  5.65,  5.21, 5.37,  5.46,  5.33,  5.15,  5.74])
y=np.array([ 19.47,  21.67,  20.98,  21.46 , 21.6,  22.29,  20.84,  21.46, 20.8,  21.56,  22.02 ,  22.54, 21.2,  21.39,  20.49,  20.46, 20.72,  20.07 ,  20.24,  21.6])

# On dessine le nuage de points :
plt.plot(x,y,"o")

# polyfit donne les coefficients du polynome de regression :
a,b=np.polyfit(x,y,1)

# On dessine la droite de regression :
plt.plot(x,a*x+b)
plt.show()
