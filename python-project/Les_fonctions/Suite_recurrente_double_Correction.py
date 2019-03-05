def u(n):
    if n==0: return 2
    elif n==1: return 1
    else: return 2*u(n-1)+3*u(n-2)
