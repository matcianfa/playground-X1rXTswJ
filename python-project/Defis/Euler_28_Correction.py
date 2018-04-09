# On remarque qu'on part de 1 puis sur le premier carré, on ajoute les nombres en sautant de 2 en 2
# Le carré suivant, on saut de 4 en 4 puis de 6 en 6 etc. jusqu'à 1000.
somme=1
n=1
for saut in range(2,1001,2):
    for _ in range(4):
        n+=saut
        somme+=n

print(somme)
