"""
Euler 128
En regardant bien, on se rend compte que les seules cases qui peuvent avoir 3 nombres premiers autour sont celles dans l'alignement 1,2,8,20...
et celles juste avant ()
Plus précisément les premières sont celles de la forme N=2+3k(k+1)
Ces cases sont entourées par les cases N+1,N+6(k+1), N+6(k+1)+1,N+6(k+1)-1,N-6k,N+6(2k+3)-1.
Si on fait les soustractions, il reste 1,6(k+1),6(k+1)+1, 6(k+1)-1, 6k, 6(2k+3)-1.
Comme 1, 6(k+1) et 6k ne peuvent pas être premiers, il reste juste à chercher pours quels k, les trois nombres restants sont premiers.
Les autres sont de la forme N-1.
Les voisines sont N-6k,N-2,N-6(2k-1),N+6(k+1)-1,N+6(k+1)-2,N+6(k+1)-3
En soustrayant et ne gardant que celles qui peuvent être un nombre premier, il reste : 6k-1,12k-7,6k+5
"""

from sympy import isprime

def chercher(N):
    k = 1
    compteur = 1
    print("le premier nombre est 1")
    while compteur <N :
        if isprime(6*k-1) and isprime(12*k-7) and isprime(6*k+5):
            compteur +=1
            reponse = 2+3*k*(k+1)-1
            print("Le {}e nombre est {}".format(compteur,reponse))
        if isprime(6*k+7) and isprime(6*k+5) and isprime(12*k+17):
            compteur +=1
            reponse = 2+3*k*(k+1)
            print("Le {}e nombre est {}".format(compteur,reponse))
        k+=1
    return reponse

print(chercher(2000))

