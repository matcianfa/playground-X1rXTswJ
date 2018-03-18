def mon_programme(k):
    somme=601
    for a in range(-10,10):
        for b in range(-10,10):
            for c in range(-10,10):
                if a*57+b*62+c*72==k and max(0,a)*57+max(0,b)*62+max(0,c)*72<somme:
                    somme=max(0,a)*57+max(0,b)*62+max(0,c)*72
    if somme<601:print(somme)
    else :
        print('Impossible')
