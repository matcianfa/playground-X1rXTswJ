# L'idée va être de partir du plus grand nombre 1 à 9 pandigital (987654321) et tester s'il peut être le produit concaténé de quelque chose. 
# Comme le début est le produit du nombre par 1, il y a juste à vérifier que ca marche
# exemple pour 987654321 : On teste si le nombre est 9 : après on devrait avoir 9*2=18 donc ca ne marche pas
# Si le nombre est 98 : ensuite on devrait avoir 98*2= 196 donc ca ne marche pas
# Si le nombre est 987 : ...
# Vue la structure du nombre, il ne sert à rien d'aller chercher plus loin que 4 chiffres.
# Si aucun ne marche on prend le nombre 1 à 9 pandigital inférieur suivant


# Pour obtenir les nombres 1 à 9 pandigital dans l'ordre décroissant, on va utiliser les permutations de 987654321
from itertools import permutations

def chercher(): # On met dans une fonction pour sortir dès qu'on a trouvé le résultat
    for pandigital in permutations("987654321"):
        pandigital="".join(pandigital) #On transforme le t-uplet donné par permutations en une chaine de chiffres d'affilée
        for rang in range(1,5):
            n=pandigital[:rang]
            reste=pandigital[rang:]
            multiplicateur=2
            while reste: # On va tester si pandigital est bien de la forme n*1 n*2 n*3... tant qu'on peut
                calcul=str(int(n)*multiplicateur)
                if calcul==reste[:len(calcul)]: # Si n*multiplicateur est bien le début de ce qu'il reste, alors on teste le le multiplicateur suivant
                    if calcul==reste : return pandigital # On a gagné !
                    reste=reste[len(calcul):]
                    multiplicateur+=1
                else : break # Si le début n'est pas bon, on passe au rang suivant
        
print(chercher())
                
