# L'idée est basée sur  la ramque suivante : Si on prend n'importe quel produit a_1*a_2*...*a_n, on peut toujours s'arranger pour qu'il donne un produit égal à la somme (en ajoutant le nombre de 1 qu'il faut.
# Par exemple 2*5 = 10 = 2+5+ 1+1+1. C'est donc un candidat pour k=5. Donc l'idée est de balayer les produits, completer par des un et regarder si le résultats est minimal pour le k qu'on obtient.
# On peut voir assez facilement qu'on balaye bien toute les possibilités en faisant tous les produits possibles

k_max=12000

# Liste dans laquelle on va ranger nos minimums. Au début on met 2*k pour l'indice k car on a une solution évidente pour k termes (il y a k-2 un) : 1+1+1...+1+2+k = 2k = 1*1*1*...*2*k. Donc le minimum cherché est toujours inférieur à 2k.
liste_minimums=[2*k for k in range(k_max+1)]

# La fonction qui prend en entrée la valeur du produit des termes différents de 1( ce qui ne change pas si on les considère d'ailleurs), la somme des termes différents de 1,  le nombre de facteurs dans le produit, et la valeur du dernier terme qu'on a rajouté au produit (pour éviter les doublons, on multiplie à chaque fois par un terme supérieur ou égal au précédent). La fonction modifie le minimum si necessaire et continue à chercher.
def chercher(prod, somme, nb_terme, precedent):
    # On remarque que prod est la valeur commune à la somme (avec les 1) et au produit. Si on soustrait la valeur de la somme (sans les 1) on obtient le nombre de 1. Si on rajoute le nombre de terme (différents de 1) alors on a le nombre de termes. D'où pour obtenir k :
    k=prod-somme+nb_terme
    if k<= k_max: 
        # Comme p donne directement la valeur on a juste à comparer avec le minimum en mémoire pour le rang k
        if prod< liste_minimums[k]:
            liste_minimums[k]=prod
        # On continue à chercher pour avec davantage de termes 
        # Si on réutilise la remarque juste avant la definition de liste_minimums, on sait que le nombre maximum qu'on va chercher sera inférieur à 2*k_max. Si on a déjà une valeur p, le nouveau facteur n'a pas besoin de dépasser 2k_max/p. D'où la borne supérieure
        for a in range(precedent, (2*k_max)//prod +1):
            chercher(prod*a, somme +a, nb_terme+1, a)
            
# On commence avec le nombre 1 et la valeur minimum des termes à rajouter qui vaut 2
chercher(1,1,1,2)

# On ajoute les termes minimums obtenus en commençant à 2 (car l'énoncé commence à 2). On transforme en ensemble car on ne veut pas les doublons.
print(sum(set(liste_minimums[2:])))
