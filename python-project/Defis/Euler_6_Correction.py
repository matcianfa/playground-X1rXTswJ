n=100
somme1=sum([k**2 for k in range(1,n+1)])
somme2=sum([k for k in range(1,n+1)])**2
print(somme2-somme1)
