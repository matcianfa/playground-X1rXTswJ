# Calcul des coefficients de Fourier

def coeff_Fourier(s):
    N = s.shape[0]
    a = np.full(N,0.0)
    b = np.full(N,0.0)
    for k in range(N):
        #print("\rCalcul du coefficient {} sur {}".format(k+1,N),end="")
        cosk = np.cos(np.arange(0,N)*2*k*np.pi/N)
        a[k]= np.vdot(s,cosk) # Produit scalaire
        sink = np.sin(np.arange(0,N)*2*k*np.pi/N)
        b[k]= np.vdot(s,sink)
    return a,b
        

# Inverse de la transformée de Fourier
def inv_Fourier(a,b,k_max=None):
    N = a.shape[0]
    if k_max is None:
        k_max = N
    s = np.full(N,0.0)
    for n in range(N):
        #print("\rCalcul du coefficient {} sur {}".format(n+1,N),end="")
        cosk = np.cos(np.arange(0,k_max)*2*n*np.pi/N)
        sink = np.sin(np.arange(0,k_max)*2*n*np.pi/N)
        s[n] = (np.vdot(a[:k_max],cosk)+np.vdot(b[:k_max],sink))/N
    return s

def donner_coefficients_harmoniques(a,b):
    return np.sqrt(a*a + b*b)
