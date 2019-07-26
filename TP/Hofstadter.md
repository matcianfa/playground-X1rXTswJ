# La suite Q de Hofstadter
`Difficulté : Moyenne`  
`Prérequis : Les listes

On appelle la suite Q de Hofstadter la suite suivante :  
$`\left\lbrace\begin{array}{l} Q_1=1 \\ Q_2=1 \\ Q_n=Q_{n-Q_{n-1}} + Q_{n-Q_{n-2}}\end{array}\right.`$

Elle "ressemble" un peu dans sa définition à la suite de Fibonacci. Elle est remarquable car assez peu de choses sont démontrées sur elle bien qu'on puisse l'observer assez facilement. Le but de cette page est de la représenter graphiquement pour pouvoir observer ses variations chaotiques.

## Calcul des termes

Créer un programme $`Q(n)`$ qui prend en entrée un entier naturel n non nul et donne en sortie la liste de tous les termes de la suite de 1 jusqu'à n.

@[Calcul des termes]({"stubs": ["TP/Hofstadter.py"], "command": "python3 TP/Hofstadter_Test.py"})
