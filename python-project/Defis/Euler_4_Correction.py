#Fonction qui vérifie si le nombre est un palindrome
def est_palindrome(n):
    n=str(n) # On traduit n en chaine de caractères
    longueur=len(n)
    # On compare la première et la dernière lettre puis la deuxième et l'avant dernière...
    # Si une paire diffère, on arrete en renvoyant False
    for i in range(longueur//2):
        if n[i]!=n[longueur-i-1]:
            return False
    return True

# Pour chercher le plus grand, on part des produits les plus grands par ordre décroissant
# Pour des raisons de symétries, il suffit que a aille de 999 à 100 et b aille de 999 à a
max=0
for a in range(999,99,-1):
    for b in range(999,a-1,-1):
        ab=a*b # Pour éviter de calculer trois fois le produit
        if max<ab and est_palindrome(ab) :
            max=ab

print(max)
