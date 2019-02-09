# Différents programmes liés à la physique chimie

Cette page et les suivantes ne sont pas des pages d'exercices mais plutôt quelques exemples de programmes qui sont en rapport avec le programme de physique chimie qui pourront servir de modèles pour les enseignants.

### Fonction qui donne le ph

Une version fonctionnelle :

```python
#Donner le pH à  partir de la concentration c=[H30+]
def pH(c):
    return -log10(c)
```

Voici une version plus intéractive :

```python
#Demande la concentration et affiche le ph
def pH():
    c=eval(input("Entrer la concentration : "))
    return -log10(c)

#Pour lancer :
pH()
```

