"""
https://www.codewars.com/kata/56ef9790740d30a7ff000199/train/python

Tree to list

Given root of tree with arbitrary number of children nodes transform data from tree to list. Where data from neighbour nodes in tree located in neighbour position in list.

Example:

       1
      / \
     2   3  -> [1,2,3,4,5,6,7]
    /|\   \
   4 5 6   7

"""

import queue
class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes

def tree_to_list(tree_root):
    q = queue.Queue()
    q.put(tree_root)
    list = []
    while q.qsize():
        node = q.get()
        list.append(node.data)
        if node:
            if node.child_nodes:
                for child in node.child_nodes:
                    q.put(child)
    return list

"""

Sample Tests

Test.assert_equals(tree_to_list(Node(1, [Node(2, [Node(3), Node(4), Node(5)]), Node(3, [Node(7)])])), 
[1, 2, 3, 3, 4, 5, 7])

"""
