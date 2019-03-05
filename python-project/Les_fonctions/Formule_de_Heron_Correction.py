def racine(x):
    def u(n):
        if n==0: return 1
        else: return (u(n-1)+x/u(n-1))/2
    
    return u(5)
