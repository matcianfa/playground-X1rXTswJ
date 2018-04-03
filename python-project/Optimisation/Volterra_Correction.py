a=0.09
b=0.00001
c=0.25
d=0.000005
# Cache pour v dans lequel on met déjà v_0
cache_v={0:9000}

def v(n):
    if n in cache_v : return cache_v[n]
    else:
        calcul=v(n-1)*(1+d*u(n-1)-c)
        cache_v[n]=calcul
        return calcul
        
# Cache pour u dans lequel on met déjà u_0
cache_u={0:53000}

def u(n):
    if n in cache_u: return cache_u[n]
    else:
        calcul=u(n-1)*(1+a-b*v(n-1))
        cache_u[n]=calcul
        return calcul
