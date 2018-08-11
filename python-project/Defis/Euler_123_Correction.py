# On développe en utilisant le binome de Newton et on trouve : 
# si n est pair =2[a²]
# si n est impair = 2na[a²]. Pour n assez grand, p_n> 2n (car le n-ieme nombre premier est équivalent à n ln(n)) donc le reste est directement 2np_n. Il suffit de trouver pour quelle valeur celle-ci dépasse 10^10.



# fonction qui dit si un nombre est premier ou pas 
# Version un peu améliorée en remarquant qu'un nombre premier ne peut être que de la forme 6k-1 ou 6k+1 (à part pour 2 et 3). donc on teste si n est divisible par les nombres de cette forme la uniquement
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
    
# Fonction qui donne le nombre premier suivant n 
# On ne cherche que parmi les impairs
def premier_suivant(n):
    p=n+2
    while not est_premier(p):
        p+=2
    return p
    
# Fonction qui cherche la solution
def chercher(N=10**10):
    n=3 # On commence à 3 pour n'avoir à considérer que des n impairs (car la valeur du reste est 2) et les p impairs (pour gagner en vitesse dans premier_suivant)
    p=5
    while 2*n*p<N :
        n+=2
        p=premier_suivant(premier_suivant(p))
    return n
    
print(chercher(10**10))
