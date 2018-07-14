# Cours : Variables et opérations

### Première partie : Les variables

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

### Deuxième partie : Les opérations sur les variables numériques

Dans cette partie, nous allons voir les opérations de base que l'on peut effectuer en python sur des nombres.

Il y a bien sur les quatre opérations classiques +, -, \*, /.  
