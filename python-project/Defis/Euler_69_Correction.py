# Le problème revient à chercher phi(n)/n minimum or phi(n)/n vaut le produit des (1-1/p) pour p premier divise n. D'où la méthode de recherche ci dessous.

from functools import lru_cache

# Fonction qui calcule phi(n)/n directement. On la mémoize car il y a beaucoup de calculs identiques. En effet phi(mn)= phi(m)phi(n) lorsque m et n premiers entre eux. Or ici les calculs sont fait nombres premiers par nombres premiers donc on peut l'utiliser.
@lru_cache(maxsize=None)
def calcul(n):
    if n==1 : return 1
    #On teste 2 à part pour gagner en temps après
    if n%2 ==0 : 
        n//=2
        while n%2== 0 :
            n//=2
        return 1/2*calcul(n)
    else :
        p=3
        rac=int(n**0.5)+1
        while n%p != 0 and p<= rac:
            p+=2
        if p> rac : return (1-1/n) # Cas où n est premier
        else: #cas ou on a trouvé p qui divise n
            while n%p==0 :
                n//=p
            return (1-1/p)*calcul(n)
            
val_min=1
n_min=0
for n in range(2,1000001):
    temp = calcul(n)
    if temp <val_min:
        val_min=temp
        n_min=n
        
print(n_min)
