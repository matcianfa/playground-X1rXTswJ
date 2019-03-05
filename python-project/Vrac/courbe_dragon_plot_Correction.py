import matplotlib.pyplot as plt
#Paramètre modifiable pour tracer la courbe jusqu'à l'étape n_max
n_max=1000000

def pliage(k):
    while k%2==0:
        k//=2
    if k%4==1:
        return "G"
    else :
        return "D"

def ma_fonction(n):
    x=y=direction=0
    l_x=[x]
    l_y=[y]
    for k in range(1,n+1):
        if direction==0:
            x=x+1
        elif direction==90:
            y=y+1
        elif direction==180:
            x=x-1
        else:
            y=y-1
        l_x.append(x)
        l_y.append(y)
        if pliage(k)=="G":
            direction=(direction+90)%360
        else:
            direction=(direction-90)%360
    plt.plot(l_x,l_y,color="black")
    return l_x,l_y
