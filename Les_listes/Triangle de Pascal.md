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

@[Triangle de Sierpinski]({"stubs": ["Les_listes/Triangle_de_Sierpinski.py"], "command": 'echo "TECHIO> open -s /project/target/ index.html"', "command": 'python3 Les_listes/Triangle_de_Sierpinski.py'})



