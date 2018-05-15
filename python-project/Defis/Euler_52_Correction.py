# Le plus simple pour savoir si deux nombres ont les mêmes chiffres est de ranger les chiffres dans l'ordre croissant pour voir dans les deux cas, on a la même chose. Pour cela, on va les mettre dans une liste

# Pour gagner en rapidité, on met notre programme dans une fonction
def chercher():
    n=1 # Il faut bien commencer quelque part
    while 1 : 
        liste_chiffres_n=sorted([chiffre for chiffre in str(n)]) # la liste des chiffres de n triée par ordre croissant
        for k in range(2,7):
            if sorted([chiffre for chiffre in str(k*n)])!=liste_chiffres_n : # On teste si k*n a les mêmes chiffres que n. Si ce n'est pas le cas, on arrete et passe au n suivant
                break
        else : # Si tous les multiples ont les mêmes chiffres, on renvoie n
            return n
        n+=1        
print(chercher())
