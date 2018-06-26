# On va utiliser les résultats classiques sur les fractions continues qu'on peut trouver ici : https://fr.wikipedia.org/wiki/Fraction_continue#R%C3%A9duites_d'une_fraction_continue

# Définissons nos fonctions a, h et k (je garde les notations de wikipédia)
# On mémoize bien sûr
from functools import lru_cache

@lru_cache(maxsize=None)
def a(n):
    if n==0 : return 2
    if (n+1)%3==0 : return (2*(n+1)//3) # c'est juste une réécriture de a_(3k-1)=2k
    return 1
    
@lru_cache(maxsize=None)
def h(n):
    if n==-2 : return 0
    if n==-1 : return 1
    return a(n)*h(n-1)+ h(n-2)
    
@lru_cache(maxsize=None)
def k(n):
    if n==-2 : return 1
    if n==-1 : return 0
    return a(n)*k(n-1)+ k(n-2)

#Faisons maintenant la somme des chiffres du 100e numérateur (donc n=99)
print(sum([int(chiffre) for chiffre in str(h(99))]))
