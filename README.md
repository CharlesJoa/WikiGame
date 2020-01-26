# WikiGame
Projet python

## installation PIP requise

````
pip install beautifulsoup4

````
## Règles du jeu

````
On peut jouer de différentes façons :️

1) Jeu de base sans option :️

   python wikigame.py

2) Jeu en choisissant la page départ et la page d'arrivée :
️
   python wikigame.py -s page_deb+page_fin

3) Jeu en dirigeant la recherche par portail (2 pages seront tirées au hasard dans ce portail):
️
   python filler.py portail
   python wikigame.py -p 

Exemple : 

1) python wikigame.py

2) python wikigame.py -s toto+titi

3) python filler.py -p jeu
   python wikigame.py -p

````