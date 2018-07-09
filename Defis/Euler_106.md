# Ensembles de sommes spéciaux : Meta-Testing
`Difficulté : Difficile (50%)`
`Origine : Projet Euler n°106`

Notons S(A) la somme des éléments d'un ensemble A de taille n. On dira que A est un ensemble de sommes spécial si pour tous ensembles disjoints B et C, on a les deux propriétés suivantes qui sont vérifiées :

    S(B) ≠ S(C) : c'est à dire que les sommes de sous ensembles sont toutes différentes
    Si B contient plus d'éléments que C alors S(B) > S(C)

Pour ce problème on va supposer que les ensembles contiennent n éléments formant une suite strictement croissante et qu'il vérifient déjà la deuxième règle.

De manière surprenante, parmi les 25 paires de sous-ensembles qu'on peut former à partir d'un ensemble à 4 éléments, seulement une de ces paires a besoin d'être testée pour vérifier la première règle. De la même manière, pour n=7, seule 70 des 966 paires de sous-ensembles ont besoin d'être testées.

Pour n=12, combien des 261625 paires de sous-ensembles qu'on peut obtenir ont elles besoin d'être testées pour vérifier la première règle ?

Note : Ce problème est en relation avec le problème 103 et 105.

On affichera le résultat avec `print`.

@[Ensembles de sommes spéciaux : Meta-Testing]({"stubs": ["Defis/Euler_106.py"], "command": "python3 Defis/Euler_106_Test.py"})

---

# Réseau minimal
`Difficulté : Moyen (35%)`
`Origine : Projet Euler n°107`

Le réseau non orienté suivant est composé de 7 sommets and 12 arêtes avec un poids total de 243. 

![reseau](https://projecteuler.net/project/images/p107_1.gif)

Ce réseau peut être représenté par le tableau suivant :

<table>
  <tr>
    <th>  </th>
    <th> A </th>
    <th> B </th>
    <th> C </th>
    <th> D </th>
    <th> E </th>
    <th> F </th>
    <th> G </th>
  </tr>
  <tr>
    <td> A </td>
    <td> - </td>
    <td> 16 </td>
    <td> 12 </td>
    <td> 21 </td> 
    <td> - </td>
    <td> -</td>
    <td> - </td>
  </tr>
  <tr>
    <td> B </td>
    <td> 16 </td>
    <td> - </td>
    <td> - </td>
    <td> 17 </td> 
    <td> 20 </td>
    <td> - </td>
    <td> - </td>
  </tr>
  <tr>
    <td> C </td>
    <td> 12 </td>
    <td> - </td>
    <td> - </td>
    <td> 28 </td> 
    <td> - </td>
    <td> 31 </td>
    <td> - </td>
  </tr>
  <tr>
    <td> D </td>
    <td> 21 </td>
    <td> 17 </td>
    <td> 28 </td>
    <td> - </td> 
    <td> 18 </td>
    <td> 19 </td>
    <td> 23 </td>
  </tr>
  <tr>
    <td> E </td>
    <td> - </td>
    <td> 20 </td>
    <td> - </td>
    <td> 18 </td> 
    <td> - </td>
    <td> - </td>
    <td> 11 </td>
  </tr>
  <tr>
    <td> F </td>
    <td> - </td>
    <td> - </td>
    <td> 31 </td>
    <td> 19 </td> 
    <td> - </td>
    <td> - </td>
    <td> 27 </td>
  </tr>
  <tr>
    <td> G </td>
    <td> - </td>
    <td> - </td>
    <td> - </td>
    <td> 23 </td> 
    <td> 11 </td>
    <td> 27 </td>
    <td> - </td>
  </tr>
</table>

Cependant, il est possible d'optimiser le reseau en retirant des arêtes et toujours assurer que chaque points du réseau reste connecté. Le réseau qui réussit le maximum d'économie est montré ci-dessous. Il a un poids de 93, représentant une économie de 243 − 93 = 150 par rapport au réseau d'origine.

![Matrice minimale](https://projecteuler.net/project/images/p107_2.gif)

En utilisant la matrice donnée ci-dessous,  correspondant à un réseau de 40 sommets, trouver l'économie maximum qui peut être réalisée en retirant des arêtes du réseau mais en assurant que tous les sommets restent connectés entre eux.

On affichera le résultat avec `print`.

@[Minimal network]({"stubs": ["Defis/Euler_107.py"], "command": "python3 Defis/Euler_107_Test.py"})

---

# Equation diphantienne réciproque I
`Difficulté : Moyen (30%)`
`Origine : Projet Euler n°108`

Considérons l'équation suivante pour x, y et n des entiers positifs :

$`\dfrac 1 x+ \dfrac 1 y = \dfrac 1 n`$

Pour n=4, il y a exactement trois solutions distinctes :

$`\dfrac 1 5+ \dfrac 1 {20} = \dfrac 1 4`$  
$`\dfrac 1 6+ \dfrac 1 {12} = \dfrac 1 4`$  
$`\dfrac 1 8+ \dfrac 1 {8} = \dfrac 1 4`$  

Quelle est la plus petit valeur de n pour laquelle le nombre de solutions distinctes dépasse 1000 ?

Ce problème est une version plus facile du problème 110. Il est fortement conseillé de le résoudre en premier.

On affichera le résultat avec `print`.

@[Equation diphantienne réciproque I]({"stubs": ["Defis/Euler_108.py"], "command": "python3 Defis/Euler_108_Test.py"})

---

# 
`Difficulté : Moyen (30%)`
`Origine : Projet Euler n°109`


On affichera le résultat avec `print`.

@[Equation diphantienne réciproque I]({"stubs": ["Defis/Euler_108.py"], "command": "python3 Defis/Euler_108_Test.py"})

---

# Equation diphantienne réciproque II
`Difficulté : Moyen (40%)`
`Origine : Projet Euler n°110`

Considérons l'équation suivante pour x, y et n des entiers positifs :

$`\dfrac 1 x+ \dfrac 1 y = \dfrac 1 n`$

Pour n=4, il y a exactement trois solutions distinctes :

$`\dfrac 1 5+ \dfrac 1 {20} = \dfrac 1 4`$  
$`\dfrac 1 6+ \dfrac 1 {12} = \dfrac 1 4`$  
$`\dfrac 1 8+ \dfrac 1 {8} = \dfrac 1 4`$  

Quelle est la plus petit valeur de n pour laquelle le nombre de solutions distinctes dépasse quatre million ?

Ce problème est une version plus difficile du problème 108. Il est fortement conseillé de le résoudre en premier.

On affichera le résultat avec `print`.

@[Equation diphantienne réciproque II]({"stubs": ["Defis/Euler_110.py"], "command": "python3 Defis/Euler_110_Test.py"})

---
