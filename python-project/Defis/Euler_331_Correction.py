# Un vrai défi ce problème !
# Temps d'execution de ce programme : 45 min environ
# Si vous voyez comment l'améliorer, vous pouvez me contacter à l'adresse : matcianfapro@outlook.com
'''
Plusieurs remarques qu'on peut se faire en reflechissant au problème :
- On peut enchainer les changements dans l'ordre que l'on veut.
- Faire deux changements au meme endroit s'annulent. Donc il y a au plus un changement par case
- Pour n impair >5, il n'y a pas de solutions. (Conjecture)
L'idée est la suivante pour n pair : 
Ramener tous les points noirs (i,j) qui sont sur une ligne qui a un nombre impair de points noirs dessus sur une ligne l_p qui a un nombre pair de points (pour faire une ligne complète). Pour cela il faut changer la case (i,j) et la case (l_p,j). On fait de même pour les colonnes.
Au final on aura une ligne et une colonne complete qui disparait en modifiant la case (l_p,c_p)
Finalement on se rend compte qu'il faut changer les cases vérifiant la propriété :
nombre de boule noire sur la case  +  nombre de boules noires sur la colonne + nombre de boules noires sur la ligne est impair.
Il n'y a plus qu'à compter !
Et pour cela, il suffit de remarquer qu'une case donne un nombre impaire si c'est une case noire dont le nb de cases noires en ligne et en colonne ont même parité ou bien c'est une case blanche dont le nombre de cases noires en ligne et en colonne ont une parité différente. Pour compter ces dernières, on prend toutes les cases dont les colonnes et lignes n'ont pas la même parité et on retire  le nombre de cases noires qui sont sur ces lignes c'est à dire les cases noires paires.

En résumé, il faut cliquer sur tous les points aux intersections des colonnes paires et lignes impaires (et inverserment) moins le nombre de points déjà présents. A cela il faut ajouter les points qui sont sur des lignes et colonnes impaires (autrement dit les points des lignes impaires qui n'ont pas de points au dessous). 

Pour cela, on remarque qu'il suffit de compter les premières lignes et utiliser la symétrie. Le plus compliqué est la gestion des cases sur la diagonale.

Le programme qui suit est très lent mais fonctionne. Il y a surement des moyens d'optimiser encore
'''

# Fonction qui donne le nombre cases à inverser en fonction de la taille n
def nb_inversion(n):
    # On les calcule une bonne fois pour toute :
    n2=n**2
    n_12=(n-1)**2
    pytha=n_12
    i_max=0
    # compteurs
    nb_cases_noires_paires=0
    nb_cases_noires_impaires=0
    nb_lignes_paires=0
    fini=False
    dessous=False
    for j in range(n-1,-1,-1) : # On descend pour que les cases noires soient trouvées pour des i croissants
        if i_max >= j : 
            if n_12<=pytha<n2 and not fini:
                nb_cases_noires_impaires+= 1
            return 2*(n-nb_lignes_paires)*nb_lignes_paires - nb_cases_noires_paires + nb_cases_noires_impaires
        # Pour éviter de recalculer en partant de 0 à chaque fois, on sait que c'est un quasi cercle donc au pire, il partira d'un cran avant le dernier max trouvé
        compt_ligne=0
        for i in range(i_max,j+1):
            if n_12<=pytha<n2 :
                if i==j : fini=True
                compt_ligne +=1
            elif pytha>= n2: 
                i_max = i-1
                pytha-= 2*i-1
                break
            pytha+= 2*i+1 # Pour ne pas calculer les carrés à chaque fois on utilise l'identité remarquable
        else : 
            i_max=j-1  
            pytha-= 2*j-1
        pytha-= 2*j-1 # Pour ne pas calculer les carrés à chaque fois
        if compt_ligne%2==0 : 
            nb_lignes_paires+=1
            if n_12<=pytha<n2 : # Ca veut dire que la dernière case noire a une case noire dessous
                if fini :
                    nb_cases_noires_impaires+= 1 + 2*dessous
                    nb_cases_noires_paires+=2*(compt_ligne-1-dessous)
                else:
                    nb_cases_noires_impaires+= 2+ 2*dessous
                    nb_cases_noires_paires+=2*(compt_ligne-1-dessous)
                    nb_lignes_paires+=1
                dessous=True    
            else:
                nb_cases_noires_paires+= 2*(compt_ligne-dessous)
                nb_cases_noires_impaires+=  2*dessous
                dessous=False
        else:
            if n_12<=pytha<n2 : # Ca veut dire que la dernière case noire a une case noire dessous
                nb_cases_noires_impaires+= 2*(compt_ligne-1-dessous)
                nb_cases_noires_paires+=2 + 2*dessous
                nb_lignes_paires+=1
                dessous=True
            else:
                if fini :
                    nb_cases_noires_impaires+= 2*(compt_ligne-1-dessous)+1
                    nb_cases_noires_paires+= 2*dessous
                else:
                    nb_cases_noires_impaires+= 2*(compt_ligne-dessous)
                    nb_cases_noires_paires += 2*dessous
                dessous=False
    
# fonction qui calcule la somme
def chercher():
    somme=3 # On met déjà le seul impair pour i = 3 qui est T(5)=3
    for i in range(4,32,2):
        somme+= nb_inversion(2**i-i)
    return somme
        
print(chercher())
