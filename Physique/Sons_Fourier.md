# Utilisation de la transformée de Fourier discrète réelle pour récupérer les harmoniques d'un son.

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
  $`= 1*1+2*1+(-1)*1 = 2`$
:::
