limite=1000000
longueur_max=0 # La longueur maximale trouvée jusque là
nombre_max=0 # On garde en mémoire le nombre qui donne la chaine la plus longue

for n in range(2,limite+1):
    compteur = 1 # Compte la longueur de la chaine
    u = n
    while u !=1 :
        if u % 2 == 0 :
            u //= 2
        else :
            u = 3*u + 1
        compteur += 1
    if compteur > longueur_max :
        longueur_max = compteur
        nombre_max = n

print(nombre_max)
