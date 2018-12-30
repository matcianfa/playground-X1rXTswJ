def ma_fonction(n):
    k=0
    while n%2==0 :
        k+=1
        n//=2
    return (n,k)
