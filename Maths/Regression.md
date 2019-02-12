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

