def ma_fonction(a,b,c):
    if a+b>=c and a+c>=b and b+c>=a:
        return 'CONSTRUCTIBLE'
    elif a+b==c or a+c==b or b+c==a:
        return 'PLAT'
    else:
        return 'PAS CONSTRUCTIBLE'
