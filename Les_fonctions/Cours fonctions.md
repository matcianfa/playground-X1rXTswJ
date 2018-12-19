<h1> <center>Cours : Compléments sur les fonctions</center></h1>

# Fonctions récursives
Une fonction récursive est tous simplement une fonction qui s'appelle elle même.  
Prenons un exemple : Le calcul de la somme des entiers entre 1 et n.  
L'idée est d'expliquer comment il faut commencer et ce qu'il faut faire pour passer de l'étape n-1 à l'étape n. Python s'occupe du reste.  
Pour commencer, si n vaut 1, la somme vaut 1. Ensuite si j'ai déjà calculé la somme de 1 à n-1, il suffit de lui ajouter n pour obtenir la somme de 1 à n. Cela donnerait le programme suivant :
```python
def somme(n):
    if n==1:
        return 1
    else :
        return somme(n-1)+n
```
Détaillons ce qu'il se passe lorsqu'on le lance :
1. Pour calculer somme(3) :  
   3 ne vaut pas 1 donc on exécute le else. On renvoie somme(2)+3. mais comme on ne connait pas encore somme(2), on met le calcul en mémoire le temps de le calculer.
2. On exécute somme(2) : comme 2 ne vaut pas 1 donc on exécute le else. On renvoie somme(1)+2. mais comme on ne connait pas encore somme(1), on met de calcul en mémoire le temps de le calculer.
3. On exécute somme(1) : comme 1 == 1, on renvoie 1.
4. Maintenant qu'on connait le résultat de somme(1), on peut calculer somme(1)+2. de l'étape 2 ce qui nous donne 3 comme valeur pour somme(2).
5. Maintenant qu'on connait le résultat de somme(2), on peut calculer somme(2)+3. de l'étape 1 ce qui nous donne 6 comme valeur pour somme(3). Comme c'était la valeur demandée initialement, le programme renvoie 6.  
Comme on peut le voir les calculs effectués sont plus long à expliquer que le programme en lui même. C'est l'intérêt d'une écriture récursive : c'est l'ordinateur qui a à gérer la complexité de ce qu'il se passe, nous on a juste à lui expliquer comment passer d'une étape à l'autre.  
### Les pièges :
+ Ne pas oublier d'initialiser c'est à dire d'expliquer ce que doit faire le programme pour les valeurs initiales. Si on n'explique pas dans notre exemple quoi fait si n==1 alors le programme va chercher à calculer somme(1) puis somme(0) puis somme(-1) puis ... sans jamais s'arrêter.
+ Lui demander des calculs trop complexes. L'avantage d'une écriture récursive est que c'est en général simple de notre coté mais pas forcément pour l'ordinateur. Cela veut dire qu'il faut quand même se demander si ce qu'on lui demande ne va pas être trop complexe et s'il n'y a pas des moyen de lui simplifier la tache. On verra dans les exercices quelques exemples.
+ En python, de base, on ne peut faire que 1000 appels de la même fonction de façon récursive c'est-à-dire que dans mon exemple, je ne pourrais pas calculer somme(1001). Il est possible de modifier cette valeur en rajoutant ceci en tout début :
  ```python
  import sys
  sys.setrecursionlimit( la_valeur_que_je_veux)
  ```
  Attention cependant, quand on a le message d'erreur comme quoi on a dépassé la limite possible cela signifie souvent qu'on a oublié une initialisation (voir le premier piège).
        
# Compléments : Les variables locales et globales.
La chose importante à comprendre sur les variables est : Toutes les variables que l'on crée et utilise à l'intérieur d'une fonction n'existent qu'à l'intérieur de cette  fonction.  
Par exemple si je lance ceci :
```python runnable
def fonction(n):
    a=n+1
fonction(3)
print(a)
```
J'obtiendrais que a n'existe pas. Le a à l'intérieur de la fonction est ce qu'on appelle une variable locale qui n'existe que dans la fonction pas en dehors.  
Encore pire :
```python runnable
a=18
def fonction(n):
    a=n+1
fonction(3)
print(a)
```
Dans ce cas, le `print(a)` affichera 18 bien que dans la fonction, a prenne la valeur 3+1. Python différencie donc les variables globales (comme le a qui vaut 18) des variables locales (le a qui prend les valeurs n+1 de la fonction)
Il existe cependant un moyen de modifier une variable globale à l'intérieur d'une fonction. Il faut rajouter une ligne au début de la fonction avec `global` suivi des nombres des variables globales qu'on voudra modifier dans la fonction. Par exemple :
```python runnable
a=18
def fonction(n):
    global a
    a=n+1
fonction(3)
print(a)
```
Cette fois ci le `print(a)` affichera 4 car le `a` modifié par la fonction est la variable globale.
Les variables globales vous serviront donc à stocker les informations qui servent pour plusieurs fonctions par exemples alors que les locales servent pour les calculs intermédiaires qui peuvent être oubliés après.


