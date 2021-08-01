"""
Euler 130
Force brute
"""

from math import gcd
from sympy import isprime


def A(n):
        k=1
        Rk=1
        while Rk!=0:
            k+=1
            Rk=(10*Rk+1)%n # On optimise le calcul de Rk sinon c'est trop long
        return k
        

def chercher(N):
    i=89
    compteur = 0
    somme = 0
    while compteur<N:
        i+=2 # Inutile de chercher les nombres pairs
        if gcd(i,10)==1 and not isprime(i) and (i-1)%A(i)==0:
            compteur+=1
            somme+=i
            print("Trouvé",i)
    return somme

print(chercher(25))
