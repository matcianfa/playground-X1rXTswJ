# Somme des chiffres d'une puissance
`Difficulté : Facile`
`Origine : Projet Euler n°16`

$`2^{15} = 32768`$ et la somme de ses chiffres est 3 + 2 + 7 + 6 + 8 = 26.

Quelle est la somme des chiffres du nombre $`2^{1000}`$ ?

On affichera le résultat avec `print`.

@[Somme des chiffres d'une puissance]({"stubs": ["Defis/Euler_16.py"], "command": "python3 Defis/Euler_16_Test.py"})

---

# Compter le nombre de lettres
`Difficulté : Facile`
`Origine : Projet Euler n°17`

Le problème d'origine étant en anglais, il faudra utiliser les nombres écrits en anglais.

Si les nombres de 1 à 5 étaient écrits en toutes lettres : one, two, three, four, five, alors il y aurait 3 + 3 + 5 + 4 + 4 = 19 lettres utilisées en tout.

Si tous les nombres de 1 à 1000 (one thousand) inclus étaient écrits en toutes lettres, combien de lettres seraient utilisées en tout ?

NOTE: Ne pas compter les espaces ni les tirets. Par exemple, 342 (three hundred and forty-two) contient 23 lettres et 115 (one hundred and fifteen) contient 20 lettres. L'utilisation de "and" quand on écrit des nombres est conforme aux habitudes britanniques.

On affichera le résultat avec `print`.

@[Compter le nombre de lettres]({"stubs": ["Defis/Euler_17.py"], "command": "python3 Defis/Euler_17_Test.py"})

---

# Chemin de somme maximum
`Difficulté : Facile`
`Origine : Projet Euler n°18`

A partir d'un nombre dans les triangles ci-dessous, on peut se déplacer uniquement vers le bas soit vers le nombre juste en dessous, soit vers le nombre à droite de celui qui est en dessous. Par exemple, à partir du 6, on peut descendre uniquement vers le 9 ou le 3 mais pas vers le 5.

En partant du sommet du triangle ci-dessous, le chemin dont le total en additionnant les nombres du chemin est le plus grand est 23.

***3***  
***7*** 4  
2 ***4*** 6  
8 5 ***9*** 3  

En efft, 3 + 7 + 4 + 9 = 23.

Trouver le total le plus grand possible en suivant un chemin sur le triangle ci-dessous.

75  
95 64  
17 47 82  
18 35 87 10  
20 04 82 47 65  
19 01 23 75 03 34  
88 02 77 73 07 63 67  
99 65 04 28 06 16 70 92  
41 41 26 56 83 40 80 70 33  
41 48 72 33 47 32 37 16 94 29  
53 71 44 65 25 43 91 52 97 51 14  
70 11 33 28 77 73 17 78 39 68 17 57  
91 71 52 38 17 14 91 43 58 50 27 29 48  
63 66 04 68 89 53 67 30 73 16 69 87 40 31  
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23  

On affichera le résultat avec `print`.

Pour vous aider, on a déjà rentré le triangle dans un liste contenant une liste de chaque ligne.
Ainsi, pour obtenir le 82 situé à la ligne 4 et à la colonne 2 (on commence à 0), on aura juste à écrire `triangle[4][2]`.

@[Chemin de somme maximum]({"stubs": ["Defis/Euler_18.py"], "command": "python3 Defis/Euler_18_Test.py"})

---


