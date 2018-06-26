# Méthode force brute mais beaucoup trop longue. Je suis intéressé si vous trouvez une solution plus rapide basée sur des arguments mathématiques.
# Rien de particulier dans la méthode : on calcul phi(n) et on compare à n pour voir si c'est une permutation

from functools import lru_cache

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n==2 : return True
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True
    
# liste des nombres premiers inférieurs à racine carrée de 10^7
premiers = [ p for p in range(2,int(10**3.5) +1) if est_premier(p)]

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

# fonction qui remet dans l'ordre croissant les chiffres d'un nombre pour pouvoir comparer si ce sont des permutations ou non
def ranger(n):
    return sorted(str(n))
    
n_min=0
val_min=10**7
for n in range(2,10**7+1):
    phi_n=phi(n)
    if ranger(phi_n)==ranger(n) :
        temp = n/phi_n
        if temp<val_min :
            val_min=temp
            n_min=n
            
print(n_min)
