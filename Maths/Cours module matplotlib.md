<h1> <center>Cours : Le module matplotlib</center></h1>

Le module matplotlib est un module très complet. Nous allons ici nous intéresser à quelques exemples d'utilisation comme par exemple le tracé de représentations graphiques de fonctions ou de séries statistiques. On pourra trouver davantage d'informations sur la [documentation officielle](https://matplotlib.org/index.html) (en anglais) ou une version plus légère mais en français [ici](http://chamilo1.grenet.fr/ujf/courses/FAMILIARISATIONAVECPYTHONSUITEANACON/document/Python/matplotlib.pdf).

# Présentation du module matplotlib

## Importer le(s) module(s)

Comme tous les modules, il faut le charger et plus précisément c'est un sous-module qui va nous intéresser : pyplot. Pour cela, nous n'allons pas charger toutes les fonctions comme d'habitude mais l'importer sous un nom plus court à utiliser. On utilisera donc `import matplotlib.pyplot as plt`. Ce qui signifie que pour utiliser une fonction de ce module comme `show()` par exemple, on devra écrire `plt.show()` (puisqu'on a importer le module sous le nom plt).  
De plus, le module matplotlib est très lié à un autre module qui sert à faire du calcul numérique qui s'appelle numpy et qu'on import souvent sous le nom np. 

Pour résumer, pour représenter graphiquement des fonctions ou autres, il faudra mettre en entête :
```python
import matplotlib.pyplot as plt
import numpy as np
```

## Les fonctions de base

+ `plt.show()` : Pour afficher le résultat. Toute les fonctions qui suivent servent à préparer le graphique mais si on ne demande pas de l'afficher, rien ne se passera (exactement comme la fonction `print` : aucun calcul ne s'affiche si on ne demande pas de l'afficher avec `print`).

+ `plt.plot(liste_x,liste_y)` : Où liste_x est une liste de nombres [x_1, x_2, ..., x_n] et liste_y une liste de nombres [y_1, y_2, ..., y_n] avec le même nombre d'éléments. Alors `plt.plot(liste_x,liste_y)` placera les points de coordonnées (x_1,y_1), (x_2,y_2), ..., (x_n, y_n) et les reliera de proche en proche par un segment. Voici un exemple où on relie les points (1;2), (3;1) et (4;6) :
  @[Exemple d'utilisation de plot]({"stubs": ["Maths/plot1.py"], "command": "python3 Maths/plot1_Test.py"})
  


# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
k = 0
while k < 6 :
    print(k)
    k += 2
```  
?[Que va afficher ce programme (les `/` remplacent ici un retour à la ligne)? ]
-[x] 0 / 2 / 4 
-[ ] 0 / 1 / 2 / 3 / 4 / 5 
-[ ] 0 / 2 / 4 / 6
-[ ] 2 / 4 

---

###### QCM 2
```python
k = 0
while k < 6 :
    k += 2
    print(k)
```  
?[Que va afficher ce programme (les `/` remplacent ici un retour à la ligne)? ]
-[ ] 0 / 2 / 4 
-[ ] 0 / 1 / 2 / 3 / 4 / 5 
-[ ] 0 / 2 / 4 / 6
-[x] 2 / 4  

---

###### QCM 3
```python
n=0
while ... :
    print(n)
    n += 3
```  
?[Par quoi remplacer les ... pour que le programme précédent affiche 0 / 3 / 6 / 9 / 12 (les `/` remplacent ici un retour à la ligne) ? ]
-[ ] n < 12
-[x] n <= 12
-[x] n < 14
-[x] n**2 < 145

---

###### QCM 4
```python
n=0
while ... :
    n += 1
print(n)
```  
?[Par quoi remplacer les ... pour que le programme précédent affiche la plus petite valeur de n telle que n²+3n dépasse 1000 ? ]
-[ ] n² + 3n < 1000
-[ ] n**2 + 3*n > 1000
-[ ] n < 1000
-[x] n**2 + 3*n < 1000

---

###### QCM 5
```python 
n = 0
somme = 0
while somme < 10000 :
    n += 1
    ... 
print(n)
``` 
?[Par quoi remplacer les ... pour que le programme précédent affiche la plus petite valeur de n telle que 2*1+ 2*2 + 2*3 + ... + 2*n dépasse 10000 ?]
-[ ] somme += n
-[ ] somme = 2 * somme 
-[x] somme += 2*n
-[ ] somme = 2*1+ 2*2 + 2*3 + 2*n

---

###### QCM 6
```python
n=0
while ... :
    n += 1
print(n)
```  
?[Par quoi remplacer les ... pour que le programme précédent affiche la plus petite valeur de n telle que 1/n soit inférieur à 0.12345 ? ]
-[ ] n < 0.12345
-[ ] 1/n < 0.12345
-[ ] 1/n != 0.12345
-[x] 1/n > 0.12345


# Entrainement 

### Exercice 1

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que (n+1)\*(n+3) dépasse 12345.

@[Exercice 1]({"stubs": ["Les_boucles/while_exo1.py"], "command": "python3 Les_boucles/while_exo1_Test.py"})

---

### Exercice 2

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que 4 + 5 + 6 + ... + n dépasse 12345.

@[Exercice 2]({"stubs": ["Les_boucles/while_exo_2.py"], "command": "python3 Les_boucles/while_exo_2_Test.py"})

---

### Exercice 3

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que 1² + 2² + 3² + ... + n² dépasse 12345.

@[Exercice 3]({"stubs": ["Les_boucles/while_exo_3.py"], "command": "python3 Les_boucles/while_exo_3_Test.py"})
