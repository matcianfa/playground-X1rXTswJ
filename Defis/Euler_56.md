# Somme des chiffres de puissances
`Difficulté : Facile`
`Origine : Projet Euler n°56`

Un googol $`10^{100}`$ est un nombre immense : 1 suivi de cent zéros. $`100^{100}`$ est tout aussi inimaginablement grand : 1 suivi de deux cent zéros. Malgré leur taille, la somme de leurs chiffres est seulement 1.

En considérant les entiers naturels de la forme $`a^b`$ avec $`a`$ et $`b`$ strictement inférieurs à 100, Quelle est la somme des chiffres maximale ?

On affichera le résultat avec `print`.

@[Somme des chiffres de puissances]({"stubs": ["Defis/Euler_56.py"], "command": "python3 Defis/Euler_56_Test.py"})

---

# Fraction continue de racine de 2
`Difficulté : Facile`
`Origine : Projet Euler n°57`

On peut démontrer que la racine carrée de deux peut être exprimée comme une fraction continue infinie : 

$`\sqrt{2}=1 + \dfrac{1}{2+\frac{1}{2+\frac{1}{2+\dots}}} = 1.414213...`$

En calculant les quatre premières itérations, on obtient : 

$`1+\dfrac 1 2 = \dfrac 3 2 =1.5`$  
$`1+\dfrac 1{2+\frac 1 2} = \dfrac 7 5 = 1.4`$  
$`1+\dfrac 1{2+\frac 1 {2+\frac 1 2}} = \dfrac {17} {12} = 1.41666...`$  
$`1+\dfrac 1{2+\frac 1 {2+\frac 1 {2+\frac 1 2}}} = \dfrac {41} {29} = 1.41379...`$  

Les trois développement suivants sont $`\dfrac{99}{70}`$, $`\dfrac{239}{169}`$ et $`\dfrac{577}{408}`$ mais le huitième développement $`\dfrac{1393}{985}`$ est le premier example où le nombre de chiffres du numérateur dépasse le nombre de chiffres du dénominateur.

Dans les mille premiers développement, combien de fractions ont un numérateur qui a plus de chiffres que son dénominateur ?

On affichera le résultat avec `print`.

@[Fraction continue de racine de 2]({"stubs": ["Defis/Euler_57.py"], "command": "python3 Defis/Euler_57_Test.py"})

---

# Spirale de nombres premiers
`Difficulté : Facile`
`Origine : Projet Euler n°58`

En partant de 1 et en tournant dans le sens inverse des aiguilles d'une montre, on peut former la spirale de coté 7 suivante : 

**37** 36 35 34 33 32 **31**  
38 **17** 16 15 14 **13** 30  
39 18  **05**  04  **03** 12 29  
40 19  06  01  02 11 28  
41 20  **07**  08  09 10 27  
42 21 22 23 24 25 26  
**43** 44 45 46 47 48 49   

Il est intéressant de noter que 8 des 13 nombres sur les deux diagonales sont premiers. On obtient alors un ratio de 8/13 ≈ 62%.

Si on complète par un nouveau tour la spirale ci-dessus, on obtient un carré de coté 9. Si on continue ce procédé, quel est la plus petite largeur de la spirale carrée qu'il faut pour que le ratio des nombres premiers présents sur les diagonales tombe en dessous de 10% ?

On affichera le résultat avec `print`.

@[Spirale de nombres premiers]({"stubs": ["Defis/Euler_58.py"], "command": "python3 Defis/Euler_58_Test.py"})

---

# Décryptage XOR
`Difficulté : Facile`
`Origine : Projet Euler n°59`

Chaque caractère d'un ordinateur peut être associé à un unique code ASCII. Par exemple, la majuscule A est associé à 65, l'asterisque (*) à 42 et la minuscule k à 107.

Une méthode de cryptage moderne est de prendre un texte, le convertir en code ASCII, et utiliser le XOR (ou exclusif) de chaque valeur avec une valeur donnée, prise dans une clé secrète. L'avantage avec la fonction XOR est qu'en cryptant le message crypté, on le décrypte. Par exemple 65 XOR 42 = 107, et 107 XOR 42 = 65.

Pour un cryptage incassable, la clé doit être de la même longueur que le message à crypter. L'utilisateur garde le message crypté et la clé de cryptage dans des endroits différents et sans les deux moitiés, il est impossible de decrypter le message.

Malheureusement cette méthode est inutilisable la plupart du temps donc on utilise comme clé un simple mot de passe. S'il est plus court que le message, on le répète de manière cyclique tout au long du message à coder. Il faut donc choisir un mot de passe assez long pour être efficace mais assez court pour être mémorisable.

Le but ici est de décoder le message donné et au final donner la somme des valeurs ASCII des lettres du message décrypté. On donne les informations suivantes :
- La clé de cryptage utilisée ne contient que trois lettres minuscules. 
- Le fichier crypté est donné directement sous forme de liste des valeurs ASCII du message.
- Le message original contient des mots communs anglais

On affichera le résultat avec `print`.

@[Décryptage XOR]({"stubs": ["Defis/Euler_59.py"], "command": "python3 Defis/Euler_59_Test.py"})

---

# Ensemble de paires de nombres premiers
`Difficulté : Moyen (20%)`
`Origine : Projet Euler n°60`

Les nombres premiers 3, 7, 109, 673 sont assez remarquables. En prenant n'importe quelle paire parmi ces nombres et en les concaténant dans n'importe quel ordre, on obtient toujours un nombre premier. Par exemple en prenant 7 et 109, les deux nombres formés par concaténation 7109 et 1097 sont premiers. La somme de ces quatre nombres premiers, 792, est la plus petite somme qu'on puisse obtenir à partir d'un ensemble de quatre nombres premiers ayant cette propriété.

Trouver la plus petite somme pour un ensemble de cinq nombres premiers pour lesquels n'importe quelle paire donne, en les concaténant (dans les deux sens) un nombre premier.

Remarque : Il est fort possible que la solution demande trop de temps pour être exécutée ici. Il faudra alors passer par un IDE Python externe.

On affichera le résultat avec `print`.

@[Ensemble de paires de nombres premiers]({"stubs": ["Defis/Euler_60.py"], "command": "python3 Defis/Euler_60_Test.py"})
