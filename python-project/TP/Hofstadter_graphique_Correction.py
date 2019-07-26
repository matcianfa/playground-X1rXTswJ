import matplotlib.pyplot as plt

# ---------- Les paramètres :
# On calcule les termes de Q de 1 jusqu'à N
N = 10000
# nb_termes correspond au nombre de terme qu'on veut afficher : de N-nb_termes+1 à N
nb_termes = 100

# Copier coller la fonction Q ci dessous
def Q(n):
    liste = [0,1,1] # On met 0 en indice 0 juste pour décaler pour que les indices soient corrects ( pour que Q(1)=liste[1] ...)
    for i in range(3,n+1):
        liste.append(liste[i-liste[i-1]]+liste[i-liste[i-2]])
    return liste[1:]

# Compléter la valeur de Y pour n'afficher que les termes de la suite de N-nb_termes+1 à N
X = list(range(nb_termes))
Y = Q(N)[-nb_termes:]

plt.plot(X,Y,"-",linewidth=1)
plt.show()
