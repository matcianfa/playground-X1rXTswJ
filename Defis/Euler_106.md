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
