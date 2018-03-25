from math import sqrt
nombre_diviseurs = 0
n = 1
while nombre_diviseurs < 250:
    n += 1
    nombre_diviseurs = 0
    # On calcule le nombre triangulaire 1+2+3+...+n
    nombre_triangulaire = sum([i for i in range(n+1)])
    # On cherche maintenant son nombre de diviseurs
    for diviseur in range(1,int(sqrt(nombre_triangulaire))):
        if nombre_triangulaire % diviseur == 0 :
            nombre_diviseurs += 1


print(nombre_triangulaire)

#-------------------------------------------------------------
# Solution plus optimisée
#-------------------------------------------------------------

nombre_diviseurs = 0
n = 1
while nombre_diviseurs < 500:
    n += 1
    nombre_diviseurs = 1
    # On calcule le nombre triangulaire en utilisant la formule 1+2+3+...+n=n*(n+1)/2
    nombre_triangulaire = n*(n+1)//2
    # On cherche maintenant son nombre de diviseurs en utilisant la décomposition en facteurs premiers
    # On sait que le nombre de diviseurs vaut le produit des (exposants + 1)
    # Pour gagner en temps, on s'occupe de 2 à part pour ne chercher ensuite que les diviseurs impairs (qui, avec notre facon de faire seront premiers forcément)
    exposant = 0
    while nombre_triangulaire % 2 == 0 :
        exposant += 1
        nombre_triangulaire //= 2
    nombre_diviseurs *= exposant + 1
    diviseur = 3
    while nombre_triangulaire != 1 :
        exposant = 0
        while nombre_triangulaire % diviseur == 0 :
            exposant += 1
            nombre_triangulaire //= diviseur
        nombre_diviseurs *= exposant + 1
        diviseur += 2

print(n*(n+1)//2)
