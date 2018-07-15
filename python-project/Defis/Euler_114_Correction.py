# L'idée est de calculer par récurrence en regardant la case où s'arrete la premiere bande rouge selon la longueur de cette bande rouge

from functools import lru_cache

# La longueur de la bande
n_max=50


# On note u(n) le nombre de façons de remplir n cases.
@lru_cache(maxsize=None)
def u(n):
    if 3>n : return 1
    # La première bande rouge peut être d'une longueur allant de 3 à n suivie d'une case noire et précédée de i cases noires. On fait la somme sur toutes ces possibilités des façons de remplir les cases restantes.
    somme = 1 # Tout est noir
    for i in range(n-2): # Le nombre de cases noires avant la bande rouge
        for longueur in range(3, n-i+1): # On parcourt les longueurs du bloc rouge possibles
            somme += u(n-i-longueur-1)
    return somme
    

print(u(n_max))
