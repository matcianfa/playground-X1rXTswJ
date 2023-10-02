# Plouf plouf

Rappelons les règles du plouf-plouf : on se place en cercle et quelqu'un pointe du doigt une personne et commence à chanter plouf plouf et une petite chanson. A chaque mot ou syllabe de la chanson, il décale son doigt vers la personne suivante, toujours dans le même sens. Quand la chanson s'arrête, la personne désignée du doigt est éliminé. La question est simple : Où se placer pour gagner ?

Modélisons la situation : On appelle ***n** le nombre de personnes et ***k*** le nombre de syllabes de la chanson. De plus, on numérote les personnes de 0 à n-1 en commençant par la personne désignée en premier.

Par exemple s'il y a 5 personnes et que la chanson est 'am-stram-gram', alors k vaut 3 et les personnes éliminées seront dans l'ordre : 2 - 0 - 4 - 1 et le gagnant sera donc le 3. Attention au début, le 'am' commence sur 0.

Points importants pour pouvoir programmer :
+ On remarque que dans cette façon de compter, après n-1, il y a 0. Ca tombe bien, c'est exactement comme si on regardait uniquement les restes de la division euclidienne par n (qui est donné avec % en python). Si je reprends l'exemple précédent, une fois éliminé le numéro 2, je compte 3 de plus j'obtiens 5. Si je garde le reste de la division euclidienne par n=5 j'obtiens 0. D'où l'élimination du 0 ensuite. 
+ Nous allons programmer la fonction ***plouf_plouf*** de manière récursive et pour cela, on a la formule : 
```math
plouf\_plouf(1,k)=0 \quad et \quad
plouf\_plouf(n,k)=(plouf\_plouf(n-1,k)+k)\%n
```
(Si quelqu'un a une explication claire pour cette formule, je suis preneur pour la mettre ici).

> Entrée : Deux entiers ***n*** et ***k***.

> Sortie : Une fonction ***plouf_plouf(n,k)*** qui renvoie la position du gagnant (avec `return`).

@[Plouf plouf]({"stubs": ["Les_fonctions/plouf_plouf.py"], "command": "python3 Les_fonctions/plouf_plouf_Test.py"})
