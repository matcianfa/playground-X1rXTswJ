<h1> <center>Cours : Les Fonctions</center></h1>

Pour l'instant, nous avons créé des programmes ni trop longs ni trop compliqués mais quand on va s'attaquer à des problèmes plus complexes, il va devenir indispensable de découper notre programme en sous-programmes plus petit pour le clarifier et pour le rendre plus facile à écrire et à débugguer. C'est dans ce but que nous allons voir comment créer des fonctions.  Les fonctions permettent aussi d'éviter d’écrire plusieurs fois un code qui fait toujours la même chose exactement comme en maths lorsqu'on appelle f la fonction plutôt qu'écrire à chaque fois tous les calculs qu'il faudrait faire à partir de x.

# Comment définir une fonction

Pour créer une fonction, rien de plus simple, on utilise la synthaxe suivante :
```python
def nom_de_la_fonction (parametres):
    #ce que doit faire la fonction
```
`def` pour expliquer qu'on définit une fonction.  
`nom_de_la_fonction` : vous pouvez mettre des lettres et chiffres (mais pas en premier) dans le nom mais pas d'espace.  
`parametres` : il faut préciser les paramètres de votre fonction comme en math pour f(x), le paramètre est x (En mathématique, on l'appelle une variable). S'il y a plusieurs paramètres, on les sépare par une virgule.  
`:` On n'oublie pas les 2 points à la fin de la ligne ni l'indentation dans tout ce qui est à exécuter dans la fonction.  
Donnons des exemples :
+ Exemple 1 :  
  ```python runnable
  def addition(a,b):
      print(a+b)
  ```
  Cette fonction prend en entrée a et b et affiche le résultat de a+b. mais si on ne tape que ça, il ne se passe rien. Pour utiliser notre fonction, il faut l'appeler :
  ```python runnable
  def addition(a,b):
      print(a+b)
      
  addition(2,3)
  addition("ab","abc")
  addition([1, 2, 3] , [1, 2] )
  ```
  Remarque : Nous n'avons pas précisé que a et b étaient des entiers donc python fera une addition de tout ce qu'il sait additionner comme ici les chaines de caractères ou les listes.
+ Exemple 2 :  
  ```python runnable
  def dire_chut() :
      print("Chhhhhhhhhuuuuuuuut!")
      
  dire_chut()
  ```
  Un fonction qu'il suffit d'appeler en écrivant dire_chut() car il n'y a pas de paramètre.
+ Exemple 3 :  
  On peut combiner les fonctions entre elles :
  ```python runnable
  def addition(a,b):
      print(a+b)
      
  def dire_chut() :
      print("Chhhhhhhhhuuuuuuuut!")    
  
  def ma_fonction(a) :
      addition(a,3)
      dire_chut()
      for i in range(2):
          addition(i,a)
  ```
  
# La commande `return`
La commande `return` permet de renvoyer un résultat obtenu par la fonction pour pouvoir l'utiliser dans la suite du programme. Elle est fondamentalement différente de `print` qui ne fait que l'afficher à l'écran (et donc plus utilisable dans notre programme).              
Reprenons notre fonction addition ci-dessus et essayons de la mettre dans une variable puis d'afficher cette variable.
```python runnable
resultat=addition(2,3)
print(resultat)
```
Quand on met `addition(2,3)` dans dans la variable `resultat` il affiche 5 et quand on veut afficher `resultat` il affiche `None` c'est à dire vide. Que se passe-t-il ? En fait c'est très simple, quand on lance `addition(2,3)`, il exécute la fonction dans laquelle on demande d'afficher a+b. Mais l'affichage se fait dans la console donc c'est comme si Python nous avait envoyé le résultat à nous et donc ne peut pas l'utiliser pour le mettre dans la variable `resultat`.  
Si on veut qu'un programme renvoie un résultat qu'il puisse réutiliser ensuite, il faut utiliser la commande `return` au lieu de `print`. Par exemple :
```python runnable 
def addition(a,b):
    return a+b

resultat=addition(2,3)
print(resultat)
```
Cette fois ci, il n'affiche rien lorsqu'on n'execute que la commande `resultat=addition(2,3)` et quand on affiche la variable `resultat`, elle contient bien 5.  
Il faut donc faire très attention à ce que l'on veut faire : retourner un résultat pour le réutiliser (dans ce cas on utilise `return`) ou bien juste afficher pour nous le résultat (dans ce cas on utilise `print`)

+ Remarque très importante : `return` arrete la fonction !
  Il est très important de savoir que quand on lance un return, la fonction s’arrête. Autrement dit il faut être sûr d'avoir fait tout ce que l'on souhaitait faire avec notre fonction avant de lancer return pour renvoyer le résultat. Cela peut être cependant très pratique par exemple dans une boucle for, dès qu'on a le résultat voulu, on le renvoie sans avoir besoin de finir la boucle. Par exemple, si je cherche à savoir s'il y a un 0 dans une liste de nombres, je pourrais utiliser cette fonction :
  ```python
  def  chercher(liste):
      for nombre in liste:
          if nombre==0:
              return True
      return False
  ```
  Pour chaque nombre dans la liste, on teste si ce nombre est 0. Si oui on renvoie True et la fonction s'arrete, si non on continue la boucle jusqu'à la fin de la liste. Donc au final dans ce cas, aucun 0 n'a été trouvé, on renvoie donc False.
        
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

# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1  
?[Que puis-je écrire si je veux rajouter le nombre 3 à une liste nommée L ? ]
-[x] L.append(3) 
-[ ] L + 3
-[x] L + [3]
-[ ] L.extend(3)
-[x] L.extend([3])
-[ ] L * 3

---

###### QCM 2
```python
liste = [ 1, 3 ]
print(liste * 2)
```  
?[Que va afficher ce programme ? ]
-[ ] [ 2, 6 ]
-[ ] [ 1, 3, 2 ]
-[x] [ 1, 3, 1, 3 ]
-[ ] [ 1, 1, 3, 3 ]
-[ ] [ [1, 3], [1, 3] ]

---

###### QCM 3
?[Que faut-il écrire pour afficher tous les entiers de 4 à 100 dans l'ordre croissant ? ]
-[x] print(list(range(4,101))) 
-[ ] print(range(4,100))
-[ ] print(list(range(4,100))
-[ ] print([4,5,...,100])

---

###### QCM 4
```python
liste = [ 1, 5, 4, 12, 7, 9 ,10 , 2]
print(liste[4])
```  
?[Que va afficher ce programme ? ]
-[ ] 2 
-[ ] 3
-[x] 7
-[ ] 12

---

###### QCM 5
```python
liste = [ 1, 5, 4, 12, 7, 9 ,10 , 2]
print(liste[3:5])
```  
?[Que va afficher ce programme ? ]
-[ ] [4, 12, 7]
-[x] [12, 7]
-[ ] [12, 7, 9]
-[ ] [12, 9]

---

###### QCM 6
```python
liste = [ 1, 5, 4, 12, 7, 9, 10, 2]
print(...)
```  
?[Que faut-il mettre à la place des ... pour afficher [7, 9, 10] ? ]
-[x] liste[4:7]
-[ ] liste[5:7]
-[ ] liste[5:8]
-[ ] liste[4:6]

---

###### QCM 7
```python
liste = [ 1, 5, 4, 12, 7, 9, 10, 2]
liste[5] = 6
print(liste)
```  
?[Que va afficher ce programme ? ]
-[ ] [ 1, 6, 4, 12, 7, 9, 10, 2]
-[ ] [ 1, 5, 4, 12, 6, 9, 10, 2]
-[x] [ 1, 5, 4, 12, 7, 6, 10, 2]
-[ ] [ 1, 5, 4, 12, 7, 9, 5, 2]

---

###### QCM 8
```python
liste = [ 1, 5, 4, 12, 7, 9, 10, 2]
liste.remove(5)
print(liste)
```  
?[Que va afficher ce programme ? ]
-[x] [ 1, 4, 12, 7, 9 , 10, 2]
-[ ] [ 1, 5, 4, 12, 7, 10, 2]
-[ ] [ 1, 5, 4, 12, 9, 10, 2]
-[ ] [ 1, 5, 4 ]

---

###### QCM 9
```python
liste = [ 1, 5, 4, 12, 7, 9, 10, 2]
liste.sort()
print(liste)
```  
?[Que va afficher ce programme ? ]
-[ ] [ 12, 10, 9, 7, 5, 4, 2, 1 ]
-[ ] [ 1, 10, 12, 2, 4, 5, 7, 9]
-[ ] [ 1, 5, 4, 12, 7, 9, 10, 2]
-[x] [ 1, 2, 4, 5, 7, 9, 10, 12]

---

###### QCM 10
```python
liste = [ 1, 1+1, "un", "2+3", 7,  23, "1", "vingt trois"]
print(23 in liste)
print(2 in liste)
print(5 in liste)
print("7" in liste)
print("vingt" in liste)
print("23" in liste)
print("vingt trois" in liste)
print([7, 23] in liste)
```  
?[Cochez les cases correspondant au numéro des lignes qui vont afficher True ]
-[x] 2
-[x] 3
-[ ] 4
-[ ] 5
-[ ] 6
-[ ] 7
-[x] 8
-[ ] 9

