# L'idée est la suivante : 
# On fixe le nombre de B de 8 à 15.
# On va regarder pour toutes les permutations avec ce nombre de B fixé. On remplace B par 1 et R par son rang et on les multiplie puis on divise par 16! pour obtenir la probabilité d'avoir cette permutation.
# Une fois obtenue la probabilité totale, On calcule la valeur du prix pour que l'esperance soit la plus proche de zéro.

from itertools import combinations
from functools import lru_cache

# nombres de tours
n_tours = 15

# La fonction factorielle
@lru_cache(maxsize=None)
def factorielle(n):
    if n==0 or n==1 : return 1
    return n*factorielle(n-1)

# Fonction qui calcule la probabilité d'une combinaison donnée (pour éviter les calculs avec les flottants, on divisera par factorielle 16 à la toute fin)
# comb contient uniquement les indices des rouges
def calcul_proba(comb):
    proba = 1
    for indice in comb :
        proba *= indice+1
    return proba
    
#  Fonction qui calcule la proba totale de gagner
def calcul_proba_gagner():
    proba = 0
    for n_rouges in range((n_tours-1)//2 +1): # n_rouges est le nombre de disques rouges
        for comb in combinations(list(range(n_tours)),n_rouges):
            proba+= calcul_proba(comb)
    proba/= factorielle(n_tours+1)
    return proba
    
# On cherche le résultat en resolvant Esperance = 0 et on trouve que la récompense doit être inférieur à  (1-p)/p + 1
def chercher():
    p = calcul_proba_gagner()
    return int((1-p)/p)+1
    
print(chercher())
