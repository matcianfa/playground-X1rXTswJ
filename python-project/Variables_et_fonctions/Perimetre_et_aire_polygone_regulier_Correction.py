def mon_programme(n):
    coté=2*sin(pi/n)
    périmètre= n*coté
    aire=périmètre*cos(pi/n)/2
    print(round(périmètre,2),round(aire,2))
