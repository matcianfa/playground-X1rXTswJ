"""
Euler 129
Force brute
Presque décevant que ca marche si facilement sans avoir besoin de faire de maths...
"""

from math import gcd


def A(n):
    if gcd(n,10)!=1 : return -1
    else :
        k=1
        Rk=1
        while Rk!=0:
            k+=1
            Rk=(10*Rk+1)%n # On optimise le calcul de Rk sinon c'est trop long
        return k
        

def chercher(N):
    i=1000001
    a = A(i)
    while a<N:
        i+=2 # Inutile de chercher les nombres pairs
        a = A(i)
        # print(i,a)
    return i

print(chercher(1000000))
