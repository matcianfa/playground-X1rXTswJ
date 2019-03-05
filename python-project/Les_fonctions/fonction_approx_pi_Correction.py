def factorielle(n):
    if n==0:
        return 1
    else:
        return n*factorielle(n-1)

def approx_pi(n):
    if n==0:
        return 2
    else:
        return 2*((2**n)*factorielle(n)**2)/factorielle(2*n+1)+approx_pi(n-1)
