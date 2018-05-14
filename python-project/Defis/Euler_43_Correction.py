# Commençons par créer la liste des premiers nombres premiers
premiers=[2,3,5,7,11,13,17]

# Comme pour les problèmes avec des nombres pandigitals précédents, nous allons utiliser la fonction permutations
from itertools import permutations

somme=0

for pandigital in permutations("0123456789"):
            pandigital="".join(pandigital)  #On transforme le t-uplet donné par permutations en une chaine de chiffres d'affilée
            for indice in range(1,8):
                if int(pandigital[indice:indice+3])%premiers[indice-1]!=0: #Si la sous chaine n'est pas divisible par le nombre premier correspondant
                    break
            else : # Si pour tous les indices, les sous-chaines étaient divisibles alors:
                somme+= int(pandigital)
                
print(somme)
                    
