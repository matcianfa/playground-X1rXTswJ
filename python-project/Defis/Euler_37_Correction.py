# Première remarque : Il ne sert à rien de considérer les nombres contenant 0,2,4,6,8 après le premier chiffre car en troncant, il y aura un des nombres qui sera pair
# Même remarque pour le chiffre 5. Donc les chiffres ne peuvent être que 1,3,7 et 9 (à part le premier).

# On crée une fonction pour savoir si le nombre est premier ou pas
def est_premier(n):
    if n < 2: return False
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return True

# Créons une fonction qui vérifie si le nombre est premier troncable
def est_premier_troncable(n):
    str_n=str(n)
    if not est_premier(n): return False
    for k in range(1,len(str_n)):
        if not est_premier(int(str_n[k:])) or not est_premier(int(str_n[:-k])):
            return False
    else:
        return True

compteur = 0 # Comme on ne sait pas trop quand s'arreter, on utilise le fait qu'on nous dit qu'il n'y en a que 11 à trouver
réponse = 0

n=10
while compteur<11:
    if est_premier_troncable(n):
        compteur+=1
        réponse+=n
    n+=1

print(réponse)
