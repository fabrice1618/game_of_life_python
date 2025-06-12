# hello_tk.py
import tkinter as tk        # import de la librairie Tkinter

# Création de la fenêtre principale
root = tk.Tk()
root.title("Hello world")  # Titre de la fenêtre

# Création d'un label avec le texte "Hello, World!"
label = tk.Label(root, text="Hello, World!")
label.pack(padx=20, pady=20) # On place (pack) le label avec un peu de marge

# Lancement de la boucle principale : gestion des événements et affichage
root.mainloop()
