<h1> <center>Cours : Le module math</center></h1>

Avant de présenter à proprement parler le module math de Python, nous allons voir quelques fonctions liées aux mathématiques mais accessibles sans importer aucun module.

# Première partie : Les fonctions mathématiques de base

Voici quelques fonctions qui peuvent être utiles :
+ `int(x)` : Permet de faire disparaitre la partie décimale de x pour ne garder que la partie entière. Par exemple `int(3.57)` vaut 3 et `int(-4.876)` vaut -4. Attention : pour les nombres négatifs `int` est différent de la partie entière.
+ `abs(x)` : Permet de faire disparaitre le signe de x. Par exemple `abs(3.65)` vaut 3.65 et `abs(-4.3)` vaut 4.3.
+ `round(x,n)` : Donne l'arrondi de x avec n chiffres après la virgule. Par exemple `round(12.345678,3)` vaut 12.345.
+ `min(a,b)` et `max(a,b)` : Donnent respectivement le plus petit et le plus grand des nombres entre a et b


# Deuxième partie : Les fonctions du module math

## Importation de modules
Commençons par parler de modules. Il existe de nombreuses fonctions qu'on peut utiliser avec Python mais pour éviter de saturer à la fois la mémoire et les noms de fonctions utilisables, on a regroupé dans ce qu'on appelle des modules, les fonctions qui ont une utilité spécifique. Pour les utiliser il faut donc demander à Python de les mettre en mémoire pour pouvoir les utiliser. Pour cela, il faut mettre en début de programme les modules qu'on importe.   
Pour simplifier, on va systématiquement importer : 
- soit une fonction spécifique en tapant `from nom_du_module import nom_de_la_fonction`.
- soit tout le module directement en tapant `from nom_du_module import *`. 

Par exemple : Pour importer uniquement la fonction cosinus (qui s'appelle cos en python) du module math, on ecrira en début de programme : `from math import cos`.  
Pour importer tout le module math pour utiliser directement toutes les fonctions qu'on va voir après, on écrira `from math import *`.

Remarque : On verra plus tard d'autres façons d'importer des modules voire d'en créer pour se faire une boite à outils par exemple de fonctions qu'on utilise souvent.

## Présentation des fonctions du module math

On ne va présenter ici que les fonctions utiles au lycée. On pourra trouver la liste complète du module math [ici](https://docs.python.org/fr/3.6/library/math.html#module-math)

+ `sqrt(x)` : Donne la racine carrée de x. On a déjà vu qu'on pouvait l'obtenir en tapant `x**0.5` qui a l'avantage de ne pas demander d'importer le module math mais les puristes préfère peut-être celle ci.
+ `cos(x)`, `sin(x)` et `tan(x)` : Donnent respectivement le cosinus, le sinus et la tangente de x **lorsque x est en radians**. Il faut donc convertir l'angle en radian avant (avec la fonction qui suit par exemple).
+ `radians(x)` : Convertit l'angle x des degrés en radians.
+ `acos(x)`, `asin(x)`, `atan(x)` : Donnent respectivement l'arccos, l'arcsin et l'arctan de x en radians.
+ `exp(x)`, `log(x)` :  Donne l'exponentielle et le logarithme népérien de x. Si on veut le logarithme en base b, il suffit de taper log(x,b).
+ `pi` : Donne la valeur de pi avec la meilleure précision disponible.
+ `e` : Donne la valeur de la constante d'Euler (ou de Neper) e avec la meilleure précision disponible.
+ `inf` : Donne l'équivalent informatique de l'infini c'est à dire que inf est plus grand que n'importe quel nombre. Il est très pratique pour initialiser des variables qu'on veut minimiser par exemple.

Voyons quelques exemples d'utilisation (Appuyer sur Run pour voir le résultat) : 
1. Calcul de la racine carrée de pi :
   ```python runnable
   from math import *
   
   a=sqrt(pi)
   print(a)
   ```
1. Calcul du cosinus d'un angle :
   ```python runnable
   from math import *
   
   angle = 60 
   angle_en_radian = radians(angle) # On convertit l'angle en radian
   c= cos(angle_en_radian) 
   print(c)
   
   # On aurait pu écrire aussi directement : 
   print(cos(radians(angle)))
   ```
1. Calcul de l'arrondi de pi² à 5 chiffres après la virgule en n'important que pi du module math :



  
# Troisième partie : QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
a=5
b=a-2
print(a*b)
```  
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] -10
-[x] 15
-[ ] 23
-[ ] 3
-[ ] 8

---

###### QCM 2
```python
a=5
a=a-2
a=a*a+1
print(a)
```  
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 16
-[ ] 26
-[ ] 12
-[x] 10

---

###### QCM 3
```python
a=7
b=a-1
print((b/2)**2)
```
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 6.0
-[ ] 1.5
-[x] 9.0
-[ ] -0.25  

---

##### QCM 4
```python
a=3
b=a+1
print((a**2+b**2)**0.5)
```
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[x] 5.0
-[ ] 13.0
-[ ] 12.5
-[ ] 7.0

---

###### QCM 5
```python
a=22
b=5
print((a//b)+(a%b))
```
?[Quelle valeur sera affichée si on execute le programme ci-dessus ? ]
-[ ] 6.4
-[ ] 4.4
-[x] 6
-[ ] 114.4 

# A vous !

###### Exercice 1 :

Le but de cet exercice est de suivre un programme de calcul en partant d'un entier ***n*** qui sera donné automatiquement.

Appuyez sur Run et suivez les instructions qui s'affichent.

N'effacez pas ce que vous avez fait juste. Il faut rajouter au fur et à mesure en dessous.

Quand on demande d'afficher, c'est avec `print`.

@[Programme de calcul]({"stubs": ["Variables_et_fonctions/Programme_calcul.py"], "command": "python3 Variables_et_fonctions/Programme_calcul_Test.py"})

---

###### Exercice 2 :

La consigne de cet exercice est identique au précédent.

Appuyez sur Run et suivez les instructions qui s'affichent.

N'effacez pas ce que vous avez fait juste. Il faut rajouter au fur et à mesure en dessous.

Quand on demande d'afficher, c'est avec `print`.

@[Programme de calcul]({"stubs": ["Variables_et_fonctions/Programme_calcul1.py"], "command": "python3 Variables_et_fonctions/Programme_calcul1_Test.py"})

---



