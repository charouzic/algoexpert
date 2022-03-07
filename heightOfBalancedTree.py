# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		
class TreeInfo:
	def __init__(self, isBalanced, height):
		self.isBalanced = isBalanced
		self.height = height


def heightBalancedBinaryTree(tree):
    # Write your code here.
	treeInfo = checkTree(tree)
	
	return treeInfo.isBalanced

def checkTree(tree):
	if tree is None:
		return TreeInfo(True, 0)
	
	leftTree = checkTree(tree.left)
	rightTree = checkTree(tree.right)
	
	
	diff = abs(leftTree.height - rightTree.height)
	
	if leftTree.isBalanced and rightTree.isBalanced and diff < 2:
		return TreeInfo(True, max(leftTree.height, rightTree.height)+1)
	else:
		return TreeInfo(False, 0)
	
## COMPLEXITY:
# time: O(n) where n is the number of nodes in the tree
# space: O(h) where h is the height of the tree