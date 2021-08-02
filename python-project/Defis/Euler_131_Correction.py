"""
Euler 131
On veut n^3+n^2p=m^3 donc n^2(n+p)=m^3.
En séparant les cas n multiples de p et n premier avec p et en utilisant l'unicité des décompoositions en facteurs premiers,
on déduit que n est un cube. donc n = a^3. D'où n+p = (m/a^2)^3 donc p =  (m/a^2)^3-a^3 .
Or, si on pose b=m/a^2, p=b^3-a^3 = (b-a)(a^2+ab+b^2) qui ne peut être un nombre premier que si b-a=1.
Donc p doit être un nombre premier de la forme (a+1)^3-a^3.
Inversement si on pose m = (a+1)a^2 et n = a^3, on a bien une solution.
"""

from math import gcd
from sympy import isprime

        

def chercher(N):
    a=0
    p=1
    compteur=0
    while p<=N:
        if isprime(p):
            compteur += 1
            print(p)
        a+=1
        p=(a+1)**3-a**3
    return compteur
            

print(chercher(1000000))
