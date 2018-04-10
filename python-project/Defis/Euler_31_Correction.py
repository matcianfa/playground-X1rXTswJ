pièces=[200,100,50,20,10,5,2,1]
# Programmons de manière récursive
# décomposer(n,k) donne le nombre de façon de décomposer n avec les pièces inférieures ou égale à k
def décomposer(n,k=200):
    somme=0
    if n==0 or k==1: # k==1 n'est pas obligatoire mais permet de gagner beaucoup de temps : Si on en est à la pièce 1, on ne peut plus que completer avec des 1 donc il n'y a qu'une facon de le faire.
        return 1
    for pièce in pièces:
        if k >= pièce and n >= pièce :
            somme+= décomposer(n-pièce, pièce)
    return somme

print(décomposer(200))



