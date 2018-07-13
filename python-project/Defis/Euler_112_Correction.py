# Force brute

# Fonction qui renvoie si un nombre est oscillant ou pas en regardant chiffre à chiffre
def est_oscillant(n):
    chiffres=[]
    if n<100: return False
    n,u=n//10, n%10
    n,d=n//10, n%10
    est_decroissante= u<=d
    est_croissante= u>=d
    while n>0 :
        n,d,u=n//10 , n%10 , d # on compare le nouveau chiffre  d par rapport à l'ancien qu'on met dans u
        est_decroissante= est_decroissante and u<=d
        est_croissante= est_croissante and u>=d
        if not (est_decroissante or est_croissante) : return True # Si elle est ni décroissante ni croissante
    return False    


seuil = 0.99

# Fonction qui cherche
def chercher():
    compteur=0
    n=1
    while compteur/n<= seuil : 
        n+=1
        if est_oscillant(n):
            compteur+=1
    return n-1
        
        
print(chercher())
