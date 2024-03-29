import os
import graphviz as gv
from subprocess import check_call
from typing import Any, List, Optional, Tuple
from pathlib import Path
from Stack import Stack
from Queue import Queue
from Node import Node
PATH = Path(__file__).parent / 'data'
PATHIMG = Path(__file__).parent.parent


class Tree:

    def __init__(self, root: "Node" = None) -> None:
        self.root = root

    def preorder(self) -> None:
        self.__preorder_r(self.root)

    def __preorder_r(self, node: "Node") -> None:
        if node is not None:
            print(node.data, end = ' ')
            self.__preorder_r(node.left)
            self.__preorder_r(node.right)

    def preorder_nr(self) -> None:
        p, s = self.root, Stack()
        while p is not None or not s.is_empty():
            if p is not None:
                print(p.data, end = ' ')
                s.add(p)
                p = p.left
            else:
                p = s.remove()
                p = p.right

    def inorder(self) -> None:
        self.__inorder_r(self.root)

    def __inorder_r(self, node: "Node") -> None:
        if node is not None:
            self.__inorder_r(node.left)
            print(node.data, end = ' ')
            self.__inorder_r(node.right)

    def inorder_nr(self) -> None:
        p, s = self.root, Stack()
        while p is not None or not s.is_empty():
            if p is not None:
                s.add(p)
                p = p.left
            else:
                p = s.remove()
                print(p.data, end = ' ')
                p = p.right

    def postorder(self) -> None:
        self.__postorder_r(self.root)

    def __postorder_r(self, node: "Node") -> None:
        if node is not None:
            self.__postorder_r(node.left)
            self.__postorder_r(node.right)
            print(node.data, end = ' ')

    def postorder_nr(self) -> None:
        p, s, s_data = self.root, Stack(), Stack()
        s.add(p)
        while not s.is_empty():
            p = s.remove()
            s_data.add(p.data)
            if p.left is not None:
                s.add(p.left)
            if p.right is not None:
                s.add(p.right)

        while not s_data.is_empty():
            print(s_data.remove(), end = ' ')

    def levels_nr(self) -> None:
        p, q = self.root, Queue()
        q.add(p)
        while not q.is_empty():
            p = q.remove()
            print(p.data, end = ' ')
            if p.left is not None:
                q.add(p.left)
            if p.right is not None:
                q.add(p.right)

    def search_father(self, data_s: Any):
        p, dad = self.root, None
        s, flag = Stack(), False
        while (p is not None or not s.is_empty()) and not flag:
            if p is not None:
                if p.data == data_s:
                    if dad is not None:
                        return dad
                    flag = True
                else:
                    s.add(p)
                    dad = p
                    p = p.left
            else:
                p = s.remove()
                dad = p
                p = p.right
        return None

class ABB(Tree):

    def __init__(self, root: "Node" = None) -> None:
        super().__init__(root)

    def search(self, elem: Any) -> Tuple[Optional["Node"], Optional["Node"]]:
        p, dad = self.root, None
        while p is not None:
            if elem == p.data:
                return p, dad
            elif elem < p.data:
                dad = p
                p = p.left
            else:
                dad = p
                p = p.right
        return p, dad
    
    def search_by_criteria(self, type: str, lower_limit: float, upper_limit: float):
        nodes = []
        p, s = self.root, Stack()
        while p is not None or not s.is_empty():
            if p is not None:
                s.add(p)
                if p.type == type and lower_limit < p.size < upper_limit:
                    nodes.append(p)
                p = p.left
            else:
                p = s.remove()
                p = p.right
            
        return nodes
    
class AVL(ABB):

#Encontrar al nodo predecesor como sucesor dadas las condiciones del arbol AVL
    def __pred(self, node: "Node") -> Tuple["Node", "Node"]:
        p, dad = node.left, node
        while p.right is not None:
            p, dad = p.right, p
        return p, dad

    def __sus(self, node: "Node") -> Tuple["Node", "Node"]:
        p, dad = node.right, node
        while p.left is not None:
            p, dad = p.left, p
        return p, dad
    
