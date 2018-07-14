# Vu le nombre : 10^100, hors de question de tenter la force brute donc on va reflechir plutôt ...
'''
 Si on note u(n,c) le nombre de nombres de n chiffres qui sont croissants et qui finissent par c, alors on remarque que u(n+1,c)=u(n,0)+ u(n,1)+...+u(n,c) en commençant par u(1,0)=0 et u(1,c)=1.
 De même pour les suites décroissantes : v(n+1,c)=v(n,c)+v(n,c+1)+...+ v(n,9) et v(1,0)=0 et v(1,c)=1
 On n'a plus qu'a faire la somme sur c pour avoir le total en n'oubliant par les suites constantes qui sont dans les deux
 
'''
from functools import lru_cache

# fonction u et v mémoizée
@lru_cache(maxsize=None)
def u(n,c):
    if n == 1:
        if c==0: return 0
        else : return 1
    return sum([u(n-1,k) for k in range(c+1)])
    
@lru_cache(maxsize=None)
def v(n,c):
    if n == 1:
        if c==0: return 0
        else : return 1
    return sum([v(n-1,k) for k in range(c,10)])
    
# fonction qui donne le nombre total de suites croissantes ou décroissantes de longueur inférieur ou égal n
def total(n):
    if n==0 : return 1 # car 0 compte comme nombre sans chiffre ici
    # On fait la somme pour tous les n du nombre de suites croissantes et décroissante en retirant les 9 suites constantes à chaque étape. 
    return sum([sum([u(k,c)+v(k,c) for c in range(10)])  -9  for k in range(1,n+1)])
    
print(total(100))
