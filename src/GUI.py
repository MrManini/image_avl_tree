import tkinter as tk
import graphviz as gv
from avl import Tree, ABB, AVL
from Node import Node
import os
from pathlib import Path
PATH = Path(__file__).parent.parent / "binary_tree1.png"


# Clase UI para crear la interfaz gráfica de TKinter
class UI:

    def InsertNodes(self, graph: "AVL", labelGraph: "tk.Label", pngGraph: "tk.PhotoImage"):
        graph.add_some_nodes()
        graph.plot()
        labelGraph.config(image = pngGraph)
        
    
    def DeleteNodes(self, graph: "AVL", labelGraph: "tk.Label", pngGraph: "tk.PhotoImage"):
        graph.del_som_nodes()
        graph.plot()
        labelGraph.config(image = pngGraph)
    
    def Inorder(self, graph: "AVL"):
        graph.inorder()
    
    def Preorder(self, graph: "AVL"):
        graph.preorder()
    
        
    def __init__(self, graph: "AVL"):
        root = tk.Tk()

        self.graph = graph

        root.geometry("600x500")
        root.title("Laboratorio Arbol AVL")

        label = tk.Label(root, text = "Representación Arbol AVL", anchor = "center", font = ("Courier", 20))
        label.pack(pady = 15)

        pngGraph = tk.PhotoImage(file = PATH)
        labelGraph = tk.Label()
        labelGraph.pack(pady = 15)
        self.label = label
        
        
        butonInsert = tk.Button(command = (lambda: self.InsertNodes(graph, labelGraph, pngGraph)), text = "Insert",)
        butonInsert.pack(pady = 15)

        butonDelete = tk.Button(command = (lambda: self.DeleteNodes(graph, labelGraph, pngGraph)), text = "Delete")
        butonDelete.pack(pady = 15)

        root.mainloop()
    
    