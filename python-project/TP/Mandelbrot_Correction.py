def Mandelbrot(mu):
    n = 0
    z = 0.5
    while abs(z) < 1000 and n < 200:
        z = f(mu,z)
        n += 1
    return n
