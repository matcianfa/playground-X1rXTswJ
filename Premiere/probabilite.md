# Première : Probabilités


## Exercice n° : Recherche d'une probabilité inconnue
`Difficulté : Moyenne`  
`Prérequis : Les listes`

On va simuler le lancer d'un verre en plastique . Ce verre peut se retrouver dans trois positions : $`\cap`$, $`\subset`$ (ou $`\supset`$ mais c'est pareil que $`\subset`$ ) ou $`\cup`$. On numérote ces positions de 1 à 3.

Pour simuler le lancer du verre, il faut utiliser la fonction $`lancer()`$ qui renverra le résultat du lancer sous la forme 1, 2 ou 3.

Créer une fonction qui renvoie la liste des approximations (à 0.01 près) des probabilités de chaque position dans l'ordre.

@[Recherche d'une probabilité inconnue]({"stubs": ["Premiere/Probabilite/proba_inconnue.py"], "command": "python3 Premiere/Probabilite/proba_inconnue_Test.py"})

---

## Exercice n° : Somme de nombres aléatoires
`Difficulté : Moyenne`  

La fonction `random()` du module `random` donne un nombre aléatoire dans l'intervalle `[0;1[`. 

On s'amuse à relancer plusieurs fois cette fonction jusqu'à ce que la somme des nombres obtenus dépasse 1. On se demande alors combien faut-il, en moyenne, additionner de nombres pris au hasard dans `[0;1[` pour dépasser 1 ?

Pour trouver une approximation de ce nombre moyen, créer une fonction qui simule 10 millions d'expériences et renvoie ce nombre moyen. Vers quel nombre vu cette année semble-t-il se rapprocher ?

@[Recherche d'une probabilité inconnue]({"stubs": ["Premiere/Probabilite/somme_nb_alea.py"], "command": "python3 Premiere/Probabilite/somme_nb_alea_Test.py"})

---

## Approfondissements

Voici quelques approfondissements possibles :
- [Fréquences d'apparition des lettres dans un texte](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/frequences-dapparitions-de-lettres)
- [Méthode de Monte Carlo](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/la-methode-de-monte-carlo)
- [Simulation de l'Euromillion](https://tech.io/playgrounds/17176/recueil-dexercices-pour-apprendre-python-au-lycee/simulation-de-leuromillion)
