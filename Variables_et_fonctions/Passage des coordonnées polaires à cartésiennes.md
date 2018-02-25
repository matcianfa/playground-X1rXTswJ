## Passage des coordonnées polaires à cartésiennes

Pour étudier le mouvement d'un objet (une planète par exemple), il est parfois plus pratique de repérer cet objet par ses coordonnées polaires.
On pourra trouver une présentation de ce système de coordonnées  ainsi que des indications pour la suite sur cette page [Wikipédia](https://fr.wikipedia.org/wiki/Coordonn%C3%A9es_polaires)

Le but de cet exercice est de créer un programme qui traduit les coordonnées polaires en coordonnées cartésiennes.

+ Pour cela, voici les formules de passage des coordonnées polaires $`(r,\theta)`$ aux coordonnées cartésiennes $`(x,y)`$ :

$`\left\{\begin{array}{l} x= r.cos (\theta) \\ y= r.sin (\theta)\end{array}\right.`$


+ Je rappelle que le cosinus et sinus en Python sont en radians. Pour les tests, les angles seront donnés en degrés ce qui signifie  qu'il faudra multiplier $`\theta`$ par $`\frac{\pi}{180}`$.

+ De plus, les résultats devront être arrondis à 3 chiffres après la virgule. Pour cela, on utilisera la fonction `round( nombre , nombre_de_chiffres_après_la_virgule)`.
+ Enfin, les résultats ***x*** et ***y*** devront être affiché d'affilée, simplement séparés d'un espace. Pour cela, on utilisera simplement la synthaxe `print(x,y)`

>Entrée : Les valeurs de $`r`$ et $`\theta`$ (en degrés).

>Sortie : Les coordonnées cartésiennes ***x*** et ***y*** correspondants aux coordonnées polaires données en entrée.

@[Passage des coordonnées polaires à cartésiennes]({"stubs": ["Passage_polaires_cartesiennes.py"], "command": "python3 Passage_polaires_cartesiennes.py_Test.py"})

