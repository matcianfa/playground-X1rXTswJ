# Palindromes (Version récursive)

Un palindrome est une phrase ou un mot qui se lit aussi bien à l'envers qu'à l'endroit. Dans un exercice précédent, on a déjà créé un programme pour déceler quand une phrase était une palindrome. 

Le but de cet exercice est de créer une fonction récursive ***est_palindrome*** qui décèle quand un ***mot*** donné en entrée est un palindrome ou pas.

:::Aide
L'idée pour créer une version récursive et de comparer la première et la dernière lettre. Si c'est la même alors on lance est_palindrome avec le mot privé de sa première et dernière lettre.
:::

> Entrée : Un ***mot***.

> Sortie : Une fonction ***est_palindrome*** qui renvoie (avec `return`) True si le ***mot*** est un palindrome et False sinon.

@[Palindrome ?]({"stubs": ["Les_fonctions/palindrome.py"], "command": "python3 Les_fonctions/palindrome_Test.py"})
