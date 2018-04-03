# La mémoïzation

La mémoïzation consiste simplement à sauvegarder les résultats renvoyés par une fonction que l'on appelle régulièrement avec les mêmes valeurs.

Prenons l'exemple classique de la suite de Fibonacci. C'est la suite $`F_n`$ de nombres définie par $`F_{n}=F_{n-1}+F_{n-2}`$ et commençant par $`F_{0}=F_{1}=1`$. Une manière naturelle de la programmer est :
``` Python
def fib(n):
    if n<2 : 
        return 1
    else:
        return fib(n-1)+fib(n-2)
```

Cette façon de faire peut sembler satisfaisante mais elle est en réalité extrêmement lente. En effet, voyons comment on calcule fib(4) :
1. Pour avoir fib(4), il faut fib(3) et fib(2).
1. Pour avoir fib(3), il faut fib(2) ( fib(1) on l'a déjà, c'est 1).
1. Pour avoir fib(2) de l'étape 2, on calcule fib(1)+fib(0). On peut donc calculer maintenant fib(3) de l'étape 1
1. Pour avoir fib(2) de l'étape 1, on calcule fib(1)+fib(0). On peut donc maintenant calculer fib(4).

On remarque que fib(2) est calculé 2 fois. On peut se dire que vue la vitesse de calcul d'un ordinateur, ce n'est pas un calcul qui va ralentir beaucoup notre programme. Cependant, si on essaye de calculer des valeurs plus élevées, on va vite se rendre compte qu'on calcule enormément de fois la même chose. Par exemple, si on veut calculer fib(10) :
1. Pour avoir fib(10), il faut fib(9) et fib(8).
1. Pour avoir fib(9), il faut fib(8) et fib(7).
1. Pour avoir fib(8) de l'étape 2, il faut fib(7) et fib(6).
1. Pour avoir fib(8) de l'étape 1, il faut fib(7) et fib(6)...

On voit qu'il faut calculer fib(8) 2 fois, fib(7) 3 fois, fib(6) ca sera 4 fois etc. D'où l'idée de sauvegarder les calculs déjà faits.

### Mise en place

C'est simple, on sauvegarde dans une liste ( ou un dictionnaire selon les cas) les valeurs déjà calculées et dans notre fonction, on commence par regarder si la valeur existe ou pas. Cette liste est souvent appelée cache.

``` python
# On met dans cache[i] la valeur de fib(i) calculée. On y place déja fib(0) et fib(1)
cache=[1,1]

def fib(n):
    if n<len(cache): #Si n est dans le cache, on a déjà calculé la valeur donc on la renvoie directement
        return cache[n]
    else :
        calcul = fib(n-1) + fib(n-2) # Je le sauvegarde pour ne pas le calculer 2 fois
        cache.append(calcul) # Je sauvegarde la valeur de fib calculée
        return calcul
```

J'ai mis un version avec liste car c'est la plus naturelle quand on début en python. Voici une version utilisant les dictionnaires qui est utilisable dans bien plus de situation et finalement, avec l'habitude, beaucoup plus naturelle :

::: Version avec dictionnaire
``` python
# On met dans cache la valeur de fib(i) calculée. On y place déja fib(0) et fib(1)
cache={0:1 , 1:1}

def fib(n):
    if n in cache: #Si n est dans le cache, on a déjà calculé la valeur donc on la renvoie directement
        return cache[n]
    else :
        calcul = fib(n-1) + fib(n-2) # Je le sauvegarde pour ne pas le calculer 2 fois
        cache[n]=calcul # Je sauvegarde la valeur de fib calculée
        return calcul
```
:::

Les versions précédentes utilisent un cache en variable globale. L'avantage est que si vous avez besoin dans une autre fonction de valeurs déjà calculées par fib ou tout simplement d'utiliser plusieurs fois fib par ailleurs, votre cache sera réutilisable. Cependant, utiliser une variable globale peut être une perte de temps si vous n'en avez pas besoin. Voici une autre façon de faire utilisant un cache comme variable locale :

::: Version avec cache local
``` python
def fib(n,cache={0:1 , 1:1}):
    if n in cache: #Si n est dans le cache, on a déjà calculé la valeur donc on la renvoie directement
        return cache[n]
    else :
        calcul = fib(n-1) + fib(n-2) # Je le sauvegarde pour ne pas le calculer 2 fois
        cache[n]=calcul # Je sauvegarde la valeur de fib calculée
        return calcul
```
:::

### Exercice

Pour vous entrainer, programmez ci-dessous avec mémoïzation une fonction ***tri_fib*** qui permet de calculer les termes de la suites $`u_n=u_{n-1}+u_{n-2}+u_{n-3}`$ avec $`u_0=u_1=u_2=1`$.

@[Mémoization tri_fib]({"stubs": ["Optimisation/tri_fib.py"], "command": "python3 Optimisation/tri_fib_Test.py"})
