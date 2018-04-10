pièces=[200,100,50,20,10,5,2,1]
# Programmons de manière récursive
# décomposer(n,k) donne le nombre de façon de décomposer n avec les pièces inférieures ou égale à k
def décomposer(n,k=200):
    somme=0
    for pièce in pièces:
        if k >= pièce and n > pièce :
            somme+= décomposer(n-pièce, pièce)
        elif k >= pièce and n==pièce :
            somme+=1
    return somme

print(décomposer(200))

