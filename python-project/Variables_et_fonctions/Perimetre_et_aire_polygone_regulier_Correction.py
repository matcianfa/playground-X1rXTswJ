def ma_fonction(n):
    coté=2*sin(pi/n)
    périmètre= n*coté
    aire=périmètre*cos(pi/n)/2
    return (round(périmètre,2),round(aire,2))
