"""
Euler 137
Déjà on montre que cela revient à chercher à résoudre A(x)=x/(1-x-x²)=n, n entier.
Donc il faut que Delta = 1+2n+5n² soit un carré parfait.
Si on cherche x=p/q on trouve 
A(1/2) = 2
A(3/5) = 15 = 3x5
A(8/13) = 104 = 8x13
A(21/34) = 714 = 21x34
A(55/89) = 4895 = 55x89
A(144/233) = 33552 = 144x233

du coup on conjecture que 
A(F(2n)/F(2n+1))=F(2n)*F(2n+1)

D'où le calcul rapide ci dessous
"""

from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n==1 or n==2:
        return 1
    else : 
        return fib(n-1)+fib(n-2)
  

def chercher(N):
    return fib(2*N)*fib(2*N+1)
        
            

print(chercher(15))
