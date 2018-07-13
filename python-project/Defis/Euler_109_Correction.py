# On tente par force brute

scoresx1=list(range(1,21))+[25]
scoresx2=[2*s for s in scoresx1]
scoresx3=[3*s for s in range(1,21)]

scores = [0]+scoresx1+scoresx2+scoresx3 # On rajoute 0 pour les éventuels ratés

# Fonction qui cherche
def chercher():
    compteur = 0
    for i,flechette1 in enumerate(scores) :
        for flechette2 in scores[i:]: # Pour éviter les doublons sur les deux premières fleches, on comment à chercher à partir de l'indice i
            for flechette3 in scoresx2:
                if flechette1+flechette2+flechette3<100:
                    compteur+=1
    return compteur
    
                
print(chercher())       
