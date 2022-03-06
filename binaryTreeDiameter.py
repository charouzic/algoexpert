# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
		
class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height

def binaryTreeDiameter(tree):
    # Write your code here.
	
    return getHeightOfTree(tree).diameter

def getHeightOfTree(tree):
	if tree is None:
		return TreeInfo(0,0)
	 
	left = getHeightOfTree(tree.left)
	right = getHeightOfTree(tree.right)
	
	longestCombinedPath = left.height + right.height
	maxDiaSoFar = max(left.diameter, right.diameter)
	
	currDia = max(longestCombinedPath, maxDiaSoFar)
	currHeight = 1 + max(left.height, right.height)
	
	return TreeInfo(currDia, currHeight)
	
	
	
	

