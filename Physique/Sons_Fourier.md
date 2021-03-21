# Utilisation de la transformée de Fourier discrète réelle pour récupérer les harmoniques d'un son

Le but de cette page est de voir un peu ce qui se cache derrière des compressions de sons qu'on retrouve dans des formats de sons comme le MP3 par exemple. Elle est déstinée à des lycéens et/ou curieux donc nous présenterons seulement ce qu'est la transformée de Fourier discrète réelle et comment l'implémenter à la main en python pour la voir fonctionner. 

## La théorie

Nous avons vu, page précèdente, qu'un son wave est simplement une suite de données joué à une certaine fréquence. Notons $`N`$ la taille de ces données et $`d_n`$ la donnée d'indice $`n`$. A partir de cette suite de données, on peut en créer 2 qu'on appelle coefficients de Fourier réels  dont les formules sont :
``` math
a_k =\displaystyle \sum_{n=0}^{N-1} d_n cos\left(\dfrac{2\pi kn}{N}\right)
```
et 
```math
b_k =\displaystyle \sum_{n=0}^{N-1} d_n sin\left(\dfrac{2\pi kn}{N}\right)
```

On a alors le miracle suivant : à partir de ces deux suites, on peut retrouver celle de départ par la formule d'inversion :

```math
d_n = \displaystyle \dfrac 1 N \sum_{k=0}^{N-1} a_k cos\left(\dfrac{2\pi kn}{N}\right) + b_k sin\left(\dfrac{2\pi kn}{N}\right)
```

:::Exemple à la main
Si je considère le "son" dont les données sont $`[1,2,-1]`$. On a alors avec les notations $`N=3`$, $`d_0=1`$, $`d_1=2`$ et $`d_2=-1`$.  
Calculons les coefficients :
- $`a_0 = d_0*cos\left(\dfrac{2\pi*0*0}{3}\right) + d_1*cos\left(\dfrac{2\pi*0*1}{3}\right) + d_2*cos\left(\dfrac{2\pi*0*2}{3}\right)`$  
  $`a_0 = 1*1+2*1+(-1)*1 = 2`$
- $`a_1 = d_0*cos\left(\dfrac{2\pi*1*0}{3}\right) + d_1*cos\left(\dfrac{2\pi*1*1}{3}\right) + d_2*cos\left(\dfrac{2\pi*1*2}{3}\right)`$  
  $`a_1 = 1*1+2*\left(-\dfrac{1}{2}\right)+(-1)*\left(-\dfrac{1}{2}\right) = \dfrac{1}{2}`$
- $`a_2 = d_0*cos\left(\dfrac{2\pi*2*0}{3}\right) + d_1*cos\left(\dfrac{2\pi*2*1}{3}\right) + d_2*cos\left(\dfrac{2\pi*2*2}{3}\right)`$  
  $`a_2 = 1*1+2*\left(-\dfrac{1}{2}\right)+(-1)*\left(-\dfrac{1}{2}\right) = \dfrac{1}{2}`$
Pour les coefficients $`b_k`$ les calculs sont très similaires et on obtient $`b_0 = 0`$, $`b_1 = \dfrac{3\sqrt{3}}{2}`$ et $`b_2 = \dfrac{3\sqrt{3}}{2}`$.

Utilisons maintenant la formule d'inversion pour se convaincre qu'elle marche bien :
- $`\dfrac 1 3 \left(a_0*cos\left(\dfrac{2\pi*0*0}{3}\right) + b_0*sin\left(\dfrac{2\pi*0*0}{3}\right) + a_1*cos\left(\dfrac{2\pi*1*0}{3}\right) +\right.`$  
  $`\qquad\qquad \left.b_1*sin\left(\dfrac{2\pi*1*0}{3}\right) + a_2*cos\left(\dfrac{2\pi*2*0}{3}\right)+ b_2*sin\left(\dfrac{2\pi*2*0}{3}\right)\right)`$  
  $`= \dfrac 1 3\left(2*1 + 0*0 + \dfrac 1 2 * 1 + \dfrac{3\sqrt 3}2 * 0 + \dfrac 1 2 * 1 + \dfrac{3\sqrt 3}2 * 0 \right)= 1 = d_0`$
