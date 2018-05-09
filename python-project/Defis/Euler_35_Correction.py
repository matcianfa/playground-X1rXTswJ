# Première remarque : Il ne sert à rien de considérer les nombres contenant 0,2,4,6,8 car par rotations il y aura un des nombres qui sera pair
# Même remarque pour le chiffre 5. Donc les chiffres ne peuvent être que 1,3,7 et 9.

# Deuxième remarque : On va utiliser les outils déjà disponibles comme product de la bibliothèque itertools pour avoir directement tous les nombres composés de 1 , 3 ,7, et 9.
from itertools import product

# On crée une fonction pour savoir si le nombre est premier ou pas
def est_premier(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

liste_nombres_premiers_circulaires=set(["2","5"]) #On sauvegarde ceux qu'on trouve ainsi que leurs permutations pour gagner du temps. On y met deja 2 et 5 car ils ne seront pas examinés

for nombre_de_chiffres in range(1,7): # Il y a au plus 6 chiffres
    for n in product("1379",repeat=nombre_de_chiffres):# Attention product donne n sous la forme ("1","1","7","3") par exemple.
        n="".join(n)
        if n in liste_nombres_premiers_circulaires: continue # Si on a déjà regarder n (par rotation) on saute au suivant
        liste_temp=set([]) # On va sauvegarder les rotations de n pour ensuite les rajouter à liste_nombres_premiers_circulaires
        for _ in range(nombre_de_chiffres): # Il y a autant de rotations à faire sur n que de chiffres
            if not est_premier(int(n)):
                break # Si n n'est pas premier on stop la recherche sur n
            liste_temp.add(n)
            if len(n)>=2:
                n=n[1:]+n[0] # On fait une rotation
        else : # Si toutes les rotations sont des nombres premiers (pas de break)
            liste_nombres_premiers_circulaires|=liste_temp

print(len(liste_nombres_premiers_circulaires))



