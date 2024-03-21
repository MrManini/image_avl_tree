from avl import Tree, ABB, AVL
from Node import Node
import graphviz as gv
from GUI import UI

def main() -> None:
    avl = AVL()
    avl.add_some_nodes()
    avl.del_som_nodes()
    avl.plot()
    print("Menu")
    op = 10
    while(op != -1):
        print("0:\t insertar nodo")
        print("1:\t eliminar nodo")
        print("2:\t buscar nodo")
        print("3:\t buscar nodo con filtro")
        print("4:\t preorden")
        print("5:\t inorden")
        print("6:\t postorden")
        print("7:\t niveles")
        print("-1:\t salir")

        nodo = None
        padre = None
        nodos = []
        op = int(input("Escoja operación: "))
        if op == 0:
            nodo_data = input("Ingrese el nombre del nodo a insertar: ")
            avl.insert(nodo_data)
            avl.plot()
        elif op == 1:
            nodo_data = input("Ingrese el nombre del nodo a eliminar: ")
            avl.delete(nodo_data)
            avl.plot()
        elif op == 2:
            nodo_data = input("Ingrese el nombre del nodo a buscar: ")
            nodo, padre = avl.search(nodo_data)
            if nodo != None:
                print(nodo.data)
            else:
                print("no existe este nodo.")
        elif op == 3:
            tipo = input("Ingrese el tipo de imagen: ")
            low = float(input("Ingrese el límite inferior: "))
            high = float(input("Ingrese el límite superior: "))
            nodos = avl.search_by_criteria(tipo, low, high)
            if nodos:
                for nodo in nodos:
                    print(nodo.data)
            else:
                print("Ningún nodo cumple esas características.")
        elif op == 4:
            print("Recorrido en preorden:")
            avl.preorder()
            print(" ")
        elif op == 5:
            print("Recorrido en inorden:")
            avl.inorder()
            print(" ")
        elif op == 6:
            print("Recorrido en postorden:")
            avl.postorder()
            print(" ")
        elif op == 7:
            print("Recorrido por niveles:")
            avl.levels_r()
            print(" ")

        if op == 2 and nodo != None:
            nivel = avl.level(nodo)
            print(f"Nivel: {nivel}")
            balanceo = avl.balance_factor(nodo)
            print(f"Factor de balanceo: {balanceo}")
            if padre != None:
                print(f"Padre: {padre.data}")
            else:
                print("No tiene padre.")
            tio = avl.search_uncle(nodo.data)
            abuelo = avl.search_grandpa(nodo.data)
            if tio != None:
                print(f"Tío: {tio.data}")
            else:
                print("No tiene tío.")
            if abuelo != None:
                print(f"Abuelo: {abuelo.data}")
            else:
                print("No tiene abuelo.")

        if op == 3 and nodos:
            index = int(input("Seleccione el indice de un nodo: "))
            nodoElegido = nodos[index]
            nivel = avl.level(nodoElegido)
            dad = avl.search_father(nodoElegido.data)
            print(f"Nivel: {nivel}")
            balanceo = avl.balance_factor(nodoElegido)
            print(f"Factor de balanceo: {balanceo}")
            if dad != None:
                print(f"Padre: {dad.data}")
            else:
                print("No tiene padre.")
            tio = avl.search_uncle(nodoElegido.data)
            abuelo = avl.search_grandpa(nodoElegido.data)
            if tio != None:
                print(f"Tío: {tio.data}")
            else:
                print("No tiene tío.")
            if abuelo != None:
                print(f"Abuelo: {abuelo.data}")
            else:
                print("No tiene abuelo.")

            


if __name__ == '__main__':
    main()