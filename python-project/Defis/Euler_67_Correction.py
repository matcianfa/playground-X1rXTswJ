# L'idée est simplement de partir de la derniere ligne et de remonter en remplaçant à chaque fois le chiffre par la somme avec les nombres en dessous qui est la plus grande.

triangle='''
A copier coller de l'énoncé
'''

# On transforme le triangle donné sous forme de tableau. Pour avoir le nombre qui se trouve à la ligne 3 et la colonne 1, il suffit d'ecrire triangle[3][1] (qui donnera 53). Attention la première ligne est la ligne 0, de même pour les colonnes.
triangle=[[int(k) for k in ligne.split()] for ligne in triangle.split("\n")][1:-1]


for ligne in range(len(triangle)-2,-1,-1):
    for colonne in range(ligne+1):# il y a numero de la ligne+1 termes sur les lignes
        triangle[ligne][colonne]+= max(triangle[ligne+1][colonne],triangle[ligne+1][colonne+1])
        
print(triangle[0][0])
