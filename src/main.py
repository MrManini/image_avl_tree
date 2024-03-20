from avl import Tree, ABB, AVL
from Node import Node
import graphviz as gv
from GUI import UI

def main() -> None:
    avl = AVL()
    gui = UI(avl)


if __name__ == '__main__':
    main()