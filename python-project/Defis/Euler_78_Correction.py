# On peut remarquer que la question est très similaire au problème 76 dont on pourrait reprendre la code mais la formule utilisée est trop lente.
# On va donc utiliser ici une formule de récurrence qu'on peut trouver ici : https://fr.wikipedia.org/wiki/Partition_d%27un_entier#Relation_de_r%C3%A9currence
#De plus, étant donné la question , on va travailler modulo 1000000

from functools import lru_cache

# Fonction qui calcule le nombre de décompositions de n. On mémoize bien sur et vu la question au problème, il suffit de travailler modulo 1 000 000.
@lru_cache(maxsize=None)
def p(n):
    if n==1 or n==0  : return 1 # Les cas évidents
    if n<0 : return 0
    somme=0
    k=1
    while (k*(3*k-1))//2<=n:
        somme=(somme+((-1)**((k+1)%2))*(p(n-(k*(3*k-1))//2)+p(n-(k*(3*k+1))//2)))%1000000
        k+=1
    return somme
    

n=1
while p(n)!=0:
    n+=1
print(n)
