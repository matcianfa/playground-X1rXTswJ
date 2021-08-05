"""
Euler 133
Même code que pour le 132
On remarque que R(a*b)=R(a)*(10^ab-1)/(10^a-1). Donc tout diviseur de R(a) divivise R(ab).
Du coup il suffit de chercher les diviseurs d'un gros nombre de la forme 10^n pour avoir ceux de tous les précédents. 
Il suffit de chercher quand la somme des diviseurs inférieurs à 100 000 ne change plus (par exemple pour R(10^100))
"""

from sympy.ntheory import nextprime
  

def chercher(N,k):
    p=1
    somme = 0
    while p<N :
        p=nextprime(p)
        Rk= pow(10,k,9*p)
        if Rk!=1:
            somme+=p
    return somme-p # Car le dernier dépasse N
            

print(chercher(100000,10**100))
