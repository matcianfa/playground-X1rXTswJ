# On va simplement réutiliser les idées utilisées pour le problème 114 et 115

from functools import lru_cache

# La longueur de la bande
n_max=50



# On note u(k,n) le nombre de façons de remplir n cases avec des bandes de longueur k exactement.
@lru_cache(maxsize=None)
def u(k,n):
    if k>n : return 1
    # La première bande colorée est précédée de i cases noires. On fait la somme sur toutes ces possibilités des façons de remplir les cases restantes.
    somme = 1 # Tout est noir
    for i in range(n-k+1): # Le nombre de cases noires avant la bande rouge
        somme += u(k,n-i-k)
    return somme
    

# Fonction qui cherche
def chercher():
    somme=-3 # On retire déjà les bandes toutes noires qu sont comptées en trop
    for k in range(2,5):
        somme+= u(k,n_max)
    return somme
        
    
print(chercher())
