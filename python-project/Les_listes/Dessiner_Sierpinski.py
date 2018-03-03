import pixel

def dessiner(liste):
  i=len(liste)-1
  for j,element in enumerate(liste):
    if element%2!=0: 
      pixel.marquer(j,i)
