# Python donne un gros avantage sur ce probleme car la librairie Decimal fait tout le travail

from decimal import *

getcontext().prec=102 # On choisit 2 chiffres en plus dans la précision car un seul en plus crée encore une erreur d'arrondi (il doit y avoir un 99 qui traine)

somme=0
for i in range(2,100):
    if i not in [n*n for n in range(1,10)]:
        somme+=sum([int(chiffre) for chiffre in str(Decimal(i).sqrt()).replace(".","")[:-2]]) #On retire le . du nombre décimal et les 2 derniers chiffres qui ne sont la que pour éviter les erreurs d'arrondi dans le nombre renvoyé par le calcul de sqrt
        
        
print(somme)

# Comme on a un peu triché pour ce problème (en utilisant une librairie qui fait tout), on peut tout de même donner une idée sur comment faire sans la librairie : Il suffit de calculer avec des entiers (car le problème sans cette librairie est le mauvais calcul par Python avec les décimales) et pour cela, il suffit de multiplier le nombre dont on veut la racine par 10^200 (ce qui donnera pour la racine carrée une partie entière à 100 chiffres). Et pour calculer la racine carrée, on peut utiliser la méthode de Héron par exemple ou tout autre méthode plus efficace.
