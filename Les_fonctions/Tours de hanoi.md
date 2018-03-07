# Tours de Hanoï
`Difficulté : moyenne`

Les tours de Hanoï est un casse-tête composé de trois tours et une pile de disques rangés du plus grand au plus petit comme sur la photo ci-dessous . 

![Photo tours de Hanoï](https://upload.wikimedia.org/wikipedia/commons/thumb/0/07/Tower_of_Hanoi.jpeg/260px-Tower_of_Hanoi.jpeg)

Le but est de déplacer la pile de disques sur la tour de droite en ne déplaçant à chaque fois qu'un seul disque et un disque ne peut pas être posé sur un disque plus petit. Voici une animation de ce qu'il faut faire dans le cas où il y a 4 disques.

![Anim Hanoï](https://upload.wikimedia.org/wikipedia/commons/thumb/6/60/Tower_of_Hanoi_4.gif/260px-Tower_of_Hanoi_4.gif)

On peut aller voir [Wikipédia](https://fr.wikipedia.org/wiki/Tours_de_Hano%C3%AF) par exemple pour plus d'informations.

Nous allons voir qu'il est très simple de créer un programme récursif qui nous dit quoi faire pour résoudre le problème. Tout d'abord on appelle les tours A, B et C. On appelle ***n*** le nombre de disque présents au départ dans la tour A. Pour déplacer tous les disques de la tour A vers la tour C, on peut raisonner comme suit : 
+ On déplace n-1 disques de A vers la tour B
+ On déplace le dernier disque de A vers C
+ On déplace les n-1 disques de B vers C



