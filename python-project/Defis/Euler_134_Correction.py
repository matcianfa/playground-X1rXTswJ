"""
Euler 134
Force brute
Un peu long. On peut peut-etre gagner en vitesse en programmant la recherche de l'inverse modulo p2 (en cherchant le u et v du théorème de Bezout pour 10^longueur_p1 et p2)
"""

from sympy.ntheory import nextprime
from math import log10
  

def chercher(N):
    p1=5
    somme = 0
    while p1<=N :
        p2=nextprime(p1)
        dix_puissance_longueur_p1 = pow(10,int(log10(p1))+1)
        S = p1
        for k in range(1,p2+1):
            S += dix_puissance_longueur_p1
            if S%p2 == 0:
                print("\r",p1,S,end="")
                somme+=S
                break
        else:
            print("Pas trouvé !")
        p1=p2
    return somme
        
            

print("\n",chercher(1000000))
