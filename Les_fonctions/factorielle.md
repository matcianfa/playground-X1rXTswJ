# Incontournable factorielle (version recursive)

La factorielle d'un nombre ***n*** (noté $`n!`$) est définie par $`n!=1\times 2\times 3\times\dots\times n`$ et par convention $`0!=1`$. On a déjà crée un programme avec un boucle `for`pour calculer la factorielle d'un nombre. Cette fois-ci, nous allons créer la version recursive.

En remarquant que $`factorielle(n)=n \times factorielle(n-1)$`, créer une version recursive de la fonction factorielle.

> Entrée : Un entier naturel ***n***.

> Sortie : La fonction ***factorielle*** programmée de manière récursive qui revoie (avec `return`) $`n!`$.

@[Créer une fonction factorielle]({"stubs": ["Les_fonctions/factorielle.py"], "command": "python3 Les_fonctions/factorielle_Test.py"})
