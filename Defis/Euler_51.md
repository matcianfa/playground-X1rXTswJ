# Remplacement de chiffres dans un nombre premier
`Difficulté : Moyen (15%)`
`Origine : Projet Euler n°51`

En remplaçant le premier chiffre dans un nombre de 2 chiffres de la forme *3, on peut trouver six sur les neufs possibles qui sont des nombres premiers : 13, 23, 43, 53, 73 et 83.

En remplaçant le troisième et le quatrième chiffres dans un nombre de la forme 56**3 par un même chiffre, ce nombre de cinq chiffre est le premier exemple ayant sept nombres premiers sur les dix générés : 56003, 56113, 56333, 56443, 56663, 56773, et 56993.  Ainsi, 56003 est le plus petit nombre premier ayant cette propriété.

Trouver le plus petit nombre premier qui, en remplaçant une partie de ce nombre (pas forcément des chiffres adjacents) avec un même chiffre engendre une famille de huit nombres premiers.

On affichera le résultat avec `print`.

@[Remplacement de chiffres dans un nombre premier]({"stubs": ["Defis/Euler_51.py"], "command": "python3 Defis/Euler_51_Test.py"})

---

# Multiples permutés
`Difficulté : Facile`
`Origine : Projet Euler n°52`

On peut voir que le nombres 125874 et son double 251748 contiennent exactement les mêmes chiffres mais dans un ordre différent.

Trouver le plus petit entier positif x tel que 2x, 3x, 4x, 5x, et 6x contiennent les mêmes chiffres.

On affichera le résultat avec `print`.

@[Multiples permutés]({"stubs": ["Defis/Euler_52.py"], "command": "python3 Defis/Euler_52_Test.py"})

---

# Selection combinatoire
`Difficulté : Facile`
`Origine : Projet Euler n°53`

Il y a exactement 10 façon de selectionner 3 chiffres parmi 5, 12345 :

123, 124, 125, 134, 135, 145, 234, 235, 245, et 345
En combinatoire, on utilise la notation $`C_5^3 = 10`$.

En général, on a la formule : $`C^r_n= \dfrac{n!}{r!(n-r)!}`$ où $`r\leq n`$, et $`n!=n\times(n-1)\times...\times 3\times 2\times 1`$, et la convention $`0!=1`$.

Ce n'est que pour n=23 qu'une valeur dépasse un million : $`C_{23}{10}=1144066`$.

Combien de valeur de $`C_n^r`$ (non necessairement distincts) pour 1 ≤ n ≤ 100, sont supérieurs à un million ?

On affichera le résultat avec `print`.

@[Selection combinatoire]({"stubs": ["Defis/Euler_53.py"], "command": "python3 Defis/Euler_53_Test.py"})

---

# Mains au poker
`Difficulté : Moyenne (10%)`
`Origine : Projet Euler n°54`

Au Poker, une main est constituée de cinq cartes et ces mains peuvent être rangées, de la moins forte à la plus forte, de la manière suivante :

    La carte la plus haute : La valeur de la carte la plus haute.  
    Une paire : Deux cartes de même valeur.  
    Deux paires : Deux paires différentes.  
    Brelan : Trois cartes de même valeur.  
    Suite : Toutes les cartes de valeurs consécutives.  
    Couleur : Toutes les cartes de la même couleur.  
    Full : Un brelan accompagné d'une paire.  
    Carré : Quatre cartes de même valeur.  
    Quinte flush : Une suite d'une seule couleur.
    
Les cartes sont rangées dans cet ordre (Attention dans la liste donnée, ce sont les initiales anglaises qui sont utilisées) : 

    2, 3, 4, 5, 6, 7, 8, 9, Ten (10), Jack (Valet), Queen (Dame), King (Roi), Ace (As).

Si deux joueurs ont des mains de même rang, alors c'est la valeur la plus haute qui fait ce range qui gagne. Par exemple une pair de 8 bat une pair de 5. Voir l'exemple 1 ci-dessous.  
Si malgré cela, il y a encore égalité, c'est alors la carte de plus haute valeur qui donne le gagnant. Par exemple si les deux joueurs ont une pair de dame, on compare les valeurs de la plus haute carte hors dame. S'il y a encore égalité, on compare les deuxièmes plus hautes etc. Voir l'exemple 4 ci-dessous.  

Voici des exemples de parties de deux joueurs où sont données les mains des deux joueurs suivies du gagnant :

Partie n°1 :  
5H 5C 6S 7S KD (Paire de 5)  
2C 3S 8S 8D TD (Paire de 8)   
Gagnant : Joueur 2
    
Partie n°2 :  
5D 8C 9S JS AC (Plus haute carte : As)  
2C 5C 7D 8S QH (Plus haute carte : Dame)  
Gagnant : Joueur 1
    
Partie n°3 :  
2D 9C AS AH AC (Brelan d'As)  
3D 6D 7D TD QD (Couleur)  
Gagnant : Joueur 2
    
Partie n°4 :  
4D 6S 9H QH QC (Paire de Dame, plus haute carte 9)  
3D 6D 7H QD QS (Paire de Dame, plus haute carte 7)  
Gagnant : Joueur 1
    
Partie n°5:  
2H 2D 4C 4D 4S (Full de 4 par les 2)  
3C 3D 3S 9S 9D (Full de 3 par les 9)  
Gagnant : Joueur 1

On a placé dans la variable ***parties*** 1000 mains aléatoires de deux joueurs. Chaque ligne contient dix cartes séparées par un simple espaces : Les cinq premières correspondent au joueur 1 et les cinq dernières sont les cartes du joueur 2. On pourra supposer que  toutes les mains sont valides (pas de caractères invalides ni de cartes qui se répètent), chaque main est donnée sans ordre spécifique (elles ne sont pas déjà classées) et dans chaque partie, il y a un gagnant (pas d'égalité).

Combien de parties le joueur 1 gagne-t-il ?

On affichera le résultat avec `print`.

@[Mains au poker]({"stubs": ["Defis/Euler_54.py"], "command": "python3 Defis/Euler_54_Test.py"})

---
