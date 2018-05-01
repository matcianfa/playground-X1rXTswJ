# L'idée va être ici de regarder toutes les permutations de 123456789 et les couper en 3. Le produit des 2 premiers termes doit être égal au troisième.
# Exemple pour la permutation 391867254, on teste si 3*9=1867254 puis 3*91=867254...
# On utilise l'itérateur permutations du package itertools mais on aurait pu créer une fonction pour cela
from itertools import permutations

reponse = set([]) # On utilise un ensemble pour éviter les doublons

for perm in permutations("123456789"):
    perm="".join(perm) #On transforme le t-uplet donné par permutations en une chaine de chiffres d'affilée
    for indice_mult in range(3,5): # pour gagner en temps, on peut utiliser la symétrie du produit et donc ne chercher que pour les nombres de 3 ou 4 chiffres pour le premier
        multiplicande=int(perm[:indice_mult])
        for indice_egal in range(indice_mult+1,7):
            multiplicateur= int(perm[indice_mult:indice_egal])
            produit=int(perm[indice_egal:])
            if multiplicande*multiplicateur==produit:
                reponse.add(produit)

print(sum(reponse))
