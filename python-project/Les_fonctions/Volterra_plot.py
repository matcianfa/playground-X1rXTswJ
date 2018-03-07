from functools import lru_cache
#Valeurs minimum et maximum des n représentés. Vous pouvez les modifier
n_min=0
n_max=300
#Copiez collez vos fonctions u et v précédentes ci-dessous:





#Copiez collez vos fonctions u et v au dessus de ces lignes
#Le but des lignes ci-dessous est d'accélérer énormément les calculs. Ne pas y toucher.
u=lru_cache(maxsize=None)(u)
v=lru_cache(maxsize=None)(v)
