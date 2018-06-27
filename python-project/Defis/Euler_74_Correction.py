# Rien d'original dans l'idée : on fait ce qui est demandé étape par étape

from functools import lru_cache

# Fonction factorielle (avec mémoization):
@lru_cache(maxsize=None)
def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)
        
# Fonction qui calcule la somme des factorielles des chiffres de n. On mémoize car il y a beaucoup de nombres qui reviennent souvent.
@lru_cache(maxsize=None)
def somme_fact(n):
    return sum([factorielle(int(chiffre)) for chiffre in str(n)])

# Dans une fonction pour aller plus vite
def chercher():
    compteur=0
    for n in range(1,1000001):
        ens=set([]) # On mémorise les nombres obtenus au fur et à mesure
        s=n
        while s not in ens:
            ens.add(s)
            s=somme_fact(s)
        if len(ens)==60:
            compteur+=1
    return compteur    
    
print(chercher())
        
# On pourrait gagner encore en temps en mémorisant pour chaque nombre la longueur de la chaine qui suit.
