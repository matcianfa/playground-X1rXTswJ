# On va utiliser les ensembles pour gagne en vitesse. 
# Comme on nous donne un exemple, on peut commencer les liste à ces valeurs la
ens_pentagonaux = set([])
ens_hexagonaux = set([])

# On met dans une fonction pour gagner en vitesse
def chercher():
    n=1
    while 1: # Tant qu'on a pas trouvé, on cherche
        # Comme les nombres pentagonaux et hexagonaux croissent plus vite, en ajoutant un à chaque fois, on est sur d'être supérieur au nombre tringulaire qu'on considère.
        nb_triangulaire=(n+285)*(n+286)//2
        ens_pentagonaux.add((n+165)*(3*(n+165)-1)//2)
        ens_hexagonaux.add((n+143)*(2*(n+143)-1))
        if nb_triangulaire in ens_pentagonaux and nb_triangulaire in  ens_hexagonaux:
            return  nb_triangulaire
        n+=1
        
print(chercher())
        
