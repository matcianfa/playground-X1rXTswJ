# On va simplement réutiliser les idées utilisées pour le problème 114, 115 et 116. On remarque juste que les couleurs ne servent à rien ici donc c'est comme le probleme 115 mais avec un longueur max des blocs

from functools import lru_cache

# La longueur de la bande
n_max=50
# Tailles max des blocs de couleur
longueur_min=2
longueur_max=4


# On note u(n) le nombre de façons de remplir n cases.
@lru_cache(maxsize=None)
def u(n):
    if longueur_min>n : return 1
    # La première bande rouge peut être d'une longueur allant de 2 à 4 suivie d'une case noire précédée de i cases noires. On fait la somme sur toutes ces possibilités des façons de remplir les cases restantes.
    somme = 1 # Tout est noir
    for i in range(n-longueur_min+1): # Le nombre de cases noires avant la bande rouge
        for longueur in range(longueur_min, min(longueur_max+1,n-i+1)): # On parcourt les longueurs du bloc rouge possibles
            somme += u(n-i-longueur)
    return somme
    
print(u(n_max))
