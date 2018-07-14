<h1> <center>Cours : Module math</center></h1>

Avant de présenter à proprement parler le module math de Python, nous allons voir quelques fonctions liées aux mathématiques mais accessibles sans importer aucun module.

# Première partie : Les fonctions mathématiques de base

Voici quelques fonctions qui peuvent être utiles :
+ `int(x)` : Permet de faire disparaitre la partie décimale de x pour ne garder que la partie entière. Par exemple `int(3.57)` vaut 3 et `int(-4.876)` vaut -4. Attention : pour les nombres négatifs `int` est différent de la partie entière.
+ `abs(x)` : Permet de faire disparaitre le signe de x. Par exemple `abs(3.65)` vaut 3.65 et `abs(-4.3)` vaut 4.3.
+ `round(x,n)` : Donne l'arrondi de x avec n chiffres après la virgule. Par exemple `round(12.345678,3)` vaut 12.345.
+ `min(a,b)` et `max(a,b)` : Donnent respectivement le plus petit et le plus grand des nombres entre a et b


# Deuxième partie : Les fonctions du module math


  
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



