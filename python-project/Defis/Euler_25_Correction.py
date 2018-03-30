# Pour mémoizer rapidement :
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n<3 :
        return 1
    else :
        return fibonacci(n-1)+fibonacci(n-2)

n=1
while fibonacci(n)<10**999:
    n+=1

print(n)
