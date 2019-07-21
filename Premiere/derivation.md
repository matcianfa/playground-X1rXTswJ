# Première : Analyse : Dérivation, études de fonctions, exponentielle et fonctions trigonométriques

## Exercice n° : Taux d'accroissement
`Difficulté : Facile`  

Ecrire une fonction qui prend en entrée une fonction $`f`$ et des réels $`a`$ et $`h`$ et donne en sortie le taux de variation (ou d'accroissement) de la fonction $`f`$ entre le point d'abscisse $`a+h`$ et $`a`$.

@[Taux d'accroissement]({"stubs": ["Premiere/Derivation/taux_accroissement.py"], "command": "python3 Premiere/Derivation/taux_accroissement_Test.py"})

---

## Exercice n° : Ecrire la liste des coefficients directeurs des sécantes pour un pas donné
`Difficulté : Moyenne`  
`Prérequis : Les listes`  
`Programme officiel`

On considère $`\mathcal{C}`$ la courbe représentative d'une fonction $`f`$ dans un repère, $`A`$ un point d'abscisse $`a`$ de $`\mathcal{C}`$ et $`B`$ celui d'abscisse $`a+h`$. 

![Sécantes](secantes.jpg)

Compléter la fonction ci-dessous pour qu'elle permette de calculer la liste des coefficients directeurs des sécantes (ou cordes) (AB) pour h variant de 1 à 0 avec un pas de 0,01. 

@[la liste des coefficients directeurs des sécantes pour un pas donné]({"stubs": ["Premiere/Derivation/liste_coeff.py"], "command": "python3 Premiere/Derivation/liste_coeff_Test.py"})

---

## Exercice n° : Donner la mesure principale d'un angle 
`Difficulté : Moyenne`

Créer une fonction qui prend en entrée un angle en radian et donne en sortie la mesure principale ( dans $`]-\pi; \pi]`$) de cet angle.

@[Mesure principale d'un angle]({"stubs": ["Premiere/Derivation/mesure_principale.py"], "command": "python3 Premiere/Derivation/mesure_principale_Test.py"})

---

## Exercice n° : Donner la mesure principale d'un angle (version améliorée I)
`Difficulté : Moyenne`

La version précédente donne une valeur approchée de la mesure principale. C'est pratique pour vérifier si le calcul qu'on a fait est juste mais ne nous donne pas la réponse comme on souhaiterait l'écrire sur notre feuille (c'est à dire de la forme $`\dfrac{3\pi}{5}`$ au lieu de 1.8849555921538759 par exemple).

Pour améliorer un peu cela, il suffit de travailler avec le nombre qui multiplie $`\pi`$ au lieu de travailler avec l'angle en entier. Une façon de voir les choses est de considérer $`\pi`$ comme une unité.

> Exemple : si on cherche la mesure principale de $`\dfrac{13\pi}{4}`$, on considère le nombre $`\dfrac{13}{4}`$, on lui retire autant de 2 que nécessaire pour être en -1 et 1. On trouve ici $`dfrac{1}{4}`$.

Donc si on part d'un angle quelconque, il faut d'abord le diviser par $`\pi`$ puis retirer ou ajouter autant de 2 que necessaire au résultat pour être entre -1 et 1. On aura juste à afficher $`\pi`$ derrière pour avoir la mesure principale.

Créer une fonction qui prend en entrée un angle et donne en sortie la mesure principale sous la forme $`nombre\pi`$

> Exemple : Si l'angle donné en entrée est $`\dfrac{7\pi}2`$ (c'est à dire 10.995574287564276) alors en sorti, il devra afficher "-0.5pi"

@[Mesure principale d'un angle]({"stubs": ["Premiere/Derivation/mesure_principale2.py"], "command": "python3 Premiere/Derivation/mesure_principale2_Test.py"})

# Pour aller plus loin 

Voici quelques approfondissements possibles :
- [Recherche de solutions par dichotomie](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-recherche-par-dichotomie)
- [La méthode d'Euler](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-deuler)
- [La méthode de Newton](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-de-newton)
- [La méthode d'Archimède](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/methode-darchimede)
