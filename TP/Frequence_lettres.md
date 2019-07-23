# Fréquence d'apparition d'une lettre dans un texte
`Difficulté : Facile`  
`Programme officiel`

Le but de cette page est de créer un programme qui donne la fréquence de chaque lettre dans un texte. Une des applications est le décryptage de codages 'simples' comme celui de César par exemple. En effet, en français, le E apparait beaucoup plus souvent que les autres lettres donc si dans notre message codé par une méthode de César, c'est le W qui apparait le plus, on peut raisonnablement penser que le E est codé en W. Une analyse plus fine des fréquences permet de décoder d'autres lettres que le E.

## Nombre d'occurrences d'une lettre dans un texte

Compléter la fonction `compter(lettre,texte)` suivante pour qu'elle donne  le nombre de fois où la ***lettre*** se trouve dans le ***texte***.

Remarque : Pour ne pas avoir à se soucier des majuscules ou minuscules, on a utilisé la fonction `lower()` pour mettre toutes les lettres du texte en minucules. De plus, dans les textes que nous allons considérer, il n'y aura aucun accent.

@[Nombre d'occurrences d'une lettre dans un texte]({"stubs": ["TP/occurrence.py"], "command": "python3 TP/occurrence_Test.py"})

