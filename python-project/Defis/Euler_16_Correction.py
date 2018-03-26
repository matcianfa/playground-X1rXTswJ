n=1000
nombre=2**n
# On traduit le nombre en chaine de caractère et on crée un liste de ses chiffres
liste = [int(chiffre) for chiffre in str(nombre)]
# On affiche la somme des chiffres
print(sum(liste))

#---------------------------------------------------------------------------------
# Version 1 ligne
#---------------------------------------------------------------------------------
print(sum([int(chiffre) for chiffre in str(2**1000)]))
