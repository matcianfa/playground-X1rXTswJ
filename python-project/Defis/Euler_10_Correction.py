from math import sqrt

# Je commence à 2 pour n'avoir que les nombres premiers impairs à chercher
somme=2
limite=2000000
for n in range(3,limite+1,2):
    # On cherche si n est premier.
    # Pas besoin de tester si le nombre est pair, je ne cherche donc que des diviseurs impairs
    # Pas besoin non plus de chercher un diviseur plus grand que la racine carrée de n
    for d in range(3,int(sqrt(n))+1,2):
        if n%d==0 :
            break
    else :
        # Si on n'a trouvé aucun diviseur, le nombre est premier donc on l'ajoute à la somme
        somme+=n

print(somme)
