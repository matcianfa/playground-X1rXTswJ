import matplotlib.pyplot as plt
import numpy as np

# La fonction f à tracer
def f(x) :
    return x**4 - 2
    
# La valeur initiale
x0 = 3

# Intervalle sur lequel on observe la fonction
x_min = 1
x_max = 3.1

# On trace l'axe des abscisses
plt.plot([x_min,x_max],[0,0],"k",linewidth=1)

# Ecrire ci dessous votre script pour qu'il affiche la fonction et les premières tangentes de la méthode de Newton

def deriver(f,a,h):
    return (f(a+0.5*h)-f(a-0.5*h))/h

# Première étape : afficher la fonction 
X = np.linspace(x_min,x_max,100)
Y = f(X)
plt.plot(X,Y)

# Deuxième étape : On trace les tangentes
for i in range(5) :
    x1 = x0 - f(x0)/deriver(f,x0,0.000001)
    plt.plot([x0,x1],[f(x0),0])
    x0=x1

plt.show()


