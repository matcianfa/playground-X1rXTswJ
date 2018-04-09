# Méthode bourrin : On calcule tout et on place au fur et à mesure dans un ensemble qui ne contient par définition aucun doublon
ensemble=set([])
for a in range(2,101):
    for b in range(2,101):
        ensemble.add(a**b)

print(len(ensemble))
