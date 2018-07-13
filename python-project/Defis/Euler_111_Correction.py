# L'idée va être de déterminer tous les nombres de 10 chiffres ayant m chiffres d où m est le plus grand possible et de regarder si ces nombres sont premiers (car c'est couteux pour des nombres de 10 chiffres)

from itertools import combinations, product


# fonction qui dit si un nombre est premier ou pas 
# Version un peu améliorée en remarquant qu'un nombre premier ne peut être que de la forme 6k-1 ou 6k+1 (à part pour 2 et 3). donc on teste si n est divisible par les nombres de cette forme la uniquement.
def est_premier(n):
    if n==2 or n==3 : return True
    if n==0 or n==1 or n%2==0 or n%3==0: return False
    k=5
    while k*k<=n :
        if n%k==0 : return False
        k+=2
        if n%k==0 : return False
        k+=4
    return True
    
#Fonction qui calcule la somme des nombres de n chiffres avec d qui se répète m fois
def S(n,d,m):
    compteur=0
    for chiffres in product("0123456789".replace(str(d),""),repeat = n-m):
        for indices in combinations(list(range(n)),n-m): # les indices où on va mettre les chiffres différents de d
            x=[str(d)]*n # nombre avec que des d
            for i,chiffre in zip(indices,chiffres): # on remplace les d qui sont aux indices i par d'autres chiffres
                x[i]=chiffre
            if x[0]!="0":
                # On transforme x en nombre
                x=int("".join(x))
                # S'il est premier on l'ajoute à notre compteur
                if est_premier(x):
                    compteur+=x
    return compteur
 
N=10
# Fonction qui cherche 
def chercher():
    reponse =0        
    for d in range(10):
        m=N
        somme=0
        while somme==0:
            m-=1
            somme=S(N,d,m)
        reponse+=somme
    return reponse
    
print(chercher())
