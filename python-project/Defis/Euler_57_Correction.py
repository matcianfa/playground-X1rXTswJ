# Faisons un petit déblayage mathématique avant. Si on note u_k = num_k/den_k la k-ième fraction.
# On a alors u_k+1=1 + 1/(1+u_k) et donc en mettant au même dénominateur on obtient 
# num_k+1 = 2*den_k+num_k 
# et den_k+1 = den_k+num_k
# D'où le programme suivant : On calcule les deux suites num_k et den_k et on compare leur nombre de chiffres

#Première méthode : avec mémoization.
#Pour gagner en temps, on va mémoizer en utilisant la fonction lru_cache directement (Voir le cours d'optimisation sur la mémoization)
from functools import lru_cache

@lru_cache(maxsize=None)
def num(k):
    if k==0 : return 1
    return 2*den(k-1)+num(k-1)
    
@lru_cache(maxsize=None)
def den(k):
    if k==0 : return 1
    return den(k-1)+num(k-1)

compteur=0    
for k in range(1001):
    if len(str(num(k)))>len(str(den(k))):
        compteur+=1
        
print(compteur)

#------------------------------------------------------------------------------------------------------
# Deuxième méthode : La même mais sans utiliser de mémoization

compteur=0
num=1
den=1
for k in range(1001):
    if len(str(num))>len(str(den)):
        compteur+=1
    num,den=2*den+num,den+num
    
print(compteur)
