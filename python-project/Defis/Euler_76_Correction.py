# On pourrait utiliser la formule de Mac Mahon mais ici on va utiliser une formule de récurrence plus naturelle :
# Si on note p(n,k) le nombre de decomposition de n en somme de k entiers (qu'on suppose ordonnée comme dans l'exemple pour éviter les doublons).
# 2 possibilités : - Soit le dernier est un 1 auquel cas il y a p(n-1,k-1) décompositions qui correspondent à ce cas
# - Soit tous les nombres de la décomposition sont plus grands que 2 auquel cas en soustrayant 1 à tout le monde on obtient une décomposition de n-k en k termes. Il y a donc p(n-k,k) décompositions de ce type
# Au final on a donc p(n,k)=p(n-1,k-1)+p(n-k,k)


from functools import lru_cache

# Fonction qui calcule le nombre de décompositions. On mémoize bien sur
@lru_cache(maxsize=None)
def p(n,k):
    if n==k or k==1 : return 1 # Les cas évidents
    if n<k : return 0
    return p(n-1,k-1)+p(n-k,k)
    
print(sum([p(100,k) for k in range(2,101)])) # On part de 2 car l'énoncé veut des vraies sommes (donc 2 termes)
