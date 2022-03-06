class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstructBst(preOrderTraversalValues):
	noNodes = len(preOrderTraversalValues)
	if noNodes == 0:
		return None
	
	currVal = preOrderTraversalValues[0]
	
	rightSubTreeRootIdx = noNodes
	
	for idx in range(1, len(preOrderTraversalValues)):
		if preOrderTraversalValues[idx] >= currVal:
			rightSubTreeRootIdx = idx
			break
	
	leftSubtree = reconstructBst(preOrderTraversalValues[1:rightSubTreeRootIdx])
	
	rightSubtree = reconstructBst(preOrderTraversalValues[rightSubTreeRootIdx:])
	
	return BST(currVal, leftSubtree, rightSubtree)
