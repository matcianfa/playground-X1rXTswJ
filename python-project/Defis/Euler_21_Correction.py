from math import sqrt
# Fonction qui calcule la somme des diviseurs propres de n
def somme_diviseurs(n):
    somme=0
    for d in range(1,n):
        if n%d==0:
            somme+=d
    return somme

# Fonction qui calcule la somme des nombres amicaux inférieurs à N
def somme_amicaux(N):
    somme=0
    for n in range(1,N+1):
        m=somme_diviseurs(n)
        if m!=n and somme_diviseurs(m)==n:
            somme+=n
    return somme

print(somme_amicaux(10000))
