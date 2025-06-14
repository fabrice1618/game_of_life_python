# Projet : Implémenter le « Jeu de la Vie » en Tkinter

## Contexte

Le **Jeu de la Vie** de John Conway est un automate cellulaire où une grille bidimensionnelle de cellules évolue selon des règles très simples. À chaque « génération », l’état (vivant ou mort) de chaque cellule se détermine en fonction de ses 8 voisins :

1. Une cellule vivante survit si elle a **2 ou 3** voisins vivants, sinon elle meurt (sous-population ou sur-population).  
2. Une cellule morte devient vivante (naissance) si elle a **exactement 3** voisins vivants, sinon elle reste morte.

Pour en savoir plus, consultez :  
- Wikipédia : https://fr.wikipedia.org/wiki/Jeu_de_la_vie  
- Vidéo explicative : https://www.youtube.com/watch?v=S-W0NX97DB0  
- Lenia: https://www.youtube.com/watch?v=PlzV4aJ7iMI

## Objectif

Compléter le script Tkinter fourni pour qu’il affiche correctement l’évolution du Jeu de la Vie :

- Écrire une fonction `nouvelle_generation(grid)` qui, à partir de la grille actuelle, calcule et renvoie la grille suivante selon les règles de Conway.  
- (Optionnel) Ajouter une fonction utilitaire pour compter les voisins vivants, gérer le **wrap-around** (bords enroulés) ou ajouter des contrôles de vitesse/pause.

## Fichier à compléter

Sauvegardez le code `jeu_de_vie_debut.py` dans `jeu_de_la_vie.py` et remplacez le corps de `nouvelle_generation(grid)` par votre implémentation.


## À faire

1. Ajouter une fonction (par exemple `compte_voisins(grid, x, y)`) pour compter les voisins vivants de la cellule `(x, y)`.  
2. Implémenter `nouvelle_generation(grid)` :  
   - Pour chaque cellule, compter ses voisins.  
   - Appliquer les règles de Conway pour remplir la nouvelle grille.  
3. Tester votre programme : lancez `python3 jeu_de_la_vie.py` et vérifiez que l’animation suit bien les règles.
