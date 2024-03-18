import os
from typing import Any, List, Optional, Tuple
from pathlib import Path
from Stack import Stack
from Queue import Queue
from Node import Node
PATH = Path(__file__).parent / 'data'

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
            if p is not None and p.type == type and lower_limit < p.size < upper_limit:
                nodes.append(p)
                s.add(p)
                p = p.left
            else:
                p = s.remove()
                p = p.right
        return nodes
    
class AVL(ABB):

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

    def height(self, node: "Node"):
        left_height = 0
        right_height = 0
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
        while p != None and abs(self.balance_factor(p)) < 2:
            son = p
            p = self.search_father(p.data)
        if p != None:
            father = self.search_father(p.data)
            p_factor = self.balance_factor(p)
            if son != None:
                son_factor = self.balance_factor(son)
                if p_factor == 2 and son_factor == 1:
                    correct_node = self.__slr(p)
                elif p_factor == -2 and son_factor == -1:
                    correct_node = self.__srr(p)
                elif p_factor == 2 and son_factor == -1:
                    correct_node = self.__drlr(p)
                elif p_factor == -2 and son_factor == 1:
                    correct_node = self.__dlrr(p)
                else:
                    if son == p.left:
                       daughter = p.right
                    else:
                        daughter = p.left
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
            if father == None:
                self.root = correct_node
            elif father.left == p:
                father.left = correct_node
            else:
                father.right = correct_node


    def delete(self, elem: Any, mode: bool = True) -> bool:
        p, dad = self.search(elem)
        if p is not None:
            if p.left is None and p.right is None:
                if p == dad.left:
                    dad.left = None
                else:
                    dad.right = None
                del p
            elif p.left is not None and p.right is None:
                if p == dad.left:
                    dad.left = p.left
                else:
                    dad.right = p.left
                del p
            elif p.left is None and p.right is not None:
                if p == dad.left:
                    dad.left = p.right
                else:
                    dad.right = p.right
                del p
            else:
                if mode:
                    pred, dad_pred = self.__pred(p)
                    p.data = pred.data
                    if pred.left is not None:
                        if dad_pred == p:
                            dad_pred.left = pred.left
                            dad = dad_pred
                        else:
                            dad_pred.right = pred.left
                    else:
                        if dad_pred == p:
                            dad_pred.left = None
                            dad = dad_pred
                        else:
                            dad_pred.right = None
                    del pred
                else:
                    sus, dad_sus = self.__sus(p)
                    p.data = sus.data
                    if sus.right is not None:
                        if dad_sus == p:
                            dad_sus.right = sus.right
                            dad = dad_sus
                        else:
                            dad_sus.left = sus.right
                    else:
                        if dad_sus == p:
                            dad_sus.right = None
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