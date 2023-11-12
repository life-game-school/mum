###############################################################################
# Generate the grid
###############################################################################
from grille_cellule import Grille

grille = Grille(25)
grille.generer()


###############################################################################
# Populate the grid
###############################################################################
from random import shuffle

nombre = int(input("Nombre de cellules vivantes : "))
coordonnees = [(i, j) for i in range(grille.cote) for j in range(grille.cote)]
shuffle(coordonnees)
vivantes = coordonnees[:nombre]

print(vivantes)
grille.modifier(vivantes)


###############################################################################
# Generate the GUI
###############################################################################
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()


###############################################################################
# Display the population, apply life rules and update the GUI
###############################################################################
from interface import jouer_tour

jouer_tour(grille, vivantes, root, canvas)  # lancer le premier tour
root.mainloop()
