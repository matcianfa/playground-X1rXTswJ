<h1> <center>Cours : Les conditions</center></h1>

Quand on programme, il est indispensable de pouvoir expliquer à notre cher ordinateur quoi faire selon les cas qu'il va rencontrer. C'est là qu'entre en jeu la structure if... else....

"if" veut dire "si" et "else" veut dire "sinon". Une fois qu'on sait ça, la structure devient assez intuitive mais il reste à respecter une certaine syntaxe.

# Première partie : La structure `if`... `elif`... `else`

## `if`

Commençons par la structure la plus simple : `if` tout seul. Elle va nous permettre d'expliquer ce qu'il faut faire si une condition est vérifiée. Décortiquons un exemple de cette partie de code (on suppose qu'il y a du code avant où on obtient la valeur de la variable `note`) : 
```python
if note>15 : 
  print("Très Bien !")
```
Dans la première ligne on pourrait traduire le "if" par "si" et l'indispensable ":" en fin de ligne par "faire" ce qui donnerait "Si note>16 faire".  
L'ordinateur comprend alors qu'il doit faire ce qui suit seulement si la note est supérieure à 16. Plus précisément, il ne va pas faire tout ce qui suit mais seulement ce qui est écrit en décalé (on dit que le texte est indenté). C'est pour cela que print n'est pas écrit au même niveau que if. Pour indenter, on utilise la touche tabulation.  
Pour résumer notre exemple, si la note obtenue est par exemple 19, le programme affichera `Très Bien !`. Si on obtient la note 15 il ne fera rien.

## `if` avec `else`

Étoffons notre exemple en rajoutant ce qu'il doit afficher si la note n'est pas supérieure à 16. 

```python
if note>15 :
    print("Très Bien !")
else :
    print("Tu devras recopier 3 fois toutes les décimales de pi !")
```
Comme pour tout à l'heure, on peut traduire "else" par "sinon" et le ":" par "faire". L'ordinateur comprend alors que si la condition note>16 n'est pas vérifiée alors il exécutera ce qui est indenté en dessous de else.  
Pour résumer notre exemple, si la note obtenue est par exemple 19, le programme affichera `Très Bien !`. Si on obtient la note 15 ou 3, il affichera `Tu devras recopier 3 fois toutes les décimales de pi !`.

## `if`... `elif` ... `else`

On comprend bien sur notre exemple qu'il faudrait rajouter davantage de conditions selon la valeur de la note pour afficher des commentaires plus pertinents. Pour cela, on va utiliser l'instruction intermédiaire `elif` qui est une contraction de `else` et `if` c'est à dire qu'on peut le traduire par "sinon si". Il va nous permettre d'enchainer les distinctions de cas. On peut en mettre autant que l'on veut.

```python
if note>15 :
    print("Très Bien !")
elif note>13 :
    print("Bien")
elif note>11 :
    print("Assez Bien")
elif note>20 :
    print("Tu es un génie !!!")
else :
    print("Tu devras recopier 3 fois toutes les décimales de pi !")
```
Remarque : Pour le premier `elif`, je n'ai pas besoin de vérifier que la note est en dessous de 16 car si ce n'était pas le cas il aurait affiché "Très Bien !" et serait passé directement à la suite du `else` sans regarder les autres conditions.  
C'est pour cette même raison que "Tu es un génie" ne pourra jamais s'afficher car si la note est par exemple 22, on a note>16 et donc il s'affichera "Très Bien !" et c'est tout.  
Pour résumer notre exemple : Quand le programme s'execute et tombe sur un `if` il va chercher dans la série de conditions la première qui est validée et executer la partie du programme qui correspond puis va sauter directement après le bloc de conditions sans examiner les autres.

Voici le code précédent que vous pouvez tester et modifier pour bien comprendre comment cela fonctionne. Essayez de deviner le résultat qu'on devrait obtenir pour des valeurs de note comme 17, 14, 10, 7 ou 21 puis vérifier en modifiant la valeur de note et en appuyant sur Run.

```python runnable
# valeur de la note que vous pouvez modifier
note = 19

if note>15 :
    print("Très Bien !")
elif note>13 :
    print("Bien")
elif note>11 :
    print("Assez Bien")
elif note>20 :
    print("Tu es un génie !!!")
else :
    print("Tu devras recopier 3 fois toutes les décimales de pi !")
# Tout ce qui n'est pas indenté et qui suit le bloc if... elif... else sera executé quoi qu'il se passe dans ce bloc
# C'est tout simplement la suite du programme...
# Si on le décale, il s'executera dans la partie else du bloc de condition.
print("Ce message représente la suite du programme...")
```

Concluons cette partie avec des erreurs classiques à éviter :
1. Après `if`et `elif`il y a toujours une condition.
2. Après `else`, il n'y a jamais de condition (étant donné que signifie sinon donc correspond à tous les cas restants, pas besoin donc de les préciser même si par chance on les connait)
3. Après un `if`, `elif` et `else` il ne faut pas oublier de mettre en fin de ligne les deux points `:`.

## Complément : Imbrication de blocs conditionnels

Un rapide complément pour montrer à quoi ressemble un programme quand on enchaine des blocs conditionnels. Appuyez sur le bouton déroulant ci-dessous pour l'afficher

::: Complément : Imbrication de blocs conditionnels
On a vu que ce qui doit être exécuté après une condition doit être indenté. Ce qui veut dire que si après une condition, on veut retester une autre condition, il faudra penser à tout décaler. Si je reprends l'exemple précédent pour l'améliorer un peu pour être plus précis cela pourrait donner : 
```python runnable
note = 19

if note>15 :
    print("Très Bien !")
    if note>17 : 
        print("Félicitations !")
        if note>20 :
           print("Tu es un génie !!!")
elif note>13 :
    print("Bien")
elif note>11 :
    print("Assez Bien")
else :
    print("Tu devras recommencer l'interrogation en devoir maison")
    if note<6 :
        print("Tu devras en plus recopier 3 fois toutes les décimales de pi !")
```
Donnons quelques explications sur un exemple. Si la note est 19 :
- comme note>15, on va effectuer toute la partie qui est indentée et qui suit cette condition. Autrement dit, les lignes 4 à 8.  
- La ligne 4 demande d'afficher "Très bien !" donc ça l'affiche.  
- On a de nouveau une condition. Comme note>17, on exécute tout ce qui suit cette condition et qui est indentée par rapport à elle c'est à dire les lignes 6 à 8.  
- La ligne 6 demande d'afficher "Félicitations !" donc ca l'affiche.  
- La ligne 7 est une condition mais comme elle n'est pas vérifiée, on n'execute pas la ligne 8. 
- Comme on a fini d'executer ce qu'on devait, on a fini.  
N'hésitez pas à modifier la valeur de la note dans le programme précédent en essayant de deviner le résultat qu'on devrait obtenir avant pour voir si vous avez bien compris. Essayez 17, 18, 22, 8, 4 par exemple.
:::

# Deuxième partie : Les conditions

Après un `if`ou un `elif`, on a dit qu'il fallait mettre une condition. Une condition est tout simplement quelque chose qui peut être vrai ou faux. Voici quelques exemples de conditions qu'on complétera au besoin.

- `True` et `False` :  
  Ils signifient vrai et faux donc ce sont les conditions les plus évidentes. On les appelle les booléens. Il peut paraitre absurde de mettre un booléen directement après un if (puisque si on met True, le code correspondant sera toujours executé donc le if ne sert à rien et inversement pour le False) mais dans la pratique, le booléen sera dans une variable qui elle pourra être modifiée et donc selon la valeur, l'action à effectuer ne sera pas la même.

- Les comparaisons :  
  Une façon d'obtenir un booléen est en comparant deux objets comme on a fait avec notre note dans la partie précédente. Voici les notations pour pouvoir comparer :  
    `==` : pour tester l'égalité. Il faut doubler le = pour le différencier de l'affectation des variables.  
    `!=` : différent de.  
    `<` : strictement inférieur.  
    `<=` :inférieur ou égal.  
    `\>` : strictement supérieur.  
    `\>=` : supérieur ou égal.  

  Par exemple :  
    `1+1 == 2` est vrai.  
    `2\*3 == 3` est faux.  
    `2+3 != 4` est vrai.  
    `14 >= 15` est faux.  

  Les inégalités ne fonctionnent pas que pour les nombres. Par exemple on peut comparer des mots ou des listes de nombres avec l'ordre lexicographique (celui du dictionnaire).  
  `"elephant" < "souris"` est vrai  
  `"français" < "mathématiques"` est vrai  
  `(1,5)<(2,3)` est vrai  

- Les connecteurs logiques `not`, `and` et `or`:  
  Ils permettent de créer une condition à partir d'autres conditions. Il en existe d'autres mais ce sont les principaux.
  Si on les traduit, ça donnerait "contraire de" pour not, "et" pour and et "ou" pour or.
  Par exemple :  
  `not x<3` est identique à `x>=3`.
  `x<3 and x>1` est identique à `1<x<3` car x doit vérifier les deux conditions en même temps.
  `x<3 or x>5` est identique... à elle même car il n'y a pas de façon plus concise de l'écrire. Elle sera vraie si une des deux conditions est vérifiée.  
        
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

###### QCM 3
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

###### Exercice 1 :


Quand on demande d'afficher, c'est avec `print`.

@[Programme de calcul]({"stubs": ["Variables_et_fonctions/Programme_calcul2.py"], "command": "python3 Variables_et_fonctions/Programme_calcul2_Test.py"})

---

###### Exercice 2 :



Quand on demande d'afficher, c'est avec `print`.

@[Afficher le plus grand des deux]({"stubs": ["Variables_et_fonctions/pi2et2pi.py"], "command": "python3 Variables_et_fonctions/pi2et2pi_Test.py"})

---



