# Nombres premiers avec répétitions de chiffres
`Difficulté : Moyen (45%)`
`Origine : Projet Euler n°111`

En considérant les nombres premiers de quatre chiffres qui se répètent, il est clair qu'ils ne peuvent pas être tous identiques : 1111 est divisible par 11, 2222 par 22 ... Cependant, il y a neuf nombres de quatre chiffres qui contiennent trois 1 :

1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111

On notera M(n,d) le nombre maximum de chiffres d répétés dans un nombre premier de n chiffres, N(n,d) le nombre de tels nombres premiers et S(n,d) la somme de tous ces nombres premiers.

Par exemple, M(4,1)=3 est le nombre maximum de répétition de 3 dans un nombre premier de quatre chiffres, il y a N(4,1)=9 nombres premiers ainsi et la somme de ces nombres est S(4,1)=22274. Pour d=0, on a seulement M(4,0)=2 répétitions possible mais N(4,0)=13 dans ce cas.

De la même façon, on peut obtenir les résultats suivants pour les nombres premiers de 4 chiffres : 

| Chiffre : d | M(4,d) | N(4,d) | S(4,d) |
|:-----------:|:------:|:------:|:------:|
| 0 | 2 | 13 | 67061 |
| 1 | 3 | 9 | 22275 |

In the same way we obtain the following results for 4-digit primes.
Digit, d 	M(4, d) 	N(4, d) 	S(4, d)
0 	2 	13 	67061
1 	3 	9 	22275
2 	3 	1 	2221
3 	3 	12 	46214
4 	3 	2 	8888
5 	3 	1 	5557
6 	3 	1 	6661
7 	3 	9 	57863
8 	3 	1 	8887
9 	3 	7 	48073

Pour d = 0 à 9, la somme de tous les S(4,d) est 273700.

Trouver la somme de tous les S(10,d).

On affichera le résultat avec `print`.

@[Nombres premiers avec répétitions de chiffres]({"stubs": ["Defis/Euler_111.py"], "command": "python3 Defis/Euler_111_Test.py"})

---