#Desarrollo de las rotaciones utilizadas para el balanceo de unu nodo
    def __slr(self, node: "Node"):
        aux = node.right
        node.right = aux.left
        aux.left = node
        return aux

    def __srr(self, node: "Node"):
        aux = node.left
        node.left = aux.right
        aux.right = node
        return aux

    def __drlr(self, node: "Node"):
        node.right = self.__srr(node.right)
        return self.__slr(node)

    def __dlrr(self, node: "Node"):
        node.left = self.__slr(node.left)
        return self.__srr(node)

#Encontrar la altura del arbol
    def height(self, node: "Node"):
        #Inicializamos la altura en 0 
        left_height = 0
        right_height = 0
        # Calcula la altura del subárbol izquierdo del nodo y la asigna a 'left_height'
        if node.left != None:
            left_height = self.height(node.left)
        if node.right != None:
            right_height = self.height(node.right)
        return max(left_height, right_height) + 1

    def level(self, node: "Node"):
        tree_height = self.height(self.root)
        p, q = self.root, Queue()
        q.add((p, 0))
        while not q.is_empty():
            p, lvl = q.remove()
            if node == p:
                return lvl
            if p.left is not None:
                q.add((p.left, lvl+1))
            if p.right is not None:
                q.add((p.right, lvl+1))

    def balance_factor(self, node: "Node"):
        left_height = 0
        if node.left != None:
            left_height = self.height(node.left)
        right_height = 0
        if node.right != None:
            right_height = self.height(node.right)
        return right_height - left_height

    def search_grandpa(self, data_s: Any):
        dad = self.search_father(data_s)
        if dad != None:
            grandpa = self.search_father(dad.data)
            return grandpa
        return None

    def search_uncle(self, data_s: Any):
        dad = self.search_father(data_s)
        grandpa = self.search_grandpa(data_s)
        if grandpa != None:
            if dad == grandpa.left:
                return grandpa.right
            else:
                return grandpa.left

    def __insertion_balance(self, node: "Node"):
        p = self.search_father(node.data)
        while p != None and abs(self.balance_factor(p)) < 2:
            son = p
            p = self.search_father(p.data)
        if p != None:
            father = self.search_father(p.data)
            p_factor = self.balance_factor(p)
            son_factor = self.balance_factor(son)
            if p_factor == 2 and son_factor == 1:
                correct_node = self.__slr(p)
            elif p_factor == -2 and son_factor == -1:
                correct_node = self.__srr(p)
            elif p_factor == 2 and son_factor == -1:
                correct_node = self.__drlr(p)
            else:
                correct_node = self.__dlrr(p)
            if father == None:
                self.root = correct_node
            elif father.left == p:
                father.left = correct_node
            else:
                father.right = correct_node

    def insert(self, elem: Any) -> bool:
        to_insert = Node(elem)
        if self.root is None:
            self.root = to_insert
            return True
        else:
            p, dad = self.search(elem)
            if p is None:
                if elem < dad.data:
                    dad.left = to_insert
                else:
                    dad.right = to_insert
                self.__insertion_balance(to_insert)
                return True
            return False

    def __deletion_balance(self, p: "Node"):
        son = None
        # Mientras el nodo p no sea None y su factor de balance sea menor a 2
        while p != None and abs(self.balance_factor(p)) < 2:
            son = p
            p = self.search_father(p.data)
        if p != None:
            #Calcular el factor de balance del nodo padre 
            father = self.search_father(p.data)
            p_factor = self.balance_factor(p)
            if son != None:
                #Calcular el factor de balanceo de nuestro nodo hijo 
                son_factor = self.balance_factor(son)
                #Dependiendo del valor del factor de balanceo encontrado se ejecuta la rotacion correspondiente
                if p_factor == 2 and son_factor == 1:
                    correct_node = self.__slr(p)
                elif p_factor == -2 and son_factor == -1:
                    correct_node = self.__srr(p)
                elif p_factor == 2 and son_factor == -1:
                    correct_node = self.__drlr(p)
                elif p_factor == -2 and son_factor == 1:
                    correct_node = self.__dlrr(p)
                else:
                    #Si el hijo es el hijo izquierdo del padre 
                    if son == p.left:
                       #Se asigna el hijo derecho de p a la hija 
                       daughter = p.right
                    else:
                        #De no ser asi se asigna el hijo izquierdo del padre a la hija 
                        daughter = p.left
                        #Se calcula el factor de balanceo de la hija y se hace la rotacion correspondiente
                    daughter_factor = self.balance_factor(daughter)
                    if p_factor == 2 and daughter_factor == 1:
                        correct_node = self.__slr(p)
                    elif p_factor == -2 and daughter_factor == -1:
                        correct_node = self.__srr(p)
                    elif p_factor == 2 and daughter_factor == -1:
                        correct_node = self.__drlr(p)
                    else:
                        correct_node = self.__dlrr(p)
            else:
                if p.left == None:
                    child = p.right
                else:
                    child = p.left
                child_factor = self.balance_factor(child)
                if p_factor == 2 and (child_factor == 1 or child_factor == 0):
                    correct_node = self.__slr(p)
                elif p_factor == -2 and (child_factor == -1 or child_factor == 0):
                    correct_node = self.__srr(p)
                elif p_factor == 2 and child_factor == -1:
                    correct_node = self.__drlr(p)
                else:
                    correct_node = self.__dlrr(p)
            #Si el nodo padre es = none considera como p, luego del balanceo aquel que reemplace al nodo padre se considera como la raiz 
            if father == None:
                self.root = correct_node
            elif father.left == p:
                father.left = correct_node
            else:
                father.right = correct_node


    def delete(self, elem: Any, mode: bool = True) -> bool:
        p, dad = self.search(elem)
        if p is not None:
            # Si ambos hijos del nodo 'p' son None (es decir, 'p' es un nodo hoja)
            if p.left is None and p.right is None:
                # Si 'p' es el hijo izquierdo de 'dad'
                if p == dad.left:
                    # Asigna None al hijo izquierdo de 'dad', eliminando la referencia a 'p'
                    dad.left = None
                else:
                    # Si no, asigna None al hijo derecho de 'dad', eliminando la referencia a 'p'
                    dad.right = None
                del p
            elif p.left is not None and p.right is None:
                # Dado el caso de que el nodo 'p' tiene un hijo izquierdo pero no un hijo derecho
                if p == dad.left:
                    dad.left = p.left
                else:
                    dad.right = p.left
                del p
            elif p.left is None and p.right is not None:
                # Dado el caso de que el nodo 'p' tiene un hijo derecho pero no un hijo izquierdo
                if p == dad.left:
                    dad.left = p.right
                else:
                    dad.right = p.right
                del p
            else:
                # Implementacion tanto del metodo de predecesor como sucesor 
                if mode:
                    # Buscar el predecesor del nodo 'p' y su padre
                    pred, dad_pred = self.__pred(p)
                    p.data = pred.data
                    if pred.left is not None:
                        # Asignar el hijo izquierdo del predecesor al hijo izquierdo del padre del predecesor
                        if dad_pred == p:
                            dad_pred.left = pred.left
                            # Asignar el padre del predecesor a 'dad'
                            dad = dad_pred
                        else:
                            dad_pred.right = pred.left
                    else:
                        if dad_pred == p:
                            # Asignar None al hijo izquierdo del padre del predecesor
                            dad_pred.left = None
                            # Asignar el padre del predecesor a 'dad'
                            dad = dad_pred
                        else:
                            dad_pred.right = None
                    del pred
                else:
                    # Buscar el sucesor del nodo 'p' y su padre
                    sus, dad_sus = self.__sus(p)
                    p.data = sus.data
                    if sus.right is not None:
                        if dad_sus == p:
                            # Asignar el hijo derecho del sucesor al hijo derecho del padre del sucesor
                            dad_sus.right = sus.right
                             # Asignar el padre del sucesor a 'dad'
                            dad = dad_sus
                        else:
                            dad_sus.left = sus.right
                    else:
                        if dad_sus == p:
                            # Asignar None al hijo derecho del padre del sucesor
                            dad_sus.right = None
                            # Asignar el padre del sucesor a 'dad'
                            dad = dad_sus
                        else:
                            dad_sus.left = None
                    del sus
            self.__deletion_balance(dad)
            return True
        return 
    
    def levels_r(self) -> None:
        p = self.root
        h = self.height(p)
        for i in range(1, h + 1):
            self.__levels_recursive(p, i)

    def __levels_recursive(self, node, start_height):
        if node is None:
            return
        if start_height == 1:
            print(node.data, end=' ')
        elif start_height > 1:
            self.__levels_recursive(node.left, start_height - 1)
            self.__levels_recursive(node.right, start_height - 1)
    
    # Hace un árbol con todos los nodos
    def add_all_nodes(self):
        for root, dirs, files in os.walk(PATH):
            for file in files:
                self.insert(file)

    # Hace un plot del arbol con graphviz
    def plot(self):
        dot = gv.Digraph()
        dot.node(str(self.root.data))

        # añade los nodos a graphviz
        def addNodes(node):
            if node.left:
                dot.node(str(node.left.data))
                dot.edge(str(node.data), str(node.left.data))
                addNodes(node.left)
            if node.right:
                dot.node(str(node.right.data))
                dot.edge(str(node.data), str(node.right.data))
                addNodes(node.right)

        addNodes(self.root)
        dot.render("binary_tree1", view = True, format = "png", directory= PATHIMG)
        c = 0
        
        #poppler_path = r"C:\Users\pipe\OneDrive\Documentos\Python Addons\poppler-24.02.0\Library\bin"
        #pdf_path = r"C:\Users\pipe\OneDrive\Documentos\Universidad\Uninorte\Semestre 4\Estructura de Datos 2\Laboratorios\image_avl_tree\binary_tree.pdf"
        #imgPath = r"C:\Users\pipe\OneDrive\Documentos\Universidad\Uninorte\Semestre 4\Estructura de Datos 2\Laboratorios\image_avl_tree"

        #pngGraph = convert_from_path(pdf_path = pdf_path, poppler_path = poppler_path)
        #pngGraph[0].save(os.path.join(imgPath, "binary_tree"), "JPEG")
        

    def add_some_nodes(self):
        self.insert("dog.161.jpg")
        self.insert("0129.png")
        self.insert("horse-42.jpg")
        self.insert("bike_107.bmp")
        self.insert("cat.142.jpg")
        self.insert("dog.73.jpg")
        self.insert("rider-107.jpg")
        self.insert("bike_110.bmp")
        self.insert("horse-9.jpg")
        self.insert("carsgraz_177.bmp")
        self.insert("carsgraz_100.bmp")
        self.insert("rider-37.jpg")
        self.insert("cat.72.jpg")
        self.insert("0038.png")
        self.insert("dog.60.jpg")
        self.insert("bike_238.bmp")
        self.insert("horse-198.jpg")
        self.insert("0177.png")
        self.insert("carsgraz_354.bmp")
        self.insert("cat.153.jpg")
        self.insert("carsgraz_127.bmp")
        self.insert("bike_072.bmp")
        self.insert("rider-201.jpg")
        self.insert("rider-125.jpg")
        self.insert("cat.100.jpg")
        self.insert("dog.165.jpg")
        self.insert("horse-139.jpg")
        self.insert("0130.png")

    def del_som_nodes(self):
        self.delete("horse-42.jpg")
        self.delete("dog.161.jpg")
        self.delete("carsgraz_177.bmp")
        self.delete("rider-107.jpg")
        self.delete("cat.142.jpg")

