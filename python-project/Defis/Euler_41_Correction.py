# Première remarque : n vaut au plus 9 puisque c'est un chiffre
# Deuxième remarque : On va utiliser comme dans les problèmes pandigitals précédents le fonction permutations pour générer les nombres pandigitals en commencant par les plus grands
from itertools import permutations

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True
    
chiffres="987654321" # On prend dans l'ordre inverse pour commencer par le plus grand
def chercher(): # On crée une fonction pour s'arreter dès qu'on a trouvé
    for indice in range(9): # On ne va considérer que les chiffres de indice à la fin
        for pandigital in permutations(chiffres[indice:]):
            pandigital="".join(pandigital)  #On transforme le t-uplet donné par permutations en une chaine de chiffres d'affilée
            if est_premier(int(pandigital)) : 
                return pandigital
                
print(chercher())
