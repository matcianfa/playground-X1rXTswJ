# fonction qui calcule la factorielle
def factorielle(n):
    if n==1 or n==0 : return 1
    return n*factorielle(n-1)

N=factorielle(100)
# On transforme N en chaine de caractères pour pouvoir recupérer chiffre par chiffre
print(sum([int(chiffre) for chiffre in str(N)]))
