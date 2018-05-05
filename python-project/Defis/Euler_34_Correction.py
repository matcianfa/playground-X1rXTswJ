# Première remarque : il ne sert a rien de regarder les nombres de 8 chiffres et plus
# car pour 8 chiffres, la valeur maximale qu'on puisse obtenir est 9!*8=2903040 qui ne fait que 7 chiffres.
# De plus, pour 7 chiffres, on obtient au mieux 9!*7=2540160 donc il ne sert à rien de chercher au dela
# D'un point de vue plus mathématique, on peut étudier la fonction x*9!-10^(x-1) pour voir qu'elle est négative pour x>=8

# Deuxième remarque : pour gagner en vitesse, on va mémoizer les valeurs des factorielles
# On pourrait aussi directement créer un liste des valeurs des 10 premières factorielles
cache={0:1,1:1} #On remplit déjà les valeurs de 0! et 1!
def factorielle(n):
    if n in cache : return cache[n]
    else : return n*factorielle(n-1)

reponse=0
for n in range(10,2540160):
    somme_factorielles=0
    # Pour chaque chiffre, on calcule la factorielle et on l'ajoute à la somme des précédents
    # Pour pouvoir récupérer les chiffres, on transforme n en chaine de caractères
    for chiffre in str(n):
         somme_factorielles += factorielle(int(chiffre))
    if somme_factorielles==n:
        reponse+=n

print(reponse)
