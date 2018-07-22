<h1> <center>Cours : Le module matplotlib</center></h1>

Le module matplotlib est un module très complet. Nous allons ici nous intéresser à quelques exemples d'utilisation comme par exemple le tracé de représentations graphiques de fonctions ou de séries statistiques. On pourra trouver davantage d'informations sur la [documentation officielle](https://matplotlib.org/index.html) (en anglais) ou une version plus légère mais en français [ici](http://chamilo1.grenet.fr/ujf/courses/FAMILIARISATIONAVECPYTHONSUITEANACON/document/Python/matplotlib.pdf).

# Présentation du module matplotlib

## Importer le(s) module(s)

Comme tous les modules, il faut le charger et plus précisément c'est un sous-module qui va nous intéresser : pyplot. Pour cela, nous n'allons pas charger toutes les fonctions comme d'habitude mais l'importer sous un nom plus court à utiliser. On utilisera donc `import matplotlib.pyplot as plt`. Ce qui signifie que pour utiliser une fonction de ce module comme `show()` par exemple, on devra écrire `plt.show()` (puisqu'on a importer le module sous le nom plt).  
De plus, le module matplotlib est très lié à un autre module qui sert à faire du calcul numérique qui s'appelle numpy et qu'on import souvent sous le nom np. 

Pour résumer, pour représenter graphiquement des fonctions ou autres, il faudra mettre en en-tête :
```python
import matplotlib.pyplot as plt
import numpy as np
```

## Les fonctions de base

+ `plt.show()` : Pour afficher le résultat. Toute les fonctions qui suivent servent à préparer le graphique mais si on ne demande pas de l'afficher, rien ne se passera (exactement comme la fonction `print` : aucun calcul ne s'affiche si on ne demande pas de l'afficher avec `print`).

+ `plt.plot(liste_x,liste_y)` : Où liste_x est une liste de nombres [x_1, x_2, ..., x_n] et liste_y une liste de nombres [y_1, y_2, ..., y_n] avec le même nombre d'éléments. Alors `plt.plot(liste_x,liste_y)` placera les points de coordonnées (x_1,y_1), (x_2,y_2), ..., (x_n, y_n) et les reliera de proche en proche par un segment. Voici un exemple où on relie les points (1;2), (3;1) et (4;6) :
  @[Exemple d'utilisation de plot]({"stubs": ["Maths/plot1.py"], "command": "python3 Maths/plot1_Test.py"})
  Vous pouvez modifier les listes de points dans le programme ci-dessus pour voir le résultat.  
  L'idée pour tracer une fonction va donc être de placer beaucoup de points de la courbe qu'on veut représenter assez proches pour qu'on ne voit pas qu'ils sont reliés par une droite.
  
+ `np.linspace(debut, fin, N)` : C'est ici que le module numpy intervient. Pour tracer correctement une fonction, il va nous falloir beaucoup de points qu'il est hors de question de rentrer à la main comme dans l'exemple précédent. La fonction `np.linspace(debut, fin, nombre)` permet de créer une liste de `N` nombres qui commencent à la valeur `debut` et s'arrête à la valeur `fin` et uniformément répartis.  
  De plus, si on fait une opération sur cette liste comme par exemple multiplier par 2, alors cette opération sera automatiquement appliquée à chaque terme de la liste (ce qui n'est pas vrai si on utilise une liste classique).  
  Par exemple, traçons la fonction définie par y = 2x²+3x-4 entre -2 et 2 en utilisant 100 points :
  @[Exemple d'utilisation de plot]({"stubs": ["Maths/plot2.py"], "command": "python3 Maths/plot2_Test.py"})
  Amusez vous à modifier la fonction, les bornes et le nombre de points (par exemple 10) utilisés pour bien comprendre le fonctionnement.
  
+ `plt.axis(x_min, x_max, y_min, y_max)` : Cette fonction permet de modifier les axes du repère qui sera affiché. Si on ne l'utilise pas, le choix des axes sera fait automatiquement mais des fois ce choix n'est pas pertinent et il faudra donc le modifier avec cette fonction. Les deux premières valeurs qu'on donne sont les valeurs minimale et maximale pour l'axe des abscisses et les deux suivantes sont celles pour l'axe des ordonnées.

+ `plt.grid()` : Affiche un quadrillage en plus sur notre repère.

## Tracé de fonctions plus complexes

Supposons qu'on veuille tracer des fonctions faisant intervenir autre chose que les opérations +, -, \*, / et ** comme par exemple des cosinus, sinus, exponentielle, logarithme... Dans ce cas on ne peut pas faire exactement comme dans l'exemple précédent.

+ Une première façon de faire est de créer "à la main" la liste des y correspondants aux x c'est à dire créer une liste composée des f(x) pour x dans la liste des abscisses.  
  Par exemple si on veut tracer la fonction y = cos(x) + 3 sin(2x) entre -4 et 4, on pourra faire ainsi :
  @[Tracé de y = cos(x) + 3 sin(2x)]({"stubs": ["Maths/plot3.py"], "command": "python3 Maths/plot3_Test.py"})
  
+ Une seconde méthode consiste à utiliser les fonctions classiques modifiées contenues dans numpy (en écrivant np.cos pour le cosinus par exemple). Pourquoi modifiées? Car elles s'appliquent directement à toute la liste.  
  Si on garde le même exemple de fonction y = cos(x) + 3 sin(2x) entre -4 et 4, cela donnera :
  @[Tracé de y = cos(x) + 3 sin(2x)]({"stubs": ["Maths/plot4.py"], "command": "python3 Maths/plot4_Test.py"})

## Tracé de plusieurs fonctions

Pour tracer plusieurs fonctions dans un même repère, il suffit de tracer plusieurs fois une fonction... Elles seront automatiquement dans le même repère.  
Par exemple, si je veux vérifier graphiquement que l'équation de droite y = -2x + 3 que j'ai obtenu correspond bien à l'équation de la tangente en 1 de la fonction y = x² - 4x + 4, il suffira d'écrire : 
@[Vérification graphique]({"stubs": ["Maths/plot5.py"], "command": "python3 Maths/plot5_Test.py"})

Voici un autre exemple où on trace une famille de fonction y=cos(nx) avec n allant de 1 à 4 :
@[Famille de fonctions]({"stubs": ["Maths/plot6.py"], "command": "python3 Maths/plot6_Test.py"})
On en a profité pour rajouter une légende pour que le graphique soit plus compréhensible. Pour cela, il faut rajouter un label dans la fonction `plot` et la fonction `plt.legend()` dans laquelle on précise sa position (ici en bas à droite).  
On remarquera aussi que nous avons utilisé `np.pi` qui est tout simplement la constante pi qui est donc disponible aussi dans le module numpy.

## Tracé de diagrammes en bâtons et histogrammes

On peut tracer assez facilement à partir de séries statistiques des diagrammes en bâtons et des histogrammes. Voici un exemple de chaque :

+ Pour les diagrammes en bâtons, on utilise la fonction `bar(valeurs,effectifs)`.
  @[Diagramme en bâtons]({"stubs": ["Maths/plot7.py"], "command": "python3 Maths/plot7_Test.py"})

+ Pour les histogrammes, on utilise la fonction `hist(liste,[n])` qui trace l'histogramme de la liste répartie en n groupes(si n est précisé).
  Par exemple si on lance deux dés au hasard et qu'on fait leur somme  et qu'on répète 1000 fois ceci. On peut tracer l'histogramme des résultats en écrivant :
  @[Histogramme]({"stubs": ["Maths/plot8.py"], "command": "python3 Maths/plot8_Test.py"})

## Affichages de nuages de points

Pour tracer des points, il suffit d'utiliser la fonction `plt.scatter(abscisses, ordonnées)` où `abscisses` est la liste des abscisses des points qu'on veut tracer et `ordonnées` la liste des ordonnées.  
Par exemple si on veut placer les points (1,2), (3,3), (2,1) et (1,3) :
@[Nuage de points]({"stubs": ["Maths/plot9.py"], "command": "python3 Maths/plot9_Test.py"})

## Pour aller plus loin

Ce qui a été présenté ici n'est qu'une infime partie des possibilités de matplotlib. 
Parmi les choses que nous n'avons pas abordées, voici quelques points qui peuvent être intéressants à regarder :
+ Toutes les options de plot : le changement de couleur, de façon de tracer la courbe, de rajouter des points sur ces courbes, d'annoter la courbe.
+ La gestion des axes et des grilles. On peut améliorer nettement la présentation en modifiant les paramètres pour obtenir ce que l'on souhaite.
+ L'affichage de plusieurs graphiques dans plusieurs repères.
+ D'autres types de graphes comme les graphiques en 3D, en camembert, champs de vecteurs etc.
+ ...

# Bac à sable

Voici une fenêtre vide que vous pouvez utiliser pour faire les exercices qui suivent ou tout simplement essayer de nouvelles choses en utilisant matplotlib.

@[Bac à sable]({"stubs": ["Maths/bac_a_sable.py"], "command": "python3 Maths/bac_a_sable_Test.py"})


# Entrainement 

Comme il n'y a pas réellement de vérifications possibles sur le graphique obtenu, tous les exercices qui suivent pourront être résolus dans la fenêtre du bac à sable mis à disposition dans la section précédente.

### Exercice 1

Afficher la représentation graphique de la fonction $`y = x^3 + 3x^2-9x+1`$ pour x entre -2 et 4.

---

### Exercice 2

Afficher la représentation graphique de la fonction $`y = 3 \cos(2x) - 2 \sin(3x)`$ entre $`-\pi`$ et $`\pi`$.

---

### Exercice 3

Afficher les représentations graphiques de la famille de fonctions $`y= \dfrac{1-nx}{x-1}`$ pour n allant de -3 à 3. On se placera dans un repère allant de -2 à 4 pour les abscisses et de -8 à 8 pour les ordonnées. On fera apparaitre aussi une légende en haut à gauche. 
