<h1> <center>Cours : Les chaines de caractères</center></h1>

# Présentation des chaines de caractères

Avec les nombres et les listes, les chaines de caractères sont les éléments informatiques qu'on utilise le plus couramment. Ce sont tout simplement des objets qui représentent du texte. Elles sont entre guillemets (ou apostrophes).
```python   
a="Ceci est une chaine de caractères"
b="1+1"
c=1+1
```
Ainsi, a et b sont des chaines de caractères alors que c est un entier qui vaut 2.  

Il y a énormément d'action possible sur les chaines de caractères, nous allons voir les principales.
# Les actions de base

+ `len(texte)` : Donne la longueur d'un texte.
```python runnable
print(len("abc def"))
```

+ `texte[n]` : Affiche le n-ième terme du texte. Attention : la première lettre commence à l'indice 0 !  
  Petite astuce : Si on veut commencer par la fin : texte[-1] est la dernière lettre, texte[-2] l'avant dernière etc.
  ```python runnable
  print("Alea jacta est"[0])
  print("Alea jacta est"[5])
  print("Alea jacta est"[-1])
  ```
  
+ `texte[debut : fin]` : Affiche les caractères de `texte` compris entre l'indice `debut` et l'indice `fin-1`.  
  Attention ici aux pièges : la première lettre du texte correspond toujours à l'indice 0 et on ne prend pas la lettre d'indice `fin`.  
  Astuce : Si on veut commencer du début du texte, on met juste `texte[:fin]`. De même si on veut aller jusqu'au dernier caractère, on mettra `texte[debut : ]`.
  ```python runnable
  print("Alea jacta est"[5:10])
  print("Alea jacta est"[:4])
  print("Alea jacta est"[5:])
  ```
  
+ `texte1+texte2` : Concatène les deux textes c'est à dire les met bout à bout.
  ```python runnable
  texte1="Vive"
  texte2="Les Mathématiques"
  print(texte1+texte2)
  ```
  On peut bien sûr enchainer les concaténations : texte1+texte2+texte3+...
  
