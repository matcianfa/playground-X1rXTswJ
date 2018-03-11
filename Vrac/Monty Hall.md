# Le paradoxe de Monty Hall
`Difficulté : Moyenne`

Le paradoxe de Monty Hall a pour origine le jeu télévisé dont le principe est le suivant :

+ Soit trois portes, l'une cache une voiture, les deux autres une chèvre. Les prix sont répartis par tirage au sort.
+ Le présentateur connaît la répartition des prix.
+ Le joueur choisit une des portes, mais rien n'est révélé.
+ Le présentateur ouvre une autre porte ne révélant pas la voiture.
+ Le présentateur propose au candidat de changer son choix de porte à ouvrir définitivement.

Petites précisions: Le présentateur n'ouvre jamais la porte devant la voiture, en effet :

+ Si le joueur choisit une porte à chèvre, le présentateur ouvrira la seule autre porte à chèvre.
+ Si le joueur choisit la porte à voiture, le présentateur ouvrira au hasard une des deux portes à chèvre (éventuellement préalablement désignée par tirage au sort).

Dans cet exercice nous allons simuler des parties de ce jeu. Vous devez créer un programme qui simulera le meilleur choix possible pour le candidat.

On numérotera les portes 1, 2 ou 3. Pour simplifier, la première phase du jeu correspondra au numéro 0 donné en entrée. 

Ainsi une partie se déroulera comme suit :
1. En entrée le programme recevra 0 et devra renvoyer un numéro de porte (1, 2 ou 3)
2. En entrée le programme recevra un numéro qui correspond à la porte qui est ouverte par le présentateur et qui cachait une chèvre. Il devra renvoyer un numéro de porte parmi celles qui restent fermées.

::: Aide
+ Vous aurez peut-être besoin de variables globales pour vous souvenir de la porte que vous avez choisie.
+ Vous aurez peut-être besoin de choisir un entier au hasard entre 1 et 3. Pour cela vous pourrez utiliser `randint(1,3)`.
:::

Je vous invite à lire [Wikipédia](https://fr.wikipedia.org/wiki/Probl%C3%A8me_de_Monty_Hall) pour comprendre l'origine du paradoxe et aussi pour trouver quelques indications pour résoudre cet exercice.

> Entrée et Sortie: Le ***numéro*** donné par le présentateur : 
> + 0 pour indiquer que c'est la phase 1 et que vous devez renvoyer (avec `return`) un nombre entre 1 et 3. 
> + 1, 2 ou 3 pour indiquer la porte qui est ouverte. Vous devez renvoyer (avec `return`) un nombre parmi les portes restantes **en utilisant la meilleur stratégie***.

> Pour gagner : De nombreuses parties seront simulées. Vous devez obtenir au final une proportion de parties gagnées d'au moins 0.66. Pour cela, vous devez bien choisir votre stratégie de choix de portes.

@[Paradoxe de Monty Hall]({"stubs": ["Vrac/Monty_Hall.py"], "command": "python3 Vrac/Monty_Hall_Test.py"})



