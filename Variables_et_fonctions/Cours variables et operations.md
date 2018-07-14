# Cours : Variables et opérations

## Première partie : Les variables

Une variable en informatique permet de garder en mémoire (le temps que le programme s'exécute) des données comme par exemple le résultat d'un calcul ou un mot, une liste ou bien d'autres choses.  
Pour stocker en mémoire une valeur dans une variable, on utilise simplement le signe égal =.  
Par exemple : 
```python
a=3
b=7
c=b+a+2
```
Dans cet exemple, on a mis en mémoire 3 variables. Dans a, on a stocké la valeur 3, dans b la valeur 7 et dans c la valeur 12. Remarque importante : ce qui est stocké est le résultat du calcul et non le calcul. Ce qui veut dire que si on modifie la valeur de a, la variable c elle restera à 12.

Pour afficher la valeur d'une variable, on utilise la fonction `print`. Appuyez sur le bouton Run pour voir l'effet du code ci-dessous :
```python runnable
a=3
b=7
c=b+a+2
print(c)
```
On voit s'afficher la valeur de c. 

## Deuxième partie : Les opérations sur les variables numériques

Dans cette partie, nous allons voir les opérations de base que l'on peut effectuer en python sur des nombres.

+ Il y a bien sur les quatre opérations classiques +, -, \*, / avec les priorités opératoires habituelles. Par exemple :
  ```python runnable
  a=5
  b=3
  print(a+b)
  print(a-b)
  print(a*b)
  print(a/b)
  ```
+ Les deux autres opérations qu'on utilise couramment sont les puissances et la racine carrée.  
  - Pour les ***puissances***, on double simplement la multiplication. Ainsi $`x^n`$ s'obtiendra en écrivant `x**n`.  
  - Pour la ***racine carrée***, on va simplement utiliser une propriété mathématique : $`\sqrt x = x^{0.5}`$. Donc pour calculer la racine carrée d'un nombre x, il suffit d'écrire `x**0.5`.  
  Voici quelques exemples. On a rajouté des commentaires à coté des instructions d'affichage des calculs pour que ces instructions soient plus claires. Pour écrire un commentaire, il suffit de mettre un # devant. Tout ce qui suit le # ne sera pas executé par l'ordinateur et ne sert donc qu'à la personne qui lit le programme.
  ```python runnable
  print(2**3) # Affiche le résultat de 2 puissance 3
  print(3**2) # Affiche le résultat de 3 puissance 2
  print(9**0.5) # Affiche la racine carrée de 9
  print(2**0.5) # Affiche la racine carrée de 2
  ```

+ On peut aussi réaliser facilement des divisions euclidiennes (c'est à dire les divisions posées comme au primaire). 
  - Pour obtenir le ***quotient*** de la division de a par b, il suffit d'écrire `a//b`.
  - Pour obtenir le ***reste*** de la division de a par b, il suffit d'écrire `a%b`.  
  Remarque : La différence entre `a/b`et `a//b`est que le premier donne une valeur approchée décimale à 16 chiffres après la virgule alors que la deuxième nous donne l'***entier*** q tel que 0 <= a-bq < b.  
  Voici quelques exemples que vous pouvez modifier pour vérifier que vous avez bien compris.
  ```python runnable
  a=17
  b=3
  print(a//b) # Affiche le quotient de la division euclidienne de a par b
  print(a%b) # Affiche le reste de la division euclidienne de a par b
  ```
  Remarque : Même si ces opérations sont finalement assez peu utilisée en cours de mathématiques, elles le sont beaucoup plus en informatique, principalement le calcul du reste de la division euclidienne. Par exemple pour déterminer si un nombre est pair, il suffit de regarder si `x%2` vaut 0. En effet, un nombre est pair si et seulement si son reste par la division par 2 est nul. On l'utilisera régulièrement dans les exercices.
  
# Troisième partie : QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

1. ?[Quelle valeur sera affichée si on execute le programme ci dessous ?  
```python
a=5
b=a-2
print(a*b)
``` 
]
-[ ] -10
-[x] 15
-[ ] 23
-[ ] 3
-[ ] 8


  
