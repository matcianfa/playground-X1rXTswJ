# Cours : Régressions linéaires et d'ordre 2

Nous allons voir dans cette partie comment calculer et afficher des droites et paraboles de régression.

La fonction au coeur de la régression est `polyfit` du module `numpy`. Pour l'utiliser il faut donc importer le module `numpy`. Elle s'utilise de la façon suivante :

```python
import numpy as np

a,b,c = np.polyfit(X,Y,2)
```
Dans ce qui précède, X et Y désignent respectivement la liste des abscisses et des ordonnées des points du nuage de points et 2 est le degré de la régression. Ici on veut donc approximer le nuage par un polynôme qui sera de la forme ax²+bx+c. `np.polyfit` renvoie donc les coefficients.

# Régression linéaire

Voici un exemple graphique de regression linéaire :

@[Tracé de la droite de régression]({"stubs": ["Maths/Reg_lin.py"], "command": "python3 Maths/Reg_lin_Test.py"})


# Régression d'ordre 2

On peut utiliser des régressions d'ordre 2 lorsqu'on étudie le mouvement d'un objet par exemple. On récupère les coordonnées des points par chronophotographie par exemple ( on peut aller voir [cette partie](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/chronophotographie) pour voir comment faire) puis on calcule la parabole de régression pour gommer un peu les imprécisions dues à la récupération des données.

Voici un exemple :

@[Tracé de la parabole de régression]({"stubs": ["Maths/Reg_pol.py"], "command": "python3 Maths/Reg_pol_Test.py"})
