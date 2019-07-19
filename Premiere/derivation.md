# Première : Dérivation et applications

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

# Pour aller plus loin 

Voici quelques approfondissements possibles :
- [Recherche de solutions par dichotomie](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-recherche-par-dichotomie)
- [La méthode d'Euler](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-deuler)
