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

# Flechettes
`Difficulté : Moyen (45%)`
`Origine : Projet Euler n°109`

Au jeu de flechettes, un joueur lance 3 flechettes sur une cible qui est divisée en 20 secteurs égaux numérotés de 1 à 20.

![Cible](https://projecteuler.net/project/images/p109.gif)

Le score d'une flechette est déterminé par le nombre du secteur dans lequelle elle est tombée. Une flechette qui tombe en dehors du cercle rouge et vert extérieur compte pour 0. Les parties de couleur noire ou crème représentent un score simple. Cependant, les cercles rouges et verts extérieurs et intérieurs représentent un score doublé et triplé respectivement.

Au centre de la cible il y a un anneau vert qui rapporte 25 points et un disque rouge qui rapporte 50 points.

Il y a différentes règles mais les plus populaires sont que le joueur commence avec un score de 301 ou 501 et le premier joueur à réduire son total à 0 gagne. Cependant, pour gagner, il faut faire un double (y compris le double au centre de la cible) sur sa fleche qui fait descendre en dessous de 0. Toutes les autres flechettes qui réduise le score en dessous de 1 ne suffisent pas pour gagner.

Quand un joueur est capable de finir à partir de son score, on dit que c'est un "check out" et le plus grand checkout est 170 : T20 T20 D25 (2 triples 20 et un double 25 au centre de la cible)

Il y a exactement 11 différentes façon d'obtenir un check out de 6 :

D3  
D1 	D2   	 
S2 	D2 	   
D2 	D1 	   
S4 	D1 	   
S1 	S1 	D2  
S1 	T1 	D1  
S1 	S3 	D1  
D1 	D1 	D1  
D1 	S2 	D1  
S2 	S2 	D1  

Il faut remarquer que D1 et D2 sont considérés comme différents car ils finissent par des doubles différents. Cependant, S1 T1 D1 et T1 S1 D1 sont considérés comme identiques.

De plus, On n'inclut pas les manqués dans les combinaisons considérées. Par exemple D3 et identique ) 0 D3 et 0 0 D3.

Il y a 42336 différents check out en tout.

Combien de façons différentes existent il pour un joueur de faire un check-out s'il a un score inférieur strictement à 100 ?

On affichera le résultat avec `print`.

@[Flechettes]({"stubs": ["Defis/Euler_109.py"], "command": "python3 Defis/Euler_109_Test.py"})

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
