#On va avoir besoin de faire des appels recursifs plus long que la limite donc il faut la modifier
import sys
sys.setrecursionlimit(2000)

# Il suffit de travailler modulo 10**10
N=10**10

# Recréons une fonction recursive puissance n**p qui calcule modulo 10**10
def puissance(n,p) : 
    if p==0 : return 1
    if p==1 : return n%N
    return (n*puissance(n,p-1))%N
    
# Calculons cette somme
somme = 0
for n in range(1,1001):
    somme = (somme + puissance(n,n))%N
    
print(somme)
