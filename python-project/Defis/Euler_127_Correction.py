# Plusieurs remarques evidentes :
# - La triple égalité des PGCD est équivalente à une seule car a+b=c
# - Si a,b et c sont premiers en eux 2 à 2 alors rad(abc)=rad(a)*rad(b)*rad(c). C'est important car du coup, on n'a pas besoin de calculer des radicaux au dela de 120000 

c_max=120000

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
    
# Calcul du PGCD
def PGCD(a,b):
    #if a<b : a,b=b,a
    while b!=0:
        a,b=b,(a%b)
    return a

    
# La liste des nombres premiers inférieurs à racine de 60 000.
premiers = [n for n in range(2,c_max) if est_premier(n)]

# création d'un dictionnaire des radicaux par crible d'erathostene
radicaux={1:1}
for p in premiers:
    for n in range(p,c_max,p):
        radicaux[n]= radicaux.setdefault(n,1)*p
        
# liste ordonnée des a selon les radicaux
liste_a=sorted([a for a in range(1,c_max)], key= lambda a : radicaux[a])

# Fonction qui cherche
def chercher():
    somme=0
    for c in range(3,c_max):
        # Tentative d'optimisation : on range les a par ordre croissant de leur radicaux comme ca, des qu'on dépasse c/2, on arrete la boucle
        for a in liste_a:
            if 2*a>c:continue
            if 2*radicaux[a]*radicaux[c]> c : break
            b=c-a
            if radicaux[a]*radicaux[b]*radicaux[c] < c and PGCD(a,b)==1 :
                somme+=c
    return somme
                
print(chercher())
