# Fonction qui renvoie True si le triplet est pythagoricien
def est_pythagoricien(a,b,c):
    return a*a+b*b==c*c

# Je crée une fonction pour que la recherche s'arrete dès qu'on trouve un bon triplet
def chercher():
    for a in range(1001):
        for b in range(a+1,1001):
            c=1000-a-b
            if c>b and est_pythagoricien(a,b,c):
                return a*b*c

print(chercher())
