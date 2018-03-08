# Autour de Kaprekar
`Difficulté : Moyenne à difficile`

### Les nombres de Kaprekar

Un nombre de Kaprekar est un nombre dont l'écriture décimale du carré de ce nombre peut être séparée en deux nombres (pas forcément de même taille) dont la somme vaut le nombre initial.

Exemples :
+ 9 est un nombre de Kaprekar car 9²=81 et on peut séparer 81 en 8 et 1 dont la somme 8+1 = 9.
+ 45 est un nombre de Kaprekar car 45²=2025 et on peut séparer 2025 en 20+25=45.
+ 12 n'est pas un nombre de Kaprekar car 12²=144 et on ne peut pas couper ce nombre pour trouver 12 (1+44=45, 14+4=18).
+ 4 879 est un nombre de Kaprekar car 4879² = 23804641 et 238 + 04 641 = 4 879.

Créer un programme qui affiche (avec `print`) si un nombre ***n*** est de Kaprekar ou pas.

> Entrée : Un entier ***n***

> Sortie : "KAPREKAR" ou "PAS KAPREKAR".

@[Kaprekar ?]({"stubs": ["Vrac/Nombres_Kaprekar.py"], "command": "python3 Vrac/Nombres_Kaprekar_Test.py"})

---

### Algorithme de Kaprekar
