def deriver(f,a,h):
  return (f(a+h/2)-f(a-h/2))/h

def Newton(f,x0,n):
    x = x0
    for i in range(n):
        x = x - f(x)/deriver(f,x,0.000001)
    return x
