<h1> <center>Compléments sur les chaines de caractères</center></h1>

# Codage ASCII

On va voir dans les exercices des problèmes de codage. Ce sont des problèmes classiques en programmation et pour cela, on a besoin de décaler des caractères par exemple ou de les mélanger. Il serait possible (mais forcément très long) d'expliquer ce que l'on fait pour chaque caractère et à chaque fois mais il existe une table 'universelle' qui associe à chaque caractère un numéro. C'est ce qu'on appelle la norme ASCII. On peut retrouver des explications et le tableau récapitulatif des correspondances ici par exemple : |Wikipédia : Norme ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange)  
Dans cette table, le "a" correspond au numéro 97, le "A" au numéro 65...
Il existe des fonctions en Python qui permettent de passer des caractères aux numéros correspondants :
+ `ord(caractere)` : Donne le code ASCII du caractère.
  ```python runnable
  print(ord("a"))
  print(ord("A"))
  print(ord("#"))
  ```

+ `chr(numero)` : Donne le caractère correspondant au code ASCII.
  ```python runnable
  print(chr(65))
  print(chr(97))
  print(chr(35))
  ```
  
Exemple d'utilisation : Je veux transformer un caractère en son suivant.
```python runnable
car="e"
numero=ord(car)
nouveau_car=chr(numero+1)
print(nouveau_car)
```
Expliquons un peu : On place "e" dans la variable `car`. On récupère son code ASCII et on le met dans la variable `numero`. On récupère le caractère suivant c'est à dire correspondant au code ASCII `numero+1`. Et on affiche le  caractère obtenu.  
Bien sûr cet exemple utilise beaucoup trop de variables mais c'est pour détailler. On pourrait mettre directement `print(chr(ord(car)+1))` mais c'est moins clair... Et petite question pour finir cette partie : Qu'obtiendrait-on si on prenait car = "z" ?

# Le formatage avec la fonction `format`

Cette partie est très facultative. Elle intéressera ceux qui veulent approfondir leurs connaissances en programmation.  
Le but de cette partie est de faire une présentation de la fonction `format`  des chaines de caractères. Il existe ce que l'on appelle les expressions régulières qui permettent de vérifier ou rechercher un certain formatage dans un texte (comme par exemple vérifier si le format d'un numéro de téléphone ou d'une adresse mail ou d'un numéro de carte bleue est valide) mais nous n'allons pas en parler ici.  
Le formatage avec `format` s'applique comme un texte à trous que l'on complète avec des données que l'on peut formater. 

Prenons l'exemple de 3 variables dont on veut afficher les valeurs dans un texte :
```python runnable
a=0.5
b=2
c=1/3
print("Dans b il y a la valeur {1}, dans a il y a la valeur {0} et dans c la valeur {2}".format(a,b,c))
```
La fonction format va remplacer les accolades par les variables en respectant l'ordre : {0} sera remplacée par la valeur de la première variable donnée (ici a), {1} par b et {2} par c. Déjà on peut voir un intérêt pratique à la fonction car sinon pour obtenir le même résultat à la main, il aurait fallu écrire :
`"Dans b il y a la valeur "+str(b)+" , dans a il y a la valeur "+str(a)+ " et dans c la valeur "+str(c)`.  
Imaginez s'il y a 15 variables à insérer dans un texte dont certaines apparaissent plusieurs fois et ont un nom long à taper...

Mais `format` permet en plus de formater ce que l'ont veut afficher. Par exemple si je veux afficher un nombre arrondi à deux chiffres significatifs après la virgule il suffit de rajouter `:.2g` dans les accolades concernées. Voici ce que cela donne :
```python runnable
a = 0.5
b = 2
c = 1/3
print("Dans b il y a la valeur {1:.2g}, dans a il y a la valeur {0:.2g} et dans c la valeur {2:.2g}".format(a,b,c))
```

Si par hasard on veut arrondir à deux chiffres après la virgule en gardant les 0 inutiles comme pour les prix par exemple, on utilise de la même façon `:.2f`.
```python runnable
a = 0.5
b = 2
c = 1/3
print("Dans b il y a la valeur {1:.2f}, dans a il y a la valeur {0:.2f} et dans c la valeur {2:.2f}".format(a,b,c))
```

Voici pour cette initiation à la fonction format. Si on veut aller plus loin (formatage de dates, personnalisés...), internet regorge d'information !

# Entrainement 

### Exercice 1

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui affiche le code ASCII correspondant à chaque lettre.

Pour l'affichage, on utilisera `print` et les code ASCII seront affichés en allant à la ligne à chaque fois.

@[Exercice 1]({"stubs": ["Chaines_caracteres/Comp_chaine_exo_1.py"], "command": "python3 Chaines_caracteres/Comp_chaine_exo_1_Test.py"})

---

### Exercice 2

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui, pour chaque lettre du texte, affiche la lettre suivante dans l'alphabet. 

Quelques compléments : 
+ Pour le "z", on affichera "a". 
+ Le texte n'est composé que de lettres minuscules et sans accent.

Pour l'affichage, on utilisera `print` et chaque lettre sera affichée en allant à la ligne.

@[Exercice 2]({"stubs": ["Chaines_caracteres/Comp_chaine_exo_2.py"], "command": "python3 Chaines_caracteres/Comp_chaine_exo_2_Test.py"})

---

### Exercice 3

Pour le texte donné dans la fenêtre ci-dessous, créer un programme qui, pour chaque lettre du texte, affiche la lettre suivante dans l'alphabet. 

Quelques compléments : 
+ Pour le "z", on affichera "a". 
+ Les lettres du texte sont toutes sans accent mais ne sont pas toutes en minuscule.
+ La ponctuation et espaces devront rester inchangés.

Pour l'affichage, on utilisera `print` et chaque lettre sera affichée en allant à la ligne.

@[Exercice 3]({"stubs": ["Chaines_caracteres/Comp_chaine_exo_3.py"], "command": "python3 Chaines_caracteres/Comp_chaine_exo_3_Test.py"})
