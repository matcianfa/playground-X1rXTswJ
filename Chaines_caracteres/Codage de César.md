## Codage de César

Le codage de César est un manière de crypter un message de manière simple : On choisit un nombre (appelé clé de codage) et on décale toutes les lettres de notre message du nombre choisi.

Par exemple : Si je choisis comme clé le nombre 2. Alors la lettre A deviendra C, le B deviendra D ... et le Z deviendra B.
Ainsi, le mot MATHS deviendra une fois codé OCVJU.

On remarquera facilement que pour décoder, il suffit de faire la même chose mais avec l'opposé de la clé (ici -2) comme clé.

Le but de cet exercice est de créer un programme qui reçoit en entrée une clé de codage ***n*** et un ***message*** à coder et qui doit afficher le message codé correspondant.

> Entrée : La clé ***n*** (qui peut être négative) et un ***message*** en majuscule sans accent à coder.

> Sortie : Le message codé par la méthode de César avec la clé ***n***. La ponctuation et espaces ne doivent pas changer.

@[Codage de César]({"stubs": ["Chaines_caracteres/Codage_cesar.py"], "command": "python3 Chaines_caracteres/Codage_cesar_Test.py"})
