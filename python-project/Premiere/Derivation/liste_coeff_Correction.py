def ma_fonction(f,a):
    liste = []
    h = 1
    while h > 0 :
        coeff = (f(a+h)-f(a))/h
        liste.append(coeff)
        h -= 0.001
    return liste
