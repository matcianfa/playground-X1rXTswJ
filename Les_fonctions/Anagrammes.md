# Anagrammes (version récursive)
`Difficulté : Moyenne`

Le but de cet exercice est de créer une fonction récursive ***anagramme*** qui renvoie la liste de toutes les anagrammes d'un ***mot*** donné en entrée c'est à dire tous mots qu'on peut former en permutant les lettres de ***mot***.

Par exemple : à partir du mot "bac", on peut créer 6 anagrammes : ["bac", "bca", "abc", "acb", "cab", "cba"].

::: Aide
Pour créer une version récursive, on peut commencer par une lettre du ***mot*** à laquelle on rajoute toutes les anagrammesqu'on peut faire avec les lettres restantes du ***mot***, puis on fait pareil avec une autre lettre du ***mot*** etc.

Par exemple avec "bac" : Je commence par chercher les anagrammes commencant par "b". Pour cela je cherche toutes les anagrammes que je peux faire avec les lettres restantes c'est à dire "ac" et "ca" et je rajoute "b" devant pour avoir toutes les anagrammes commençant par b. et je recommence avec a...
:::

> Entrée : Un ***mot*** sans lettre en double.

> Sortie : Une fonction ***anagramme*** qui renvoie (avec `return`) la liste des anagrammes.

@[Anagramme]({"stubs": ["Les_fonctions/anagramme.py"], "command": "python3 Les_fonctions/anagramme_Test.py"})
