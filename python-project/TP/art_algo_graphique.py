from math import *   
import matplotlib.pyplot as plt

# Copier-coller ci dessous les fonctions u(n), x(n) et y(n) précédentes




# N représente le nombre de points tracés
N=100000
plt.axis('equal') # pour que les axes aient les mêmes unités
plt.plot(x(N),y(N),linewidth=1)
plt.show()
