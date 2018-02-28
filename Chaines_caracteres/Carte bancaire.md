## Vérification d'une carte bancaire
`Difficulté : moyenne`

Sur le devant d'une carte bancaire, on peut lire 16 chiffres. Les 15 premiers ont une signification (identification de la banque, du numéro de compte...) et le 16e est une clé de vérification qui permet de savoir s'il y a eu une erreur en recopiant le numéro par exemple. 

Pour vérifier si un numéro est valide, on considère les 16 chiffres de la carte. 
- On commence par multiplier par deux tous les chiffres de rang impair (le premier, le troisième etc.). Si le résultat de la multiplication par deux dépasse 9, on soustrait 9. 
- On additionne tous les chiffres du numéro obtenu après ces multiplications par deux. 
- Si le résultat est un multiple de 10 alors le numéro est valide. Sinon, il ne l'est pas. 

::: Exemple
Si le numéro est 1234561234561234. 
+ On multiplie les numéros de rangs impairs (en soustrayant 9 si la valeur dépasse 9) donc ce numéro devient : 2264162264162264
+ On additionne tous les chiffres obtenus : On obtient 56.
+ Comme 56 n'est pas divisible par 10, ce numéro est "NON VALIDE".
:::

Le but de cet exercice est de dire si le ***numero*** donnée en entrée est "VALIDE" ou "NON VALIDE".

> Entrée : Un ***numero***.

> Sortie : Afficher si ce ***numero*** est un numéro de carte bancaire "VALIDE" ou "NON VALIDE".

@[Validité d'un numéro de carte bancaire]({"stubs": ["Chaines_caracteres/Carte_bancaire.py"], "command": "python3 Chaines_caracteres/Carte_bancaire_Test.py"})
