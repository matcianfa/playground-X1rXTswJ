<h1> <center>Compléments sur les boucles</center></h1>


# Première partie : 



# Deuxième partie : 


# Troisième partie : QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
x = 2
if x <= -1 : 
    print(2*x+1)
elif x <=3 :
    print(-x+2)
else :
    print(2*x-5)
```  
?[Que va afficher ce programme ? ]
-[ ] -x+2
-[x] 0
-[ ] 5
-[ ] -1

---

###### QCM 2
```python
if ... :
    print("a est nul")
```  
?[Que faut-il mettre à la place des ... pour que s'affiche "a est nul" lorsque a vaut 0 ?]
-[ ] a=0
-[ ] a != 0
-[ ] a%0
-[x] a==0

---

###### QCM 3
```python
if ... :
    print("a est non nul")
```  
?[Que faut-il mettre à la place des ... pour que s'affiche "a est non nul" lorsque a ne vaut pas 0 ?]
-[ ] a/=0
-[x] a != 0
-[ ] a%0
-[ ] a<>0

---

###### QCM 4
?[Cochez les cases qui correspondent à des conditions vraies]
-[x] 3>2 and 1<=5
-[ ] 3>2 and 1>=5
-[ ] 3<2 and 1>=5
-[ ] 3<2 and 1<=5
-[x] 3>2 or 1<=5
-[x] 3>2 or 1>=5
-[ ] 3<2 or 1>=5
-[x] 3<2 or 1<=5
-[ ] not 3>2
-[x] not 1>=5

# A vous !

###### Exercice 1 : Calcul de l'inverse d'un nombre

Ecrire un programme qui prend en entrée un nombre ***x*** et qui renvoie "Impossible" si ***x*** est nul et le resultat de 1/***x*** sinon.

Quand on demande d'afficher, c'est avec `print`.

@[Calcul de l'inverse d'un nombre]({"stubs": ["Les_conditions/Inverse.py"], "command": "python3 Les_conditions/Inverse_Test.py"})

---

###### Exercice 2 :

Ecrire un programme qui prend en entrée une température ***t*** et qui affiche l'état de l'eau à cette température c'est à dire "SOLIDE", "LIQUIDE" ou "GAZEUX". 

On prendra comme conditions les suivantes : 
- Si la température est strictement négative alors l'eau est à l'état solide.
- Si la température est entre 0 et 100 (compris) l'eau est à l'état liquide.
- Si la température est strictement supérieure à 100.

> Entrée : Une température ***t***.

> Sortie : L'état de l'eau à cette température parmi les trois possibilités : "SOLIDE", "LIQUIDE" ou "GAZEUX".

Quand on demande d'afficher, c'est avec `print`.

@[Afficher le plus grand des deux]({"stubs": ["Les_conditions/Etat_eau.py"], "command": "python3 Les_conditions/Etat_eau_Test.py"})

---



