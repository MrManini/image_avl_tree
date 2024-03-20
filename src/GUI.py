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

        self.graph = graph

        root.geometry("600x500")
        root.title("Laboratorio Arbol AVL")

        label = tk.Label(root, text = "Representación Arbol AVL", anchor = "center", font = ("Courier", 20))
        label.pack(pady = 15)

        pngGraph = tk.PhotoImage(file = PATH)
        labelGraph = tk.Label(image = pngGraph)
        labelGraph.pack(pady = 15)
        
        def InsertNodes(graph: "AVL", label, pngGraph):
            graph.add_some_nodes()
            label.config(image = pngGraph)
            graph.plot()
        
        def DeleteNodes(graph: "AVL", label, pngGraph):
            graph.del_som_nodes()
            label.config(image = pngGraph)
            graph.plot()

        butonInsert = tk.Button(InsertNodes(graph, labelGraph, pngGraph))
        butonInsert.pack(pady = 15)

        butonDelete = tk.Button(DeleteNodes(graph, labelGraph, pngGraph))
        butonDelete.pack(pady = 15)

        root.mainloop()
    
    