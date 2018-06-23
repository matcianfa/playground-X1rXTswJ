# Une petite fonction qui renverse un nombre.
def renverser(n):
    str_n=str(n) # On le transforme en chaine de caractère
    reponse=""
    for chiffre in str_n:
        reponse=chiffre+reponse
    return int(reponse)
    
# Une petite fonction qui dit si une chaine de caracttère est un palindrome ou non (programmé de manière recursive)
def est_palindrome(mot):
    if len(mot)<2: return True
    return mot[0]==mot[-1] and est_palindrome(mot[1:-1])

compteur_Lychrel=0
for n in range(1,10000):
    k=n+renverser(n) # Il faut faire au moins une itération car un nombre palindrome peut être de Lychrel
    compteur=0  #Compteur pour voir si on a atteint les 50 itérations
    while compteur<50 and not est_palindrome(str(k)): # tant qu'on a pas fait les 50 itérations ou que le nombre k n'est pas un palindrome on calcule...
        k=k+renverser(k)
        compteur+=1
    if compteur==50: 
        compteur_Lychrel+=1
        
print(compteur_Lychrel)

#Remarque : On pourrait optimiser en se souvenant des nombres sur lesquels on est déjà tombé.
    
        
    
    
