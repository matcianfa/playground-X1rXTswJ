def ma_fonction(a,b,c):
    if a>0: 
        extremum = "minimum"
    else : 
        extremum = "maximum"
    alpha = -b/(2*a)
    beta = a*alpha*alpha + b*alpha + c
    return "Le polynôme possède un {} qui vaut {}".format( extremum, beta)
    
