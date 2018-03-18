def mon_programme(a,b,c):
    if a+b>=c and a+c>=b and b+c>=a:
        print('CONSTRUCTIBLE')
    elif a+b==c or a+c==b or b+c==a:
        print('PLAT')
    else:
        print('PAS CONSTRUCTIBLE')
