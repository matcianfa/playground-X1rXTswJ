##  Anacycliques et Palindromes

### Anacycliques

Un anacyclique est un mot qui, lorsqu'on le lit à l'envers, donne un autre mot (qui a du sens). 
Exemple : 
+ nez et zen 
+ bons et snob 
+ tracé et écart 

Le but de cet exercice est de créer un programme qui affiche "ANACYCLIQUE" lorsque les deux mots donnés en entrée sont symétriques ou bien "PAS ANACYCLIQUE"

> Entrée : Deux mots nommés ***mot_1*** et ***mot_2***.

> Sortie : "ANACYCLIQUE" ou "PAS ANACYCLIQUE".

@[Anacycliques ?]({"stubs": ["Chaines_caracteres/Anacycliques.py"], "command": "python3 Chaines_caracteres/Anacycliques_Test.py"})

---

### Palindromes

Un palindrome est une phrase qui peut se lire à l'envers comme à l'endroit. 

Exemples : 
+ "ici" 
+ "kayak" 
+ "selles" 
+ "A Cuba Anna a bu ça" 
+ "C'est sec" 
+ "Engage le jeu, que je le gagne !" 
+ "À l'étape, épate-la !" 


Le but de cet exercice est d'écrire un programme qui affichera si une phrase est "PALINDROME" ou "PAS PALINDROME" 

Dans un premier temps, il suffira de valider les premiers tests ou il faudra gérer les problèmes de majuscules et d'espaces. mais pour les meilleurs, il faudra essayer de tous les valider en gérant les accents et la ponctuation.

::: Aide
+ On remarquera qu'il suffit de ne considérer que les lettres.
+ On pourra jetter un oeil sur les fonctions .upper() ou .lower().
:::

> Entrée : Une ***phrase***.

> Sortie : "PALINDROME" ou "PAS PALINDROME".
