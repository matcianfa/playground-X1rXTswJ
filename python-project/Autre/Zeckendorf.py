from functools import lru_cache

# Fonction avec mémoization qui calcule les termes de la suite de Fibonacci
@lru_cache(maxsize=None)
def fibonacci(n):
    if n==0 : return 1
    if n==1 : return 2
    return fibonacci(n-1)+fibonacci(n-2)


def Zeckendorf(N):
    # On cherche l'indice du nombre de Fibonacci le plus grand qui soit inférieur à N
    indice=0
    while fibonacci(indice)<=N:
        indice+=1
    indice-=1
    # Si N est un nombre de Fibonacci alors on l'affiche seul
    if fibonacci(indice)==N : 
        return str(fibonacci(indice))
    # Sinon on calcule la décomposition du reste qu'on rajoute au nombre trouvé
    else :
        return Zeckendorf(N-fibonacci(indice))+" + "+str(fibonacci(indice))
        
print(Zeckendorf(N)) 