+ `str(objet)` : Transforme (quand c'est possible) l'`objet` en texte pour pouvoir l'utiliser comme un texte. Très utile pour rajouter des variables dans un texte par exemple ou récupérer les chiffres d'un nombre.
  ```python runnable
  c = 1 + 1
  print("La valeur de c est "+str(c))
  
  # On récupère le chiffre d'indice 4 c'est à dire le cinquième :
  n = 133675184
  chiffre = str(n)[4] 
  print(chiffre)
  ```
  Dans `c` il y a le résultat du calcul. `str(c)` transforme ce résultat en chaine de caractère contenant ce résultat. On le rajoute ensuite à la chaine `"La valeur de c est "`
  Pour le deuxième exemple, on transforme le nombre `n`en chaine de caractère ce qui nous permet de récupérer les chiffres un à un sous forme de chaine de caractères. Si on veut les retransformer en nombre pour pouvoir faire des calculs par exemple, on pourra utiliser `int(chiffre)`.
  
+ `texte*k` : Crée une chaine de caractère dans laquelle on répète le texte k fois d'affilée.
  ```python runnable
  texte = "Monsieur, j'ai pas compris ! "
  print(texte*5)
  ```
  
+ `sous_texte in texte` : Renvoie True si la chaine de caractère `sous_texte` est dans `texte` et False sinon.
A utiliser par exemple comme condition avec if par exemple.
  ```python runnable
  texte = "C'est un trou de verdure où chante une rivière"
  print("chante" in texte)
  print("dur" in texte)
  print("eau" in texte)
  ```
  On teste ici si les sous-textes "chante", "dur" et "eau" sont dans la chaine de caractères stockée dans `texte`.
  
  Voici un exemple d'utilisation dans une structure conditionnelle : 
  ```python
  if lettre in "aeiouy":
    print(lettre + " est une voyelle")
  else :
    print(lettre + " n'est pas une voyelle")
  ```
  Ce code permettrait par exemple de vérifier si la variable lettre est une voyelle ou pas.
  
+ `for caractere in texte` : Nous permet de créer une boucle en énumérant les lettres de texte.
  Par exemple si je veux afficher les chiffres d'un texte :
  ```python runnable
  texte="Quatre bonbons à 0,25 euro chacun coûtent un euro"
  for caractere in texte:
      if caractere in "0123456789":
          print(caractere)
  ```
  Quelques explications : La boucle `for` va prendre le premier caractère de `texte` et le placer dans la variable `caractere` c'est à dire que `caractere` = 'Q'. Ensuite on teste si car fait partie des chiffres. Comme ce n'est pas le cas, et qu'il n'y a rien à faire dans ce cas, on revient à la boucle for avec la deuxième lettre cette fois et on recommence jusqu'au caractère "0" qui faire partie des chiffres donc on l'affiche etc.
  
+ Comparaisons de chaines de caractères : On peut comparer, comme pour les nombres, des chaines de caractères.
  Le résultat de la comparaison est True ou False et peuvent donc s'utiliser comme condition avec if .
  Voici les différentes comparaisons possibles :
  - `texte1 == texte2` : Renvoie True si les deux textes sont parfaitement identiques.
  - `texte1 != texte2` : Renvoie True si les deux textes ont au moins un caractère de différent.
  - `texte1 < texte2` : Renvoie True si le `texte1` est strictement avant `texte2` dans l'ordre lexicographique (l'ordre du dictionnaire).
  - `texte1 <= texte2` : Comme < mais les deux textes peuvent être les mêmes.
  - `texte1 > texte2` : Renvoie True si le `texte1` est strictement après `texte2` dans l'ordre lexicographique (l'ordre du dictionnaire).
  - `texte1 >= texte2` : Comme < mais les deux textes peuvent être les mêmes.
  Pour ranger dans l'ordre lexicographique, on compare les deux premiers caractères de chaque texte. S'ils sont égaux, on compare le second etc.
  Par exemple : "azerty"<"azfa" car les premiers termes de chaque chaines sont égaux. De même pour le second. Pour le troisième, comme "e"<"f", on a "azerty"<"azfa". (On ne regarde même pas la suite).
  Ça fonctionne aussi pour les nombres dans une chaine de caractères : "1234"<"2". En effet, on les compare comme des chaines de caractères et non comme des nombres. On regarde le premier caractère : "1"<"2" donc "1234"<"2".
  Pour être plus précis, pour comparer deux caractères, on compare en fait leur code ASCII (voir plus loin). Donc on a "1" < "A" < "_" < "a" par exemple.
  
# Fonctions plus spécifiques aux chaines de caractères

Ce sont des fonctions que l'on applique à une chaine de caractères et qui donc devront se mettre après la chaine de caractère à laquelle on l'applique en mettant un point entre.

+ `.find(sous_chaine)` : Donne l'indice où se trouve pour la première fois `sous_chaine`.
  ```python runnable
  texte="J'ai posé ma brosse sur le bureau"
  print(texte.find("brosse"))
  print(texte.find("o"))
  ```
  On fera bien attention au fait que les indices commencent à 0 ! Le 'b' de brosse étant le 14e caractère, son indice est donc 13.
  Pour le deuxième exemple, on voit que le "o" de brosse n'est pas pris en compte. La fonction find ne renvoie que l'indice du premier "o" qu'il rencontre.
  
+ `.count(sous_chaine)` : Donne le nombre de fois où `sous_chaine` se trouve dans la chaine à qui l'on applique la fonction.
  ```python runnable
  texte="J'ai posé ma brosse sur le bureau"
  print(texte.count("os"))
  print(texte.count("e"))
  ```
  Il y a 2 fois "os" dans texte et 3 "e". On remarquera que "é" n'est pas compté comme un "e".
  
