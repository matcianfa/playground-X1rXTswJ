# Calcul de distances à vol d'oiseau

Lorsqu'on regarde une carte de la Terre et que l'on souhaite aller d'un point à un autre, le plus court chemin n'est pas forcément la ligne droite sur la carte. De manière naturelle, cette plus courte distance est la distance à vol d'oiseau (ce plus court chemin s'appelle aussi l'orthodromie). Pour plus d'explication, vous pouvez aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Orthodromie)

Le but de cet exercice est de calculer la distance à vol d'oiseau entre deux endroits A et B dont on connait la latitude et longitude (que l'on obtient facilement [ici](https://www.coordonnees-gps.fr/) par exemple). 

Pour cela, on utilisera la formule suivante, valable pour des petites distances par rapport au rayon de la terre : 
1. $`x=(longitude_B-longitude_A).cos\left(\frac{latitude_A+latitude_B}{2}\right)`$
2. $`y=latitude_B-latitude_A`$
3. $` distance = rayon.\sqrt{x^2+y^2}`$


+ On prendra pour le rayon de la Terre la valeur 6 371 km
+ On fera bien attention au fait que les latitudes et longitudes dans ces formules doivent être en radians alors que celles qu'on a en entrée seront en degrés. On n'oubliera donc pas de les multiplier par $`\frac \pi{180}`$ pour passer des degrés en radians.
+ De plus, les résultats devront être arrondis au mètre près. Pour cela, on utilisera la fonction `round( nombre , nombre_de_chiffres_après_la_virgule)`.

> Entrée : Les latitudes et longitudes des deux points en degrés.

> Sortie : La distance à vol d'oiseau entre ces deux points, arrondie au mètre près.

@[Calcul de distances à vol d'oiseau]({"stubs": ["Variables_et_fonctions/Calcul_distance_vol_oiseau.py"], "command": "python3 Variables_et_fonctions/Calcul_distance_vol_oiseau_Test.py"})


### Pour aller plus loin :

Vous pouvez tester votre programme avec vos propres valeurs. Pour cela, il suffit de récupérer les latitudes et longitudes des lieux sur ce site : [www.coordonnees-gps.fr](https://www.coordonnees-gps.fr/).

Puis tout en bas de votre programme et sans indentation il suffit de taper `print(mon_programme(latitude_A, longitude_A,latitude_B,longitude_B))`en remplaçant latitude_A, longitude_A, latitude_B et longitude_B par vos valeurs.
