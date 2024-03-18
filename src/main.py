from avl import Tree, ABB, AVL
from Node import Node
import graphviz as gv
from GUI import UI

def main() -> None:
    avl = AVL()
    
    avl.insert("bike_001.bmp")
    avl.insert("bike_002.bmp")
    avl.insert("bike_003.bmp")

    avl.plot()


if __name__ == '__main__':
    main()