- $`\dfrac 1 3 \left(a_0*cos\left(\dfrac{2\pi*0*1}{3}\right) + b_0*sin\left(\dfrac{2\pi*0*1}{3}\right) + a_1*cos\left(\dfrac{2\pi*1*1}{3}\right) +\right.`$  
  $`\qquad\qquad \left.b_1*sin\left(\dfrac{2\pi*1*1}{3}\right) + a_2*cos\left(\dfrac{2\pi*2*1}{3}\right)+ b_2*sin\left(\dfrac{2\pi*2*1}{3}\right)\right)`$  
  $`= \dfrac 1 3\left(2*1 + 0*0 + \dfrac 1 2 * \left(-\dfrac 1 2\right) + \dfrac{3\sqrt 3}2 * \dfrac{\sqrt 3}2 + \dfrac 1 2 * \left(-\dfrac 1 2\right) + \dfrac{3\sqrt 3}2 * \left(-\dfrac{\sqrt 3}2\right \right)= 2 = d_1`$
- Je vous laisse le plaisir de prouver que le dernier calcul donne -1...
:::

Quelques précisions encore : En utilisant les formules de trigonométrie classiques, on peut trouver un $`\varphi_k`$ tel que les termes des sommes peuvent s'écrire :  
```math
a_k cos\left(\dfrac{2\pi kn}{N}\right) + b_k sin\left(\dfrac{2\pi kn}{N}\right) = \sqrt{a_k^2 + b_k^2} cos\left(\dfrac{2\pi kn}{N} + \varphi_k\right)
```

## La pratique 
On peut se demander quel est l'intérêt de faire tous ces calculs avec les données de notre son si au final on retrouve les mêmes qu'au départ. Nous allons voir que c'est pourtant extrêment astucieux. En effet, une fois nos $`d_n`$ écrits sous la forme de somme de cosinus, on peut alors les interpreter comme la somme de signaux fondamentaux (des sons "purs", sinusoidaux). Or notre oreille n'entend (en prenant large mais on pourrait réduire) que les fréquences ente 20hz et 20 000 Hz. Donc tous les termes qui correspondent à des fréquences en dehors de cette plage peuvent être éliminés de notre son.  
De plus, tous les coefficients $`a_k`$ ou $`b_k`$ trop petits peuvent être éliminé aussi puisqu'ils n'interviennent que peu dans le son donc nous ne verrons pas la différence en écoutant.  
Cette simple réecriture de nos données en somme de Fourier nous permet donc naturellement d'éliminer un grand nombre de données et ainsi réduire la place nécessaire pour stocker notre son. Bien sûr les compressions comme le MP3 sont un peu plus optimales encore que cette méthode mais elles en sont grandement inspirées.

### Le codage 
Je vais me contenter d'expliquer l'idée général du code ci-dessous. 
Tout d'abord, le code est séparé en 2 onglets : le premier où on  travaille sur notre son et le second où sont regroupées les fonctions calculatoires en lien avec les coefficients de Fourier.  

Commençons par le second onglet : Il contient les fonctions correspondant à la théorie présentées ci-dessus. Une qui calcule les coefficients de Fourier. Une qui donne le coefficient si on regroupe le cosinus et le sinus en un seul cosinus. Enfin une fonction d'inversion qui redonne les coefficients initiaux à partir des coefficients de Fourier. Comme sur ce site on est limité à 30 sec de calculs, on est obligé d'utiliser numpy pour accélérer grandement nos calculs. Ils respectent cependant les calculs présentés dans la partie théorique.

Le premier onglet est normalement assez lisible. On charge les données de notre son. On ne peut malheureusement pas faire le traitement avec toutes les données (car le temps de calcul est trop limité sur ce site) donc on coupe un peu la fin du son et on ne garde qu'une donnée sur 3. Du coup notre fréquence d'échantillonage est divisée par 3 aussi.  
On calcule ensuite les coefficients de Fourier de notre son. Comme dit précédemment, il ne sert à rien de conserver les coefficients correspondant à des fréquence trop haute. On choisit de couper ici à 4000Hz ce qui est en gros la note la plus aigue d'un piano. On cherche alors à quel indice $`k`$ va correspondre cette fréquence à partir de laquelle on décide de couper. C'est une simple règle de proportionnalité qui donne $`k_{max} = \dfrac{f_{max}}{f_{echantillon}} taille_{echantillon}`$.  
On affiche ensuite les coefficients harmoniques en fonction des frequences. Ce graphique est important car il permet de voir quelles frequences fondamentales se trouve dans notre son. Ici on peut voir qu'il y a un gros pic pour la frequence 440hz (Normal puisque le son représente un LA joué au piano) mais aussi un pic pour les multiples de 440 : 880hz, 1320 hz, 1760 hz, 2200 hz... qui correspondent respectivement à un LA(à l'octave), un MI, un LA (2 octaves au dessus) et un DO#. Donc en réalité, quand on joue une note avec un instrument, le son n'est pas pur mais au contraire il y a plusieurs notes dans une. Par exemple les notes LA+MI+DO# forment l'accord de LA Majeur. Autre remarque : ce qui permet de différencier des instruments (on reconnait très facilement si un LA est joué au piano ou à la guitare ou à la trompette...) c'est simplement les différences de hauteurs des pics dans ce diagramme. 
On termine le traitement de notre son en arrondissant à 0 tous les coefficients trop faibles (ici inférieur à 2 mais vous pouvez tester avec un seuil plus grand).  
Enfin on écoute le résultat après tant d'efforts. Il n'est pas si différent par rapport à l'original pourtant il contient presque 10 fois moins de coefficients.

@[Transformée de Fourier]({"stubs": ["Physique/Fourier.py","Physique/fonctions_Fourier.py"], "command": "python3 Physique/Fourier_Test.py"})

Tout ce qui précède est très perfectible. Le but était ici de montrer les idées qui sont derrière beaucoup de type de compression de données (sons, images...). Si on veut le faire plus efficacement, il vaut mieux utiliser des fonctions déjà existantes comme celles se trouvant dans le module `numpy.fft` qui vont beaucoup beaucoup beaucoup plus vite que les fonctions naives présentées ici. Mais ce n'est qu'en codant à la main les techniques qu'on les comprend vraiment. N'hésitez pas à adapter les codes précédents pour pouvoir les utiliser sur votre ordinateur où vous pourrez laisser calculer davantage et sur des sons plus longs. 

## Quelques précisions sur les fréquences harmoniques

Le fait qu'un son représenté par des valeurs discrètes soit la somme de sons "purs" n'est pas réellement une évidence à partir des formules ci-dessus. En effet, dans ces formules on a $`d_n =  \displaystyle \dfrac 1 N \sum_{k=0}^{N-1} \sqrt{a_k^2 + b_k^2} cos\left(\dfrac{2\pi kn}{N} + \varphi_k\right)`$. Or les frequences qui interviennent dépendent de $`n`$.  
Pour mieux comprendre ce qui se passe, il faut revenir à l'origine : Un son peut être vu comme une fonction $`f(t)`$ du temps. Pour pouvoir faire un traitement informatique de ce son on est obligé de prélever des données à une frequence $`frequence_{echantillon}`$. On a ainsi nos données $`(d_n)`$ pour $`n`$ allant de 0 à $`N-1`$. Autrement dit on pose $`d_0=f(0)`$, $`d_1=f\left(\dfrac 1{frequence_{echantillon}}\right)`$, $`d_2=f\left(\dfrac 2{frequence_{echantillon}}\right)`$ ...  
On traite ces données comme on a vu précédemment pour obtenir la décomposition $`d_n =  \displaystyle \dfrac 1 N \sum_{k=0}^{N-1} \sqrt{a_k^2 + b_k^2} cos\left(\dfrac{2\pi kn}{N} + \varphi_k\right)`$. Maintenant il faut revenir à la fonction d'origine $`f`$ représentant notre son en fonction du temps. Pour cela, le moyen le plus naturel en utilisant la formule précédente est de poser :
```math
\tilde f(t) = \dfrac 1 N \sum_{k=0}^{N-1} \sqrt{a_k^2 + b_k^2} cos\left(\dfrac{2\pi k  {frequence_{echantillon}}t}{N} + \varphi_k\right)
```
On remarque que pour les valeurs $`t= 0, \dfrac 1{frequence_{echantillon}}, \dfrac{2}{frequence_{echantillon}}`$... cette fonction prend exactement les mêmes valeurs que $`f`$ (qui sont $`d_0`$, $`d_1`$, $`d_2`$ ...). Cependant, $`f`$ et $`\tilde f`$ sont a priori différente en dehors de ces valeurs. Cependant, comme on choisit une frequence d'echantillonage très élevée, les différences ne sont pas audibles. Donc on peut considérer que notre son est représenté par $`\tilde f`$ et c'est cette fonction qui est la somme de sons "purs". En théorie de  $`N`$ sons purs différents d'après la formule mais en général, la plupart des coefficients $`sqrt{a_k^2 + b_k^2}`$ sont trop faibles pour qu'on les prennent en considération.  
Une dernière remarque : pour connaitre la fréquence associée au son "pur" il suffit de calculer $`frequence_harmonique = \dfrac{k frequence_{echantillon}}{N}`$.
