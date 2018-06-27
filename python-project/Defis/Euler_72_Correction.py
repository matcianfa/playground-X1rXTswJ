# La force brute serait trop longue
# On remarque donc que pour chaque d, il y a phi(d) fractions irréductibles de dénominateurs d ou phi(d) est la fonction d'Euler (vue dans les problèmes précédents.
# D'où le programme suivant : 

from functools import lru_cache

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n==2 : return True
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True
    
# liste des nombres premiers inférieurs à racine carrée de 10^6
premiers = [ p for p in range(2,10**3+1) if est_premier(p)]

# Fonction qui calcule phi(n). On la mémoize car il y a beaucoup de calculs identiques. En effet phi(mn)= phi(m)phi(n) lorsque m et n premiers entre eux. Or ici les calculs sont fait nombres premiers par nombres premiers donc on peut l'utiliser.
@lru_cache(maxsize=None)
def phi(n):
    if n==1 : return 1
    for p in premiers :
        rac=int(n**0.5)+1
        if p> rac : return n-1 # Cas où n est premier
        elif n%p==0: #cas ou on a trouvé p qui divise n
            n//=p
            temp=p-1
            while n%p==0 :
                n//=p
                temp*=p
            return temp*phi(n)
    return n-1 # Cas ou on a épuisé la liste des nombres premiers


somme=0
for d in range(2,1000001):
    somme+=phi(d)
    
print(somme)
