# Présentation des boucles ***for***

La boucle `for` énumère les éléments d'un ensemble et pour chaque élément, répète toujours le même code mais pour cet élément. Donnons un exemple informel :

``` python
for objet in liste_courses :
    trouver(objet)
    mettre_dans_le_chariot(objet)
aller_payer()
```
Détaillons un peu. Pour chaque objet dans ma liste de courses, je fais toujours la même chose : je le trouve, je le mets dans le chariot. C'est ça que fait ma boucle `for`. Quand il n'y a plus d'objet dans ma liste de course, je vais payer.  
Attention au fait que, comme pour le `if... else...`, il ne faut pas oublier les ":" en fin de ligne et, de plus, ce qui doit être fait en boucle doit être indenté. Et le `aller_payer` n'est pas indenté car je ne paye qu'à la fin. S'il était indenté, je devrais pour chaque objet aller payer avant de passer à l'objet suivant...

Passons à des exemples plus informatiques.  
Nous allons nous intéresser principalement à l'énumération de nombres car c'est de loin la plus utile au début. Pour créer une liste de nombres, on utilise la fonction `range`.

+ range(n) : crée une liste de n nombres allant de 0 à n-1.  
Et oui en informatique, il va falloir prendre l'habitude de toujours commencer à 0 et du coup finir à n-1 si on veut n nombres en tout.
+ range(n1,n2) : crée une liste de nombres allant de n1 à n2-1.
+ range(n1,n2,pas) : crée une liste de nombres allant de n1 à n2-1 en sautant de pas en pas.

Par exemple :
range(4) est la suite de nombres 0 1 2 3
range(3,6) est la suite de nombres 3 4 5
range(1,9,3) est la suite de nombres 1 4 7 (de 3 en 3 en partant de 1)
range(3,0,-1) est la suite 3 2 1  (un pas négatif permet de compter à l'envers ce qui est très pratique des fois)

Passons à des exemples d'utilisation :
``` Python
>>>for i in range(3) :
>>>    print(i)
0
1
2
```
``` Python
>>>somme=0
>>>for i in range(4) :
>>>    somme+= i
>>>print(somme)
6
```
Détaillons cet exemple : Pour i allant de 0 jusqu'à 3 (c'est à dire range(4)), je demande à chaque fois somme+=i ce qui veut dire que je rajoute à somme la valeur i. Finalement, j'affiche le résultat qui n'est autre que 0+1+2+3.

# Entrainement 

### Exercice 1

On a recopié ci-dessous le programme de l'exemple précédent.
Modifier ce programme pour qu'il affiche la somme des entiers de 3 à 172 c'est à dire 3 + 4 + 5 + ... + 171 + 172.

@[Exercice 1]({"stubs": ["Les_boucles/for_exo_1.py"], "command": "python3 Les_boucles/for_exo_1_Test.py"})

---

### Exercice 2


