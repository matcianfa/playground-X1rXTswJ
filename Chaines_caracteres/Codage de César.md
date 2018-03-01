## Codage de César et Vigenère

### Codage de César

Le codage de César est un manière de crypter un message de manière simple : On choisit un nombre (appelé clé de codage) et on décale toutes les lettres de notre message du nombre choisi.

Par exemple : Si je choisis comme clé le nombre 2. Alors la lettre A deviendra C, le B deviendra D ... et le Z deviendra B.
Ainsi, le mot MATHS deviendra une fois codé OCVJU.

On remarquera facilement que pour décoder, il suffit de faire la même chose mais avec l'opposé de la clé (ici -2) comme clé.

Le but de cet exercice est de créer un programme qui reçoit en entrée une clé de codage ***n*** et un ***message*** à coder et qui doit afficher le message codé correspondant.

> Entrée : La clé ***n*** (qui peut être négative) et un ***message*** en majuscule sans accent à coder.

> Sortie : Le message codé par la méthode de César avec la clé ***n***. La ponctuation et espaces ne doivent pas changer.

@[Codage de César]({"stubs": ["Chaines_caracteres/Codage_cesar.py"], "command": "python3 Chaines_caracteres/Codage_cesar_Test.py"})

---

### Codage de Vigenère

Tout comme le codage de César, pour appliquer un codage de Vigenère il faut décaler les lettres mais pas toutes du même nombre. La clé est cette fois-ci un ***mot_clé*** dont chaque lettre nous donne le décalage à effectuer (en prenant A pour un décalage de 0, B pour un décalage de 1 ...). 

Prenons un exemple pour expliquer la méthode : Imaginons que le ***mot_clé*** soit "MATHS" et le mot à coder "PYTHON". 
1. Pour coder P, je décale du nombre correspondant à M c'est à dire 12 (car on commence à 0 avec A) ce qui me donne B comme codage pour P. 
2. Passons au Y : Je le décale du nombre correspondant au A c'est à dire 0 donc Y est le codage de Y ici. 
3. Passons au T qui se décale du nombre correspondant à T c'est à dire 19 donc T devient une fois décalé M 
4. Ainsi de suite. 

Si notre ***mot_clé*** est trop court on recommence au début du mot c'est à dire que N sera décalé du nombre correspondant à M.

Le but de cet exercice est de créer un programme qui reçoit en entrée un ***mot_clé*** et un ***mot*** à coder et qui affiche le mot codé par cette méthode.

> Entrée : Un ***mot_clé*** et un ***mot*** à coder écrits en majuscules et sans accent.

> Sortie : Le mot codé par la méthode de Vigenère en majuscule.

@[Codage de Vigenère]({"stubs": ["Chaines_caracteres/Codage_vigenere.py"], "command": "python3 Chaines_caracteres/Codage_vigenere_Test.py"})
