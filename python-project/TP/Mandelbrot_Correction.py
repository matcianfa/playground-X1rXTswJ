def Mandelbrot(mu):
    n = 0
    z = 0.5
    while abs(z) < 1000 and n < 200:
        z = mu * z * (1-z)
        n += 1
    return n
