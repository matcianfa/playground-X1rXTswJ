# En remarquant que si n est un nombre, en additionnant tous les chiffres à la puissance 5 on a au plus log(n)*9^5.
# En étudiant n-log(n)*9^5, on peut obtenir que ça ne sert à rien de chercher pour des valeurs de n supérieures à 350000 car cette fonction devient toujours strictement positive.
somme=0
for n in range(2,350000):
    # Pour obtenir les chiffres de n, on transforme n en chaine de caractères
    if n==sum([int(chiffre)**5 for chiffre in str(n)]):
        somme+=n

print(somme)
