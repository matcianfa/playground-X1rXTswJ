# Il suffit de remarquer que pour obtenir les nombres sur les coins du plus petit carré, on part de 1 et on ajoute 4 fois 2. Pour obtenir les 4 coins du carré d'après, on ajoute 4 fois 4 à 9 etc. On peut même remarquer qu'il suffit d'ajouter la largeur du carré considéré moins 1

#  Ressortons de notre boite à outils la fonction qui permet de savoir si un nombre est premier
def est_premier(n):
    if n < 2 or n%2==0: return False
    for x in range(3, int(n**0.5) + 1,2):
        if n % x == 0:
            return False
    return True
    
    
largeur=1
ratio=1
nb_premiers=0 # Compteur de nombres premiers croisés dans un coin
nb_coins=1 # compteurs de coins considérés en comptant 1
n=1
while ratio>=0.1 : 
    largeur +=2
    for _ in range(4): # On regarde les 4 coins
        n+= largeur-1
        nb_coins+=1
        if est_premier(n) : 
            nb_premiers+=1
    ratio = nb_premiers/nb_coins

print(largeur)
