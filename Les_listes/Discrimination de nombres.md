# Discrimination de nombres
`Difficulté : Moyenne`

Le but de cet exercice est de créer un programme qui prend en entrée un nombre entier ***n*** et un nombre ***max*** et qui affiche la liste des nombres entiers compris entre 0 et ***max*** tels que ***n*** n'apparaissent pas dans l'écriture du nombre.

Par exemple :
+ si ***n=1***  et ***max*** = 22, la liste à afficher sera [0,2,3,4,5,6,7,8,9,20,22] car on enlève tous les nombres où 1 apparait.
+ si ***n=13***, dans la liste n'apparaitront pas les nombres qui contiennent 13 comme 130, 4139 ou 313. Par contre les nombres 310 ou 123 seront dans la liste.

::: Aide
Le plus simple pour vérifier si un nombre contient ***n*** est de transformer le nombre et ***n*** en chaine de caractères.
:::

> Entrée : Deux nombres entiers non nuls ***n*** et ***max***.

> Sortie : La liste des nombres compris entre 0 et ***max*** qui ne contiennent pas ***n*** dans leur écriture.

> Défi : Pour les meilleurs, vous pouvez essayer de répondre au problème en ne rajoutant qu'une seule ligne !

@[Discrimination de nombres]({"stubs": ["Les_listes/discrimination_de_nombres.py"], "command": "python3 Les_listes/discrimination_de_nombres_Test.py"})
