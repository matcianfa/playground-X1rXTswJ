# Utilisation de la transformée de Fourier discrète réelle pour récupérer les harmoniques d'un son.

Le but de cette page est de voir un peu ce qui se cache derrière des compressions de sons qu'on retrouve dans des formats de sons comme le MP3 par exemple. Elle est déstinée à des lycéens et/ou curieux donc nous présenterons seulement ce qu'est la transformée de Fourier discrète réelle et comment l'implémenter à la main en python pour la voir fonctionner. 

## La théorie

Nous avons vu, page précèdente, qu'un son wave est simplement une suite de données joué à une certaine fréquence. Notons $`N`$ la taille de ces données et $`d_n`$ la donnée d'indice $`n`$. A partir de cette suite de données, on peut en créer 2 qu'on appelle coefficients de Fourier réels  dont les formules sont :
``` math
a_k =\sum_{n=0}^{N-1} d_n cos\left(\dfrac{2\pi kn}{N}\right)
```
et 
```math
b_k =\sum_{n=0}^{N-1} d_n sin\left(\dfrac{2\pi kn}{N}\right)
```

On a alors le miracle suivant : à partir de ces deux suites, on peut retrouver celle de départ par la formule :

```math
d_n = \dfrac 1 N \sum_{k=0}^{N-1} a_k cos\left(\dfrac{2\pi kn}{N}\right) + b_k sin\left(\dfrac{2\pi kn}{N}\right)
```
