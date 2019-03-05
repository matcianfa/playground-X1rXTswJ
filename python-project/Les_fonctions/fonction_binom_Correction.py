#Copiez-collez ici votre fonction factorielle
def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

#Créez ci-dessous votre fonction binom(n,k)
def binom(n,k):
    if n<k: return 0
    else:
        return factorielle(n)/(factorielle(k)*factorielle(n-k))

