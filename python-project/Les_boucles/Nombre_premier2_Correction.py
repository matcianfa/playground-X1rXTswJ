def mon_programme(n):
    if n<2 or (n%2==0 and n!=2):
        print('PAS PREMIER')
    else:
        for d in range(3,int(sqrt(n))+1,2):
            if n%d==0:
                print('PAS PREMIER')
                break
        else:
            print('PREMIER')
