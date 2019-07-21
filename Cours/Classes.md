# Les classes en python

Le but de cette page est de présenter un peu le fonctionnement des classes en python. Il existe déjà beaucoup de très bons cours par ailleurs, on va plutôt voir ici comment le mettre en place dans un cas particulier relativement complet : les fractions.  Cet exemple m'a semblé riche à la fois informatiquement et mathématiquement car c'est toujours bon de se replonger dans les fondements des notions qu'on connait depuis très longtemps pour encore mieux les comprendre.

Bien sûr, il existe déjà un modules fractions en python très bien fait. Nous allons ici reconstruire petit à petit un équivalent que nous mettrons dans un module nommé mes_fractions. Je le précise pour expliquer pourquoi il y a `from mes_fractions import Fraction` : cela permet d'importer ce qu'on a fait avant entre chaque fenêtre.

## Définition d'une classe

Pour définir une classe, on commence par écrire `class <nom de la classe> :` et tout ce qui fait partie de la classe (fonctions, variables etc.) devra être écrit en dessous et indenté (exactement comme lorsqu'on définit une fonction par exemple).

Ensuite, chose indispensable à faire, il faut définir ce que doit faire python lorsqu'on crée un élément de notre classe. Pour cela il faudra ***toujours*** définir une fonction `__init__`.

Dans notre cas, on veut définir 

@[Définition d'une classe]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/Classe_Test.py", "layout": "aside"})

@[Définition d'une classe 2]({"stubs":["Cours/Classe.py"], "command": "python3 Cours/Classe_Test.py", "layout": "aside"})
