# game_of_life_tk.py
import tkinter as tk
import random

# Configuration
WIDTH, HEIGHT = 150, 90    # nombre de cellules horizontalement et verticalement
CELL_SIZE = 10            # taille d'une cellule en pixels
DELAY = 100               # délai entre générations en ms


def nouvelle_generation(grid):
    """Calcule la génération suivante selon les règles de Conway."""

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
root.title("Jeu de la Vie (Conway game of life)")

# Canvas dimensionné à la taille de la grille
canvas = tk.Canvas(root,
                   width=WIDTH*CELL_SIZE,
                   height=HEIGHT*CELL_SIZE,
                   bg="white")
canvas.pack(side="top")

# Boutons de contrôle
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
