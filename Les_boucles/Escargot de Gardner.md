## Escargot de Gardner

Nous allons nous intéresser à la progression de l'escargot  de Gardner. Je vous renvoies vers cette vidéo pour une présentation : [Youtube](https://www.youtube.com/watch?v=L1vDkUziBpw).

En résumé, ce qui va nous intéresser ici est que la ***n***-ieme heure, le pourcentage de progression de l'escargot sur l’élastique augmente de $`\frac 1 n `$.
Autrement dit, le pourcentage de progression  la ***n***-ieme heure est $`1+\frac 1 2+\frac 1 3+\dots+\frac 1 n`$.
On se demande naturellement au bout de combien de temps ce pourcentage de progression dépassera une valeur donnée ***e***.

Écrire un programme qui prend en entrée une valeur ***e*** et affiche en sortie la plus petite valeur de ***n*** pour laquelle le pourcentage de progression dépasse ***e***.

> Entrée : Un nombre strictement positif ***e*** pas trop grand (regarder la vidéo pour comprendre pourquoi).

> Sortie : La plus petite valeur de ***n*** tel que $`1+\frac 1 2+\frac 1 3+\dots+\frac 1 n >e`$.

@[Escargot de Gardner]({"stubs": ["Les_boucles/Gardner.py"], "command": "python3 Les_boucles/Gardner_Test.py"})
