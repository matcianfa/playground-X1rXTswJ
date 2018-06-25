# Commençons par déterminer jusqu'à quelle valeur de n il faut chercher. en effet, pour former un nombre de n chiffres, il faut valoir moins de 10^n donc quand on cherche une puissance n-ieme, il suffit de chercher pour les nombres de 2 à 9.
# De plus, si 9^n< 10^(n-1), le nombre obtenu n'aura que n-1 chiffres et donc il n'existera aucune puissance n-ieme de n chiffres. Cette inéquation revient à avoir ln(10)/ln(10/9)<n autrement dit, il faut n<=21 pour qu'il y ait des solutions.

compteur=0
for n in range(1,22):
    for k in range(2,10):
        if len(str(k**n))==n :
            compteur+=1
        
print(compteur+1) # On rajoute le 1^1 qu'on n'a pas testé
