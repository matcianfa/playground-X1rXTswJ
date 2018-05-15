# En utilisant la formule de Pascal, on peut clairement optimiser en rapidité notre recherche.
# Nous allons ici utiliser la formule donnée. Pour optimiser les calculs avec les factorielles, nous allons utiliser une mémoization (voir la partie optimisation)

# Le cache pour la fonction factorielle
cache={0:1,1:1}

def factorielle(n):
    if n in cache: return cache[n]
    else :
        calcul=n*factorielle(n-1)
        cache[n]=calcul
        return calcul
        
# On met dans une fonction pour aller plus vite
def chercher():
    compteur=0
    for n in range(23,101):
        for r in range(0,n+1):
            if factorielle(n)//(factorielle(r)*factorielle(n-r))>=1000000:
                compteur+=1
    return compteur
    
print(chercher())
