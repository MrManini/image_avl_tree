import tkinter as tk
import graphviz as gv
from avl import Tree, ABB, AVL
from Node import Node
import os
from pathlib import Path
PATH = Path(__file__).parent.parent / 'binary_tree.png'

# Clase UI para crear la interfaz gráfica de TKinter
class UI:
    def __init__(self, graph: "AVL"):
        root = tk.Tk()

        root.geometry("600x500")
        root.title("Laboratorio Arbol AVL")

        label = tk.Label(root, text = "Representación Arbol AVL", anchor = "center", font = ("Courier", 20))
        label.pack(pady = 15)

        pngGraph = tk.PhotoImage(file = PATH)
        labelGraph = tk.Label(image = pngGraph)
        labelGraph.pack(pady = 15)

        root.mainloop()
    
    