+ `.replace(sous_chaine1, sous_chaine2)` : Remplace toutes les `sous_chaine1` par les `sous_chaine2`.
  ```python runnable
  texte= "Une foncttttion ttttrès prattttique si vous répéttttez ttttrop les tttt"
  print(texte.replace("tttt","t"))
  ```

+ `.lower()`, `.upper()` : La première permet de mettre tout le texte en minuscule et la deuxième en majuscule.
  Pas les plus utiles mais elles dépannent car pour Python, "e" est différent de "E". donc pour chercher les voyelles par exemple, il est plus simple de mettre d'abord tous le texte en minuscule sinon il faudra chercher parmi "aeiouyAEIOUY".
  

# QCM

Voici quelques QCM pour voir si vous avez bien compris. N'hésitez pas à relire ce qui précède si vous avez un doute.

###### QCM 1
```python
k = 0
while k < 6 :
    print(k)
    k += 2
```  
?[Que va afficher ce programme (les `/` remplacent ici un retour à la ligne)? ]
-[x] 0 / 2 / 4 
-[ ] 0 / 1 / 2 / 3 / 4 / 5 
-[ ] 0 / 2 / 4 / 6
-[ ] 2 / 4 

---

###### QCM 2
```python
k = 0
while k < 6 :
    k += 2
    print(k)
```  
?[Que va afficher ce programme (les `/` remplacent ici un retour à la ligne)? ]
-[ ] 0 / 2 / 4 
-[ ] 0 / 1 / 2 / 3 / 4 / 5 
-[ ] 0 / 2 / 4 / 6
-[x] 2 / 4  

---

###### QCM 3
```python
n=0
while ... :
    print(n)
    n += 3
```  
?[Par quoi remplacer les ... pour que le programme précédent affiche 0 / 3 / 6 / 9 / 12 (les `/` remplacent ici un retour à la ligne) ? ]
-[ ] n < 12
-[x] n <= 12
-[x] n < 14
-[x] n**2 < 145

---

###### QCM 4
```python
n=0
while ... :
    n += 1
print(n)
```  
?[Par quoi remplacer les ... pour que le programme précédent affiche la plus petite valeur de n telle que n²+3n dépasse 1000 ? ]
-[ ] n² + 3n < 1000
-[ ] n**2 + 3*n > 1000
-[ ] n < 1000
-[x] n**2 + 3*n < 1000

---

###### QCM 5
```python 
n = 0
somme = 0
while somme < 10000 :
    n += 1
    ... 
print(n)
``` 
?[Par quoi remplacer les ... pour que le programme précédent affiche la plus petite valeur de n telle que 2*1+ 2*2 + 2*3 + ... + 2*n dépasse 10000 ?]
-[ ] somme += n
-[ ] somme = 2 * somme 
-[x] somme += 2*n
-[ ] somme = 2*1+ 2*2 + 2*3 + 2*n

---

###### QCM 6
```python
n=0
while ... :
    n += 1
print(n)
```  
?[Par quoi remplacer les ... pour que le programme précédent affiche la plus petite valeur de n telle que 1/n soit inférieur à 0.12345 ? ]
-[ ] n < 0.12345
-[ ] 1/n < 0.12345
-[ ] 1/n != 0.12345
-[x] 1/n > 0.12345


# Entrainement 

### Exercice 1

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que (n+1)\*(n+3) dépasse 12345.

@[Exercice 1]({"stubs": ["Les_boucles/while_exo1.py"], "command": "python3 Les_boucles/while_exo1_Test.py"})

---

### Exercice 2

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que 4 + 5 + 6 + ... + n dépasse 12345.

@[Exercice 2]({"stubs": ["Les_boucles/while_exo_2.py"], "command": "python3 Les_boucles/while_exo_2_Test.py"})

---

### Exercice 3

En vous inspirant des exemples donnés dans la partie cours, écrire un programme qui affiche le plus petit entier n tel que 1² + 2² + 3² + ... + n² dépasse 12345.

@[Exercice 3]({"stubs": ["Les_boucles/while_exo_3.py"], "command": "python3 Les_boucles/while_exo_3_Test.py"})
