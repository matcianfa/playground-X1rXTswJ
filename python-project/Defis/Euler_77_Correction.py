# En admettant la conjecture de Goldbach, on voit qu'il suffit de chercher pour des nombres inférieurs à 10002. En effet : 10002= 10000+2 = 9998+2+2=...=2+2+...2. Et comme tout nombre pair s'écrit comme somme de deux nombres premiers, on peut créer une décomposition en somme de nombres premiers pour chacun des termes des égalités précédentes soit au moins 5000 décompositions.


from functools import lru_cache

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n==2 : return True
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True
    
# liste des nombres premiers inférieurs à racine carrée de racine de 10002
premiers = [ p for p in range(2,int(10002**0.5)+1) if est_premier(p)]

# Fonction qui donne le nombre de décompositions de n en nb premiers inférieurs à p_max
@lru_cache(maxsize=None)
def nb_decomp(n,p_max=n-1):
    if n==1 or n<0 : return 0
    if n==0 : 
        return 1
    somme=0
    for p in premiers:
        if p>p_max : break
        somme+= nb_decomp(n-p,p)
    return somme
    
n=1
nb=0
while nb<5000:
    n+=1
    nb=nb_decomp(n,n-1)
print(n)
