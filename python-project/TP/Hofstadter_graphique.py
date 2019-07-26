import matplotlib.pyplot as plt

# ---------- Les paramètres :
# On calcule les termes de Q de 1 jusqu'à N
N = 10000
# nb_termes correspond au nombre de terme qu'on veut afficher : de N-nb_termes+1 à N
nb_termes = 50

# Copier coller la fonction Q ci dessous




# Compléter la valeur de Y pour n'afficher que les termes de la suite de N-nb_termes+1 à N
X = list(range(nb_termes))
Y = ...

plt.plot(X,Y,"-",linewidth=1)
plt.show()
