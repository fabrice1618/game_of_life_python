# Projet : Implémenter le « Jeu de la Vie » en Tkinter

## Contexte

Le **Jeu de la Vie** de John Conway est un automate cellulaire où une grille bidimensionnelle de cellules évolue selon des règles très simples. À chaque « génération », l’état (vivant ou mort) de chaque cellule se détermine en fonction de ses 8 voisins :

1. Une cellule vivante survit si elle a **2 ou 3** voisins vivants, sinon elle meurt (sous-population ou sur-population).  
2. Une cellule morte devient vivante (naissance) si elle a **exactement 3** voisins vivants, sinon elle reste morte.

Pour en savoir plus, consultez :  
- Wikipédia : https://fr.wikipedia.org/wiki/Jeu_de_la_vie  
- Vidéo explicative : https://www.youtube.com/watch?v=S-W0NX97DB0  

## Objectif

Compléter le script Tkinter fourni pour qu’il affiche correctement l’évolution du Jeu de la Vie :

- Écrire une fonction `nouvelle_generation(grid)` qui, à partir de la grille actuelle, calcule et renvoie la grille suivante selon les règles de Conway.  
- (Optionnel) Ajouter une fonction utilitaire pour compter les voisins vivants, gérer le **wrap-around** (bords enroulés) ou ajouter des contrôles de vitesse/pause.

## Fichier à compléter

Sauvegardez le code ci-dessous dans `game_of_life_tk.py` et remplacez le corps de `nouvelle_generation(grid)` par votre implémentation.

```python
# game_of_life_tk.py
import tkinter as tk
import random

# Configuration
WIDTH, HEIGHT = 150, 90    # nombre de cellules horizontalement et verticalement
CELL_SIZE = 10             # taille d'une cellule en pixels
DELAY = 100                # délai entre générations en ms

def nouvelle_generation(grid):
    """
    Calcule la génération suivante selon les règles de Conway.
    À implémenter par vos soins !
    - grid est une liste de listes d'entiers 0 (mort) ou 1 (vivant).
    - Retourner une nouvelle grille de mêmes dimensions.
    """
    # → VOTRE CODE ICI ←
    return grille_aleatoire(WIDTH, HEIGHT)

def grille_aleatoire(w, h):
    """Retourne une matrice h x w remplie aléatoirement de 0 (mort) ou 1 (vivant)."""
    return [[random.choice((0,1)) for _ in range(w)] for _ in range(h)]

def dessiner_grille(canvas, grid):
    """Dessine la grille sur le Canvas : vivant=noir, mort=blanc."""
    canvas.delete("all")
    for i in range(HEIGHT):
        for j in range(WIDTH):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            color = "black" if grid[i][j] else "white"
            canvas.create_rectangle(x1, y1, x2, y2,
                                    fill=color, outline="gray")

def update():
    """Fonction appelée à chaque génération."""
    global grid
    grid = nouvelle_generation(grid)
    dessiner_grille(canvas, grid)
    root.after(DELAY, update)   # replanifie l'appel dans DELAY ms

def restart():
    """Recrée une grille aléatoire et relance l'animation."""
    global grid
    grid = grille_aleatoire(WIDTH, HEIGHT)
    dessiner_grille(canvas, grid)

# --- Initialisation de l'interface ---
root = tk.Tk()
root.title("Jeu de la Vie (Conway)")

canvas = tk.Canvas(root,
                   width=WIDTH*CELL_SIZE,
                   height=HEIGHT*CELL_SIZE,
                   bg="white")
canvas.pack(side="top")

frame = tk.Frame(root)
frame.pack(side="bottom", fill="x")

btn_restart = tk.Button(frame, text="Restart", command=restart)
btn_restart.pack(side="left", padx=5, pady=5)

btn_quit = tk.Button(frame, text="Quitter", command=root.destroy)
btn_quit.pack(side="right", padx=5, pady=5)

# Création et dessin initial de la grille
restart()

# Démarrage de la boucle d'updates
root.after(DELAY, update)

# Lancement de la boucle principale Tkinter
root.mainloop()
```

## À faire

1. Ajouter une fonction (par exemple `compte_voisins(grid, x, y)`) pour compter les voisins vivants de la cellule `(x, y)`.  
2. Implémenter `nouvelle_generation(grid)` :  
   - Pour chaque cellule, compter ses voisins.  
   - Appliquer les règles de Conway pour remplir la nouvelle grille.  
3. Tester votre programme : lancez `python3 game_of_life_tk.py` et vérifiez que l’animation suit bien les règles.

Bon courage !