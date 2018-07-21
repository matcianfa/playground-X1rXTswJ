<h1> <center>Compléments sur les boucles</center></h1>


# Première partie : Les boucles `for` avec autre chose que `range`

On a vu qu'on pouvait faire une boucle sur avec un indice k appartenant à une suite de nombre donnée par range. En réalité, on peut faire une boucle sur n'importe quoi qui peut s'enumérer. On appelle cela un itérateur. Nous n'allons pas rentrer ici dans les détails sur les itérateurs mais juste présenter deux exemples classiques : les listes et les chaines de caractères. Il y a une partie du cours dédiée à chacune de ces notions de base en informatique un peu plus tard. Nous allons juste présenter ici quelques applications simples aux boucles.

## Les chaines de caractères

Une chaine de caractère est tout simplement un texte mis entre guillemet `"`. On en a déjà croisé quand on a parlé de la fonction `print`.

Si à la place de `range` on met une chaine de caractères à énumérer dans une boucle `for`, on va tout simplement prendre chaque lettre l'une après l'autre de cette chaine de caractères.

Prenons un exemple on ne peut plus basique :
```python runnable
for lettre in "Bonjour !":
    print(lettre)
```
En executant on voit que s'affichent successivement les lettres de "Bonjour !".

Autre exemple un peu plus utile, supposons que je veuille compter le nombre de "e" dans un texte, nous pourrions alors écrire ceci :
```python runnable
texte = "Homme libre, toujours tu chériras la mer ! La mer est ton miroir ; tu contemples ton âme Dans le déroulement infini de sa lame, Et ton esprit n'est pas un gouffre moins amer."
compteur=0
for lettre in texte :
    if lettre == "e" :
        compteur += 1
print(compteur)
```
Dans notre boucle, on énumère lettre après lettre de notre texte. Si la lettre est "e", on rajoute 1 à notre compteur. Attention, "E" et "é" sont différents de "e".

## Les listes

Une liste peut contenir de tout : des nombres, des chaines de caratères, des booléens et même d'autres listes... Nous verrons plus en détail les listes dans une autre partie du cours. Nous allons ici présenter des listes simples.

Pour créer une liste *à la main*, il suffit de mettre nos objets entre crochets et les séparer par des virgules : Par exemple [1, "arbre", true] est une liste de 3 éléments : le nombre 1, la chaine de caractère "arbre" et le booléen true. 

On peut énumérer une liste élément par élément avec une boucle `for` tout simplement en remplaçant `range` par la liste que l'on veut énumérer. Par exemple, pour afficher les éléments d'une liste :
```python runnable
liste = [ 1, "arbre", true, 2.564, "Bonjour !"]
for k in liste: 
    print(k)
```

# Deuxième partie : `break`, `continue` et `else`

Il existe deux instructions très utiles qu'on peut utiliser à l'intérieur d'une boucle aussi bien `for` que `while` et qui permettent d'agir sur la boucle pour l'arrêter ou sauter des étapes.

## L'instruction `break`

L'instruction `break` permet d'arrêter une boucle. Par exemple si on cherche quelque chose et dès qu'on l'a trouvé, on peut s'arrêter.

Par exemple, supposons qu'on cherche à savoir si une chaine de caractère contient un "x" ou pas, autrement dit, dès qu'on en a trouvé un, on peut s'arrêter. On pourra le coder ainsi :
```python runnable
texte = "Ceci est un texte, tout ce qu'il y a de plus simple"
for lettre in texte : 
    print(lettre)
    if lettre == "x" :
        print("Un x a été trouvé !")
        break
```
Notre boucle va parcourir lettre à lettre le texte, Dès qu'on trouve une lettre qui vaut "x", on affiche "Un x a été trouvé !" et le `break` arrête la boucle.

## L'instruction `continue`

L'instruction `continue` permet de sauter une étape de la boucle.

Par exemple, supposons que nous voulions afficher l'inverse 1/n de nombres n dans une liste. Si n vaut 0, le calcul 1/n sera impossible, il faudra donc sauter cette étape et passer au nombre suivant. Cela donnerait : 
```python runnable
liste = [ -4, 2, 6, 0, 1, 3, 0, 10]
for n in liste:
    if n==0:
        continue
    print(1/n)
```

## l'instruction `else`

Elle se place en fin de boucle et va de paire avec l'instruction `break`. Tout ce qui est indenté après le `else` ne sera executé que si la boucle s'est terminée entièrement (sans utilisation de `break`)

Par exemple, si je reprends l'exemple de recherche du "x", s'il n'était pas trouvé, il ne se passait rien. Si on veut signaler qu'on ne l'a pas trouvé, il faut utiliser le `else` comme ceci :
```python runnable
texte = "Ceci est une phrase, tout ce qu'il y a de plus simple"
for lettre in texte : 
    print(lettre)
    if lettre == "x" :
        print("Un x a été trouvé !")
        break
else :
    print("Pas de x trouvé !")
```
Soit on trouve un "x" et donc la boucle s'arrête avec le `break` et donc ce qui est dans le `else` n'est pas exécuté. Sinon on n'a pas trouvé de "x" et ce qui est dans le `else`sera exécuté.

# Troisième partie : QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
for lettre in "Ab cd" :
    print(lettre)
```  
?[Que va afficher ce programme ( les "/" signifie un retour à la ligne)? ]
-[ ] Ab / cd
-[x] A / b /  / c / d
-[ ] Ab cd
-[ ] A / b / c / d

---

###### QCM 2
```python
texte = "Homme libre, toujours tu chériras la mer !"
compteur=0
for lettre in texte :
    if lettre == "e" :
        compteur += 1
print(compteur)
``` 
?[Que va afficher ce programme ?]
-[ ] 1
-[ ] 2
-[x] 3
-[ ] 4

---



