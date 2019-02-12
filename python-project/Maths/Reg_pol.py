import matplotlib.pyplot as plt
import numpy as np

# Les listes des abscisses et ordonnées des points mesurés
x=np.array([111, 131, 152, 172, 192, 213, 234, 255, 276, 297, 317, 338, 359, 380, 401, 423, 442, 462])
y=np.array([339, 362, 384, 398, 409, 411, 409, 404, 394, 374, 350, 325, 290, 250, 212, 162, 108, 51])

# On affiche les points mesurés
plt.plot(x,y,"o")

# polyfit donne les coefficients du polynome de regression
a,b,c=np.polyfit(x,y,2)

# On affiche la parabole de régression
plt.plot(x,a*x**2+b*x+c)
plt.show()
