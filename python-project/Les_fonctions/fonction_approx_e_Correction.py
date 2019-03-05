#Copiez collez votre fonction factorielle ici
def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

#Créez ci dessous votre fonction approx_e(n)
def approx_e(n):
    if n==0:
        return 1
    else:
        return 1/factorielle(n)+approx_e(n-1)

