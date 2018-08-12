# Méthode brute : On calcule la liste des 100000 nombres et leurs radicaux puis on les range pour en sortir le 10 000 ieme

# fonction qui donne si un nombre est premier ou pas 
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
    
# La liste des nombres premiers inférieurs à racine de 100 000.
premiers = [n for n in range(2,100000+1) if est_premier(n)]

# création de la liste des radicaux par crible d'erathostene
radicaux=[1]*100001
for p in premiers:
    for n in range(p,100001,p):
        radicaux[n]*=p
    
print(sorted(list(range(100001)),key=lambda n : radicaux[n])[10000])
