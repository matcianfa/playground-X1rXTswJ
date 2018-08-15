# On calcule toutes les sommes de 1 à n puis on les soustrait pour les avoir toutes
# Il y a un piège : certains nombres sont obtenus plusieurs fois par sommes consécutifs de carrés or il ne faut les compter qu'une fois

n_max= 10**8

# Donne si le mot est un palindrome
def est_palindrome(mot):
    if len(mot)<2: return True
    else:
        return mot[0]== mot[-1] and est_palindrome(mot[1:-1])
        
# Création de la liste des sommes des carrés de 1 à n pour n inférieur à la racine carrée de n_max
sommes_carrés=[0]
s = 0
for n in range(1,int(n_max**0.5)+1):
    s+=n**2
    sommes_carrés.append(s)
    
# Fonction qui cherche la réponse
def chercher():
    résultat = set([])
    for i,s_1 in enumerate(sommes_carrés[1:]):
        for s_2 in sommes_carrés[:i]:
            s = s_1-s_2
            if s <= n_max and est_palindrome(str(s)):
                résultat.add(s)
    return sum(résultat)
    
print(chercher())
