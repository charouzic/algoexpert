# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    # Write your code here.
    nodes = inOrderTraversal(tree)

    return nodes

    noNodes = len(nodes)
    
    for i in range(noNodes):
        if nodes[i].value == node and i < noNodes-1:
            return nodes[i+1].value
        
    return None

def inOrderTraversal(tree, array = [] ):
    if tree is None:
        return array
    
    inOrderTraversal(tree.left, array)
    array.append(tree)
    inOrderTraversal(tree.right, array)
    
    return array

