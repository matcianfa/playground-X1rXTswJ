## Passage des coordonnées cartésiennes à polaires

Le but de cet exercice est de créer un programme qui reçoit les coordonnées cartésiennes et les transforme en coordonnées polaires. C'est le l'inverse du programme qu'on a fait dans le chapitre précédent. On pourra trouver plus d'informations sur les coordonnées polaires par exemple ici : [Wikipédia](https://fr.wikipedia.org/wiki/Coordonn%C3%A9es_polaires)

Entre autre, voici une des façons d'obtenir les valeurs de $`r`$ et $`\theta`$ :
+ $`r=\sqrt{x^2+y^2}`$
+ $`\theta=\left\{\begin{array}{ll} arctan\left(\frac{y}{x}\right) & \textrm{si } x>0 \\ arctan\left(\frac{y}{x}\right) + \pi & \textrm{si } x<0\ et \ y\geq 0 \\ arctan\left(\frac{y}{x}\right) - \pi & \textrm{si } x<0\ et \ y<0 \\ \dfrac \pi 2 & \textrm{si } x=0\ et\ y>0 \\ -\dfrac \pi 2 & \textrm{si } x=0\ et\ y>0 \end{array}\right.`$

> Entrée : Les coordonnées cartésiennes ***x*** et ***y***.

> Sortie : Les coordonnées polaires correspondantes ***r*** et ***theta*** arrondies à 3 chiffres après la virgule.

@[Passage coordonnées cartésiennes à polaires]({"stubs": ["Les_conditions/passage_cartesiennes_polaires.py"], "command": "python3 Les_conditions/passage_cartesiennes_polaires_Test.py"})
