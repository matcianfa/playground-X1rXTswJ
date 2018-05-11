# On a déjà créé une fonction pour savoir si une chaine de caractère est un palindrome :
def est_palindrome(mot):
    if len(mot)<2: return True
    else:
        return mot[0]== mot[-1] and est_palindrome(mot[1:-1])

# Créons une fonction qui convertit un nombre entier en binaire (directement en chaine de caractère) :
def dec_to_bin(n):
    q = -1
    res = ""
    while q != 0:
        q = n // 2
        r = n % 2
        res = str(r) + res
        n = q
    return res

# Il ne reste plus qu'à tester pour tous les nombres inférieurs à un million
somme=0

for n in range(1,1000000):
    if est_palindrome(str(n)) and est_palindrome(dec_to_bin(n)):
        somme+=n

print(somme)
