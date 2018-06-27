# L'idée est de trouver pour chaque d, le n max (en prenant 3d//7)) qui est en dessous de 3/7.
# et de ne garder en mémoire que celui qui est plus proche que le précédent

approx_max=0
n_max=0
trois_septieme=3/7
for d in range(2,1000001):
    n=(3*d)//7
    temp=n/d
    if  approx_max < temp < trois_septieme:
        approx_max=temp
        n_max=n

        
print(n_max)
