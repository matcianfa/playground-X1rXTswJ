# Version avec cache global
# On met dans cache la valeur de fib(i) calculée. On y place déja fib(0) et fib(1)
cache={0:1 , 1:1, 2:1}

def tri_fib(n):
    if n in cache: #Si n est dans le cache, on a déjà calculé la valeur donc on la renvoie directement
        return cache[n]
    else :
        calcul = tri_fib(n-1) + tri_fib(n-2) + tri_fib(n-3) # Je le sauvegarde pour ne pas le calculer 2 fois
        cache[n]=calcul # Je sauvegarde la valeur de fib calculée
        return calcul

# -----------------------------------------------------------------
# Version avec cache local
# -----------------------------------------------------------------
def tri_fib(n,cache={0:1 , 1:1, 2:1}):
    if n in cache: #Si n est dans le cache, on a déjà calculé la valeur donc on la renvoie directement
        return cache[n]
    else :
        calcul = tri_fib(n-1) + tri_fib(n-2) + tri_fib(n-3) # Je le sauvegarde pour ne pas le calculer 2 fois
        cache[n]=calcul # Je sauvegarde la valeur de fib calculée
        return calcul
