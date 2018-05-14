# Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

# On met le tout dans une fonction pour gagner en vitesse
def chercher():
    # Créons une liste des nombres premiers qu'on complétera au fur et à mesure (On exclut 2 vue les propriétés à vérifier)
    liste_premiers=[3]
    # Créons aussi l'ensemble des doubles des carrés
    ens_double_carrés=set([0,2,8,18])
    
    n=5 # le nombre  qu'on considère
    while 1:
        #On ajoute les carrés de n-1 et n dans ens_carrés même s'il ne vont pas servir de suite
        ens_double_carrés.add(2*((n-1)**2))
        ens_double_carrés.add(2*n*n)
        if est_premier(n):
            liste_premiers.append(n)
        for p in liste_premiers:
            if n-p in ens_double_carrés: 
                break
        else : 
            return n
        n+=2
        
print(chercher())
