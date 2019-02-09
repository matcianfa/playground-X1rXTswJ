# Différents programmes liés à la physique chimie

Cette page et les suivantes ne sont pas des pages d'exercices mais plutôt quelques exemples de programmes qui sont en rapport avec le programme de physique chimie qui pourront servir de modèles pour les enseignants.


1. Fonction qui donne le ph  
::: Une version fonctionnelle :
```python
#Donner le pH à  partir de la concentration c=[H30+]
def pH(c):
    return -log10(c)
```
:::  
::: Voici une version plus intéractive :
```python
#Demande la concentration et affiche le ph
def pH():
    c=eval(input("Entrer la concentration : "))
    print("Le PH est",-log10(c))

#Pour lancer :
pH()
```
:::  
2. Fonction qui donne les composantes selon x et y d'un vecteur vitesse en fonction de sa norme et l'angle par rapport à l'horizontale  
::: Dérouler pour voir le code
```python
from math import *

# Fonction qui donne v_x et v_y en fonction de la norme de v et de l'angle en degré par rapport à  l'horizontale
def coord_v(norme, angle):
    return norme*cos(radians(angle)),norme*sin(radians(angle))
```
:::  
3. Convertir une quantité en mole

::: Dérouler pour voir le code
```python
# Convertir une quantite en mole
def convertir_mole(n):
    Na= 6.02214076*10**23
    return n/Na
```
:::

