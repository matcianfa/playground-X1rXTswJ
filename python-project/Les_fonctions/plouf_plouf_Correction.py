def plouf_plouf(n,k):
    if n==1 : return 0
    else:
        return (plouf_plouf(n-1,k)+k)%n
