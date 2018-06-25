# Idée : calculer tous les cubes tant qu'on ne trouve pas et les ranger dans un dictionnaire avec pour clé le nombre formé des chiffres dans l'ordre croissant (par exemple 7^3 =343 serait associé = 334). Dés qu'une clé a 5 valeurs, on a trouvé.


# Fonction qui range les chiffres d'un nombre dans l'ordre croissant.
def ordonner(n):
    return "".join(sorted([chiffre for chiffre in str(n)])) ### trouver la bonne fonction
    
    
# Fonction qui cherche la solution 
def chercher():
    dic={}
    n=1
    while 1:
        cube_ordonné= ordonner(n*n*n)
        dic[cube_ordonné]=dic.setdefault(cube_ordonné,[])+[n]
        if len(dic[cube_ordonné])==5:
            return dic[cube_ordonné][0]**3
        n+=1
        
print(chercher())
