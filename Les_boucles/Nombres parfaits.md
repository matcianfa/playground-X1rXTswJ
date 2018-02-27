## Nombres parfaits

Un nombre est dit parfait si il est égal à la somme de ses diviseurs stricts (c'est à dire des diviseurs strictement plus petit que lui même).

Par exemple : 
- Les diviseurs de 6 sont 1, 2, 3 et 6. La somme de ses diviseurs stricts est donc 1+2+3=6. Le nombre 6 est donc un nombre parfait.
- Les diviseurs de 8 sont 1, 2, 4, 8. La somme de ses diviseurs stricts est donc 1+2+4=7. Le nombre 8 n'est donc pas parfait.

Écrire un programme qui affiche si le nombre est parfait ou pas. 

::: Aide 
On utilisera le fait que d est un diviseur de n si et seulement si n%d==0.
:::

> Entrée : un nombre entier ***n***.

> Sortie : "PARFAIT" si le nombre est parfait ou "PAS PARFAIT" sinon.

@[Nombre Parfait ?]({"stubs": ["Les_boucles/Nombres_parfaits.py"], "command": "python3 Les_boucles/Nombres_parfaits_Test.py"})
