"""
Euler 138
On se ramène à l'équation diophantienne L²=5n²+-4n+1 (où n=b/2)
Après une petite (grosse?!) prise de tête pour la résoudre, on trouve que L_n+2 = 18L_n+1 - L_n
On peut peut-être utiliser diophantine du module sympy pour la résoudre avec python
"""

from functools import lru_cache

def chercher(N):

    @lru_cache(None)
    def L(n):
        if n==1: return 17
        if n==2: return 305
        else:
            return 18*L(n-1)-L(n-2)

    return   sum([L(n) for n in range(1,N+1)])
            

print(chercher(12))
