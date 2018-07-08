# On réutilise les fonctions du problème 103. Rien de bien original : Pour chaque ensemble, on reste s'il est spécial et on fait la somme de ses éléments...
# Dans un premier temps on va créer des fonctions pour vérifier qu'un ensemble  est spécial. 
# Remarque : on parle d'ensemble dans l'énoncé mais comme il est ordonné, c'est une liste que nous allons utiliser

# Liste des ensembles (donnés sous forme de listes) à tester
liste= # A copier coller

from itertools import combinations

#On réordonne les ensembles
liste=[sorted(ens) for ens in liste]

# fonction pour vérifier la premier propriété
# Vue la propriété 2, il suffit de le vérifier pour les ensembles de même cardinal
# Astucieusement, on calcule toutes sommes pour k éléments qu'on met dans un ensemble et on vérifie à la fin qu'il y en a le nombre attendu (C'est à dire combinaison(n,k))
def vérif1(A):
    for k in range(1,len(A)//2+1): # le cardinal des deux sous ensembles à comparer
        ens=set([])
        for combi in combinations(A,k): # On prend tous les ensembles de k éléments dans A
            temp = sum(combi)
            if temp in ens : return False
            ens.add(temp)
    return True
            
            
# Fonction qui vérifie la seconde propriété.
# Comme A est ordonnée, pour vérifier la deuxième propriété, il suffit de la vérifier pour les k+1 premiers par rapport aux k derniers (car pour des raisons de croissances, les autres inégalités seront vérifiées. pour k allant de 1 à (len(A)-1)//2            
def vérif2(A):
    for k in range(1,(len(A)-1)//2+1):
        if sum(A[:k+1])<=sum(A[-k:]) : return False
    return True
    
    
# Fonction qui cherche la solution
def chercher():
    somme=0
    for ens in liste:
        if vérif1(ens) and vérif2(ens) :
            somme+= sum(ens)
    return somme
    
print(chercher())
