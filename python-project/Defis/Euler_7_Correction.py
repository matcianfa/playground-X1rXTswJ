from math import sqrt
limite=10001
compteur=1 #On compte déjà 2 pour éviter les conditions pour rien
n=2
while compteur<limite:
    n+=1
    if n%2!=0:# Si n pas pair, on cherche des diviseurs impairs
        for d in range(3,int(sqrt(n))+1,2):
            if n%d==0:
                break
        else: # Si on n'a pas trouvé de diviseurs, c'est un nombre premier
            compteur+=1

print(n)
