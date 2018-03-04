# Triangle de Pascal
`Difficulté : Moyenne`

### Construction

Le triangle de Pascal est un triangle de nombre que l'on croise souvent en mathématiques. On peut trouver sur [Wikipédia](https://fr.wikipedia.org/wiki/Triangle_de_Pascal) beaucoup d'information à son sujet.

En voici les premières lignes : <br/>
1<br/>
1 1<br/>
1 2 1<br/>
1 3 3 1<br/>
1 4 6 4 1<br/>
1 5 10 10 5 1<br/>
...

Pour le contruire une nouvelle ligne :
+ on commence par un 1
+ ensuite, pour les suivants jusqu'à l'avant dernier, on fait la somme du nombre au même niveau dans la ligne précédente avec son prédécesseur. En terme plus informatique, pour constuire le j ième terme de la ligne i, on ajoute le j ième terme et le j-1 ième de la ligne i-1.
+ le dernier terme est un 1.

On pourra jeter un oeil sur cette vidéo pour voir la construction au fur et à mesure : [Youtube](https://youtu.be/N1Pw-QYPTSo?t=3m42s)

Le but de cet exercice est de créer un programme qui prend en entrée un entier ***n*** et affiche la ligne numéro ***n*** du triangle (celle dont le deuxième chiffre est ***n***).

> Entrée : Un entier ***n***.

> Sortie : La ligne numéro ***n*** du triangle de Pascal sous forme de liste de nombres entiers non nuls. La ligne numéro 0 correspond à la première avec un seul 1.

@[Triangle de Pascal]({"stubs": ["Les_listes/Triangle_de_Pascal.py"], "command": "python3 Les_listes/Triangle_de_Pascal_Test.py"})

---

### Triangle de Sierpinski

Le triangle de Sierpinski est un triangle très particulier : Quand on zoom sur une de ses parties, on peut voir de nouveau le triangle en entier. Les objets qui ont cette propriété s'appellent des fractales. On peut aller voir sur [Wikipédia](https://fr.wikipedia.org/wiki/Triangle_de_Sierpiński) pour davantage d'information sur le triangle de Sierpinski.

Une des façons d'obtenir ce triangle est de partir du triangle de Pascal et de représenter par une case noire les nombres impairs et blanche les pairs.

Pour voir le résultat avec votre programme, copiez-collez la partie de votre programme précédent que vous avez rajouté dans la fenêtre ci-dessous et lancez le test. Le test va colorier en noir les nombres impairs et afficher l'image qui correspond.

Vous pouvez modifier la dimension de votre triangle. Vue la façon de calculer notre triangle de Pascal et de l'afficher, on ne peut pas prendre de grandes valeurs. Il faudrait optimiser notre programme pour cela mais ce n'est pas le but ici. Pour voir un triangle entier, il faut prendre des puissances de 2.

@[Triangle de Sierpinski]({"stubs": ["Les_listes/Triangle_de_Sierpinski.py"], "command": "python3 Les_listes/Triangle_de_Sierpinski_Test.py"})

