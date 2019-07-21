# Les classes en python

Le but de cette page est de présenter un peu le fonctionnement des classes en python. Il existe déjà beaucoup de très bons cours par ailleurs, on va plutôt voir ici comment le mettre en place dans un cas particulier relativement complet : les fractions.  Cet exemple m'a semblé riche à la fois informatiquement et mathématiquement car c'est toujours bon de se replonger dans les fondements des notions qu'on connait depuis très longtemps pour encore mieux les comprendre.

Bien sûr, il existe déjà un module fractions en python très bien fait. Nous allons ici reconstruire petit à petit un équivalent.

Une remarque pratique : Si vous appuyez sur une des barres Run, des tests sur votre code vont être faits en fonction de la partie où vous êtes. Seule la première barre Run est libre donc si vous voulez tester des choses librement, c'est la première qu'il vaut mieux utiliser.

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

Pour cela il faut remplacer la fonction `__str__` pour qu'elle renvoie ce que l'on veut. Il semble assez naturel d'afficher une fraction sous la forme "numerateur / denominateur" (avec un espace entre pour mieux voir).

Créer en dessous de la fonction `__init__` une fonction `__str__(self)` qui renvoie le texte sous la forme "numerateur / denominateur" (avec un espace entre pour mieux voir). Pour récupérer le numérateur et dénominateur de `self`, il suffira de taper `self.num` et `self.den`.

Appuyer sur Run ci-dessous pour tester votre code.

@[Définition d'une classe 2]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/affichage_Test.py", "layout": "aside"})
