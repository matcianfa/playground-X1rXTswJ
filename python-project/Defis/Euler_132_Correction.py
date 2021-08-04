"""
Euler 132
Plus ou moins brute force
On utilise le fait qu'un repunit est en fait la somme d'une suite géométrique de raison 10 donc vaut (10**k-1)//9.
Il est donc divisible par p ssi 10**k==1 mod 9p.
On utilise donc la fonction pow(a,b,c) qui calcule de manière optimisée a**b mod c
"""

from sympy.ntheory import nextprime

def R(k):
    n=0
    for i in range(k):
        n=10*n+1
    return n     

def chercher(k,nombre_diviseurs):
    compteur = 0
    p=2
    somme = 0
    while compteur<nombre_diviseurs :
        p=nextprime(p)
        Rk= pow(10,k,9*p)
        if Rk==1:
            compteur+=1
            print(p)
            somme+=p
    return somme
            

print(chercher(10**9,40))
