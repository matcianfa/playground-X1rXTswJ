def ma_fonction(a,b,c):
    if a+b==c or a+c==b or b+c==a:
        return 'PLAT'
    elif a+b>=c and a+c>=b and b+c>=a:
        return 'CONSTRUCTIBLE'
    else:
        return 'PAS CONSTRUCTIBLE'
