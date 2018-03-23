def mon_programme(n):
    if n==0:
        print('.')
    else:
        for k in range(n):
            print('.'*(n-k-1)+'^'*(2*k+1)+'.'*(n-k-1))
