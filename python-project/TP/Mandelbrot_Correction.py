def Mandelbrot(mu):
    n = 0
    u = 0.5
    while abs(u) < 1000 and n < 200:
        u = mu * u * (1 - u)
        n += 1
    return n
