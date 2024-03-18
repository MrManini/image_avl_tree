from avl import Tree, ABB, AVL
from Node import Node
import graphviz as gv
from GUI import UI

def main() -> None:
    ui = UI()

    avl = AVL()
    avl.insert("1")
    avl.insert("2")
    avl.insert("3")
    avl.insert("4")
    avl.insert("5")

    avl.plot()


if __name__ == '__main__':
    main()