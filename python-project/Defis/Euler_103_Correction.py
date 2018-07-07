# Plus ou moins force brute. On nous donne déjà une approximation de la solution donc on va chercher pour des valeurs autour
# Dans un premier temps on va créer des fonctions pour vérifier qu'un ensemble  est spécial. 
# Remarque : on parle d'ensemble dans l'énoncé mais comme il est ordonné, c'est une liste que nous allons utiliser

from itertools import combinations


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
    
    
# Si on applique la règle proposée, on obtient comme nombre minimum 22 et maximum 46.
# On va donc chercher dans tous les 7 uplets de nombres entre 19 et 49. Ce qui fait à peu près 2 millions de cas donc c'est raisonnable
def chercher():
    somme_min=49*7
    ens_min=[]
    for A in combinations(range(19,50),7):
        if sum(A)< somme_min and vérif1(A) and vérif2(A) :
            ens_min=A
            somme_min=sum(A)
    return "".join([str(n) for n in ens_min])
    
print(chercher())
