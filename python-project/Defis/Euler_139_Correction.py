"""
Euler 139
On génère les triplets pythagoriciens primitifs avec le classique a= p²-q², b= 2pq et c= p²+q² où p et q premiers entre eux et de parité différente
si on multiplie par k un triplet qui marche alors il marchera aussi (c'est simplement une homothétie de la figure) donc il y aura 100000000/(a+b+c) triplets
qui marchent pour chaque triplet primitif (a,b,c)

Remarque a posteriori : Les triplets primitifs vérifient a = b +/- 1
"""

from math import gcd

def chercher(N):

    compteur = 0
    for p in range(2,int(N**0.5)+1):
        for q in range(1,p):
            if (p+q)%2==1 and gcd(p,q)==1:
                a = p*p-q*q
                b=2*p*q
                c=p*p+q*q
                
                if c%abs(a-b) == 0:
                    print("Triplet primitif valide :",a,b,c)
                    compteur += N//(a+b+c)
    return compteur
            

print(chercher(100000000))
