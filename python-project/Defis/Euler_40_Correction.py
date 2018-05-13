# Méthode bourrin : On ecrit le nombre puis on récupère les valeurs

champernowne="0" 
n=1 
longueur=0 # Il vaut mieux calculer au fur et à mesure la longueur de notre chaine plutot que faire len à chaque fois

while longueur<1000000 :
    str_n=str(n)
    champernowne+=str_n
    longueur+=len(str_n)
    n+=1
    
indice=1
réponse=1
for k in range(7):
    réponse*=int(champernowne[indice])
    indice*=10
    
print(réponse)
