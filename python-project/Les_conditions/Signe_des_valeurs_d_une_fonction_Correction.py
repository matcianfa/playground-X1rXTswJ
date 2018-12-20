def ma_fonction(x):
    p=x**2-x-6
    if p>0:
        return 'P(x) strictement positif'
    elif p<0:
        return 'P(x) strictement négatif'
    else :
        return 'P(x) vaut 0'
