#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True

# Créons une fonction qui donne le nombre premier suivant le nombre impair n donné en entrée :
def premier_suivant(n):
    n+=2
    while not est_premier(n):
        n+=2
    return n
    
N_max=1000000
# On met dans une fonction pour aller plus vite
def chercher():
    liste_premiers=[2,3]
    longueur_max=1
    réponse=0
    indice_0=0 # L'indice du nombre premier du début de la somme (on commence par 2 ici )
    while liste_premiers[indice_0]*longueur_max < N_max: # Un critère pour s'arreter de chercher (ici le nb premier de départ de la somme fois la longueur max de la somme déja trouvée dépasse la borne)
        somme=0
        longueur=0 #nb de termes de la somme
        for p in liste_premiers[indice_0:]:
            if somme+p> N_max: break
            else :
                somme+=p
                longueur+=1
                if est_premier(somme) and longueur>longueur_max :
                    réponse=somme
                    longueur_max=longueur
        else: # Si la somme des nombres premiers ne dépasse pas un million alors on en rajoute
            p=premier_suivant(liste_premiers[-1])
            while somme +p < N_max:
                somme+=p
                longueur+=1
                liste_premiers.append(p)
                if est_premier(somme) and longueur>longueur_max :
                    réponse=somme
                    longueur_max=longueur
                p=premier_suivant(p)
        indice_0+=1       
    return réponse        
        
                        
print(chercher())
