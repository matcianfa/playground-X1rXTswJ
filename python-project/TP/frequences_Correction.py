def compter(lettre,texte):
    compteur = 0
    for L in texte.lower() :
        if L == lettre :
            compteur +=1
    return compteur

def frequence(texte):
    N = len(texte)
    alphabet="abcdefghijklmnopqrstuvwxyz"
    resultat = []
    for lettre in alphabet :
        resultat.append(compter(lettre,texte)/N)
    return resultat

"""
Remarque : C'est une très mauvaise façon de faire si le texte est très long
( un livre ou même l'ensemble des textes d'une bibliothèque..) car on parcourt 26 fois le texte.
Pour améliorer cela, il vaudrait mieux utiliser un dictionnaire  qui à chaque lettre
compte le nombre de fois où on la croise et le remplir au fur et à mesure
qu'on lit le texte pour ne le parcourir qu'une fois. A la place du dictionnaire,
on pourrait utiliser une liste mais en passant par le code ASCII des lettres
"""

