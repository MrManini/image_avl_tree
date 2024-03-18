import tkinter as tk
import graphviz as gv
from avl import Tree, ABB, AVL
from Node import Node
    

# Clase UI para crear la interfaz gráfica de TKinter
class UI:
    node = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    avl = AVL(node)
    def __init__(self):
        root = tk.Tk()

        root.geometry("600x500")
        root.title("Laboratorio Arbol AVL")

        label = tk.Label(root, text = "Representación Arbol AVL", anchor = "center", font = ("Courier", 20))
        label.pack(pady = 15)

        root.mainloop()
    
    