from math import sqrt
n=600851475143
diviseur_trouvé=True
# On divise n par le premier diviseur d qu'on trouve (qui sera forcément premier)
# On recommence avec n//d jusqu'à ce qu'on ne puisse plus
# Le n pour lequel on ne peut plus est le plus grand diviseur premier
# On utilise la remarque classique qui consiste à ne pas chercher un diviseur plus grand que la racine carrée du nombre
while diviseur_trouvé:
    diviseur_trouvé=False
    # Vu que le nombre n'est pas pair, on ne cherche que les diviseurs impairs pour gagner du temps
    for i in range(3,int(sqrt(n))+1,2):
        if n%i==0:
            diviseur_trouvé=True
            n=n//i
            break
print(n)
