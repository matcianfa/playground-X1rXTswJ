<h1> <center>Cours : Les boucles `while`</center></h1>

# Présentation des boucles `while`

While signifie en anglais "tant que". Tout comme la commande `for`, elle permet de répéter des instructions mais contrairement à `for` qui le fait en énumérant les éléments de quelque chose, `while` permet de boucler tant qu'une condition est vérifiée. L'avantage e while est donc qu'il ne faut pas connaitre à l'avance le nombre de fois où on devra répéter notre boucle.  
Par exemple, observez le résultat pour le code suivant :
```python runnable
i = 0
while i < 4 :
    print(i)
    i+=1
```
Quelques explications : 
Tant que `i<4`, on demande d'afficher `i` puis d'augmenter `i` de 1. Du coup le résultat sera l'affichage verticalement de 0, 1, 2 et 3. Le chiffre 4 ne sera pas affiché car quand `i` vaut 4, la condition `i<4` n'est pas vérifiée donc on n’exécute pas la boucle. 

Les conditions que l'on peut mettre après while sont exactement les mêmes que pour if. 

Remarque important : Ça peut paraitre du bon sens sur des exemples simples comme celui ci mais il ne faut pas oublier d'augmenter i sinon i vaudra toujours 0 et donc le programme affichera des 0 jusqu'à la fin des temps... C'est ce qu'on appelle une boucle infinie. En voici malheureusement une autre :
```python
while ma_note_en_maths <20 :
    je_bosse_mes_maths()
```

Sur l'exemple précédent, on aurait pu aussi bien utiliser un boucle `for`. Voyons à présent un exemple où l'utilisation de while est indispensable.   
Supposons qu'on veuille trouver la plus petite valeur de `n` telle que n(n+1)(n+2)  dépasse un million. Ici on ne peut pas utiliser la boucle `for` puisqu'on ne saurait pas a priori quoi mettre dans `range` (Si on savait, on aurait la réponse au problème et donc pas besoin de faire de programme...). 
Voyons un exemple de code qui répond à notre problème :
```python runnable
n = 0
while n*(n+1)*(n+2) < 1000000 :
    n+=1
print(n)
```
Notre programme commence avec n=0 puis tant que le calcul de n\*(n+1)\*(n+2) ne dépasse pas un million, on augmente n de 1 pour tester de nouveau si n\*(n+1)\*(n+2) ne dépasse pas un million etc. Dés que n\*(n+1)\*(n+2) dépasse un million, la boucle s'arrête et on affiche la valeur de n qui sera forcément la première telle que n\*(n+1)\*(n+2) dépasse un million.

Voyons un autre exemple classique de ce qu'on appelle une recherche de seuil, où cette fois ci on recherche à partir de quel valeur de n la somme 1 + 2 + 3 + ... + n dépasse un million. Ce fois ci, il va falloir à chaque étape de la boucle à la fois augmenter n mais aussi calculer la somme au fur et à mesure. Voici un exemple de programme qui pourrait répondre à la question :
```python runnable
n = 0
somme = 0
while somme < 1000000 :
    n += 1
    somme += n 
print(n)
```
Quelques explications : Comme on veut calculer 1 + 2 + 3 + ..., la valeur de n va commencer à 0 et augmenter de 1 à chaque fois. Pour notre somme, à chaque étape on ajoute la valeur de n tant que la somme ne dépasse pas le million.  
Remarque : Il ne faut surtout pas inverser l'ordre de `n += 1` et `somme += n` car sinon quand notre somme va enfin dépasser un million, on va augmenter n de 1 et donc on aura comme résultat 1 de trop par rapport à la bonne réponse. En effet, dans une boucle while, la condition est testée uniquement quand une boucle s'est terminée entièrement. Donc même si somme dépasse un million, s'il y a des instructions qui suivent dans la boucle, elles seront exécutées. 

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
