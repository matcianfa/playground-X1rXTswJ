# Les classes en python

Le but de cette page est de présenter un peu le fonctionnement des classes en python. Il existe déjà beaucoup de très bons cours par ailleurs, on va plutôt voir ici comment le mettre en place dans un cas particulier relativement complet : les fractions.  Cet exemple m'a semblé riche à la fois informatiquement et mathématiquement car c'est toujours bon de se replonger dans les fondements des notions qu'on connait depuis très longtemps pour encore mieux les comprendre.

Bien sûr, il existe déjà un module fractions en python très bien fait. Nous allons ici reconstruire petit à petit un équivalent.

Une remarque pratique : Si vous appuyez sur une des barres Run, des tests sur votre code vont être faits en fonction de la partie où vous êtes. Seule la première barre Run est libre donc si vous voulez tester des choses librement, c'est la première qu'il vaut mieux utiliser. De plus, n'hésitez pas à agrandir la fenetre (en haut à droite de l'éditeur) pour mieux voir.

## Définition d'une classe

Pour définir une classe, on commence par écrire `class <nom de la classe> :` et tout ce qui fait partie de la classe (fonctions, variables etc.) devra être écrit en dessous et indenté (exactement comme lorsqu'on définit une fonction par exemple).

Ensuite, chose indispensable à faire, il faut définir ce que doit faire python lorsqu'on crée un élément de notre classe. Pour cela il faudra ***toujours*** définir une fonction `__init__`. C'est la fonction qui sera lancée lorsqu'on appellera notre classe. Il faudra toujours rajouter en premier la variable `self` (et ce sera le cas pour toutes les fonctions de notre classe) pour pouvoir l'utiliser sur les éléments de notre classe. On verra dans la suite plus en détail l'utilité de `self`. 

Dans le cas de nos fractions, on veut définir une classe `Fraction`. Une fraction $`\dfrac{a}b`$ est composée d'un numérateur $`a`$ et d'un dénominateur $`b`$. On va donc définir deux attributs pour toutes les fractions qui seront `num` et `den`(pour aller plus vite) qui correspondront respectivement au numérateur et au dénominateur. Vous pouvez voir ce que cela donne dans le code déjà prérempli ci-contre.

A vous maintenant de compléter ce code pour voir comment utiliser ces attributs :

- Commencons par créer notre première fraction ($`\dfrac 3 4`$ par exemple) et appellons la `frac`. Pour cela il suffit de taper `frac = Fraction(3,4)` (sans indentation, cela ne fait pas partie de notre classe).
- Et maintenant, affichons son dénominateur : Pour cela, rien de plus simple, il suffit d'écrire `print(frac.den)`. Appuyez sur Run ci-dessous pour lancer le script. Il devrait s'afficher en dessous 4.

On peut peut-être commencer à voir l'utilité de `self` dans la classe. Cela permet de donner un nom à l'élément de la classe à qui on applique la fonction.

@[Définition d'une classe]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/Classe.py", "layout": "aside"})

## Affichage d'une classe

Essayez d'afficher la variable `frac` en tapant `print(frac)` et en appuyant sur Run ci-dessus. On s'attendrait à voir s'afficher quelque chose comme (3,4) ou 3 4 ou 3/4 mais au lieu de ça, on a quelque chose comme `<Classe.Fraction object at 0x7f03401f2e50>`. Ce que renvoie Python est en fait assez naturel : une classe peut être très complexe et comment choisir quelle information renvoyer ? Python fait le choix de base de dire où se trouve l'objet de la classe. Si on veut qu'il affiche autre chose, il suffit de lui expliquer.

Pour cela il faut remplacer la fonction `__str__` pour qu'elle renvoie ce que l'on veut. Il semble assez naturel d'afficher une fraction sous la forme "numerateur / denominateur" (avec un espace entre pour mieux voir). Attention au nom de la fonction : il faut 2 tirets _ avant et après. C'est la norme pour les fonctions de base d'une classe (qui existent déjà et que nous remplaçons pour qu'elle fasse ce que l'on souhaite).

Créer en dessous de la fonction `__init__` une fonction `__str__(self)` qui renvoie le texte sous la forme "numerateur / denominateur" (avec un espace entre pour mieux voir). Pour récupérer le numérateur et dénominateur de `self`, il suffira de taper `self.num` et `self.den`.

Appuyer sur Run ci-dessous pour tester votre code.

@[ ]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/affichage_Test.py", "layout": "aside"})

## Création d'une fonction de classe

Maintenant que nos fractions s'affichent correctement et avant de s'attaquer aux opérations entre fractions, il va falloir s'intéresser à comment les réduire. Pour cela, on sait que pour réduire une fraction, il suffit de diviser le numérateur et le dénominateur par le pgcd des deux. Pour obtenir le pgcd, on utilisera la fonction `gcd` du module `math` qu'on pourra importer au tout début du script en écrivant `from math import gcd`.  
(Petite remarque : pour utiliser `math.gcd`, il faut être en python 3.5 minimum. Ce qui veux dire que si vous voulez utiliser votre classe Fraction avec EduPython, il faut créer votre propre fonction `gcd`, avant votre class)

Créez maintenant une fonction `reduire(self)` qui renvoie tout simplement la fraction réduite de notre fraction.

Remarque : Pas besoin de mettre des tirets _ au nom car c'est une fonction qu'on crée nous et ne remplace aucune fonction déjà existante de base pour une classe. Par contre le self est indispensable quand on définit la fonction mais pour l'appeller, il suffira d'écrire  `frac.réduire()` pour l'appliquer à une Fraction `frac`.

::: Aide
Dans le cas où cela n'est pas encore tout à fait claire :  
Il suffit de renvoyer `Fraction(self.num//gcd(self.num,self.den) , self.den//gcd(self.num,self.den))`.  
Formule qu'on peut bien sûr améliorer en ne calculant qu'une fois le PGCD...
:::

Remarque supplémentaire : En simplifiant, on peut se retrouver avec des fractions de la forme 4/1. Il serait plus naturel de n'afficher que 4. Modifiez donc, en plus, la fonction `__str__` pour qu'elle affiche seulement le numérateur lorsque le dénominateur est 1.

Testez votre code en appuyant sur Run ci-dessous.

@[ ]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/reduire_Test.py", "layout": "aside"})

## Retour sur le constructeur `__init__`

Revenons un peu sur la façon de construire un élément de notre classe. Au début on a simplement créé une fonction `__init__` qui permet, lorsqu'on écrit `Fraction(2,3)` de créer un élément ayant 2 attributs : un qui s'appelle `num` et qui ici vaut 2 et une qui s'appelle `den` et qui prend la valeur 3. Mais notre fonction `__init__` peut être beaucoup plus complexe et créer des attributs après de longues lignes de code.

Pour expérimenter cela, on va s'intéresser au signe de notre fraction. On sait que $`-\dfrac 23 = \dfrac{-2}3 = \dfrac{2}{-3}`$. Donc pour simplifier les choses et éviter de voir s'afficher des fractions sous la forme "2 / -3" ou "-2 / -3", on va systématiquement mettre le signe - (s'il y est encore après simplification) au numérateur et cela dès la création de la Fraction c'est à dire dans la fonction `__init__`.

De plus, il est impossible de créer une fraction ayant un 0 comme dénominateur donc si c'est le cas, on va lever une exception. Pour cela il suffit d'écrire `raise ZeroDivisionError` pour que s'affiche un beau message rouge lorsqu'on met 0 en dénominateur.

@[ ]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/signes_Test.py", "layout": "aside"})


## Egalités

Maintenant que nous avons nos fractions bien définie, on va s'intéresser aux cas d'égalité. En effet, si on teste le script suivant :
```python
a = Fraction(1,2)
b = Fraction(1,2)
print(a==b)
```
On a la fraction $`\dfrac 1 2`$ dans la variables `a` et `b` donc on s'attendrait à voir s'afficher `True` mais malheureusement, il apparait `False`. C'est tout à fait logique : pour nous les fractions sont les mêmes mais pour python ce sont deux objets différents (imaginez qu'au lieu de faire une classe Fraction, on ait fait une classe Voiture. Si on crée 2 voitures (même identiques) ce ne sont pas a priori les mêmes. Il faut donc expliquer ce que python doit comprendre par deux Fractions égales.

Pour cela, il suffit de modifier la fonction `__eq__(self,fraction2)` comme on a fait pour `__init__` et `__str__`.

Créez une fonction `__eq__(self,fraction2)` qui permette de dire quand les Fractions `self` et `fraction2` sont égales (au sens des fractions c'est à dire que 1/2 = 2/4 = 3/6...).

Rappel : $`\dfrac ab =\dfrac cd `$ si et seulement si $`ad=bc`$.

Appuyer sur Run ci-dessous pour tester votre code.

@[ ]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/egalite_Test.py", "layout": "aside"})

## Inégalités

Tant qu'on y est, expliquons ce que doit comprendre Python lorsqu'on écrit `Fraction(1,3)<Fraction(1,2)`.

Pour l'inégalité strict < il suffit de modifier la fonction `__lt__(self,fraction2)` (`lt`pour lower than). Pour l'inégalité large <=, il faut modifier la fonction `__le__(self,fraction2)`. Pas besoin de redéfinir (mais on pourrait) les fonctions pour > et >= car elles sont automatiquement déduites des deux précédentes tout comme != se déduite de ==.

Créez la fonction `__lt__(self,fraction2)` (resp. `__le__(self,fraction2)`) qui renvoie True si la Fraction `self` est strictement inférieure (resp. inférieure ou égale)  à `fraction2` et False sinon.

Rappel : Si $`bd>0`$ , on a $`\dfrac ab <\dfrac cd `$ si et seulement si $`ad<bc`$.

Appuyer sur Run ci-dessous pour tester votre code.

@[ ]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/inegalite_Test.py", "layout": "aside"})

## Les opérations

Attaquons nous maintenant à ce qui a traumatisé des générations d'élèves : l'addition de fractions !

On voudrait que lorsqu'on tape "Fraction(1,3)+Fraction(1,3)" on obtienne Fraction(2,3). Pour cela, rien de plus simple, il suffit de modifier la fonction `__add__(self,fraction2)`. 

Je rappelle la formule : $`\dfrac ab + \dfrac cd = \dfrac{ad+bc}{bd}`$. Tant qu'à faire, on peut afficher le résultat sous forme réduite. Cela donnerait pour l'addition :
```python

```
