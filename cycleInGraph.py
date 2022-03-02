def cycleInGraph(edges):
    
	noOfNodes = len(edges)
	visited = [False for _ in range(noOfNodes)]
	isStack = [False for _ in range(noOfNodes)]
	
	for node in range(noOfNodes):
		if visited[node]:
			continue
		
		hasCycle = ContainsCycleDFS(edges, node, visited, isStack)
		if hasCycle:
			return True
		
    return False

def ContainsCycleDFS(edges, node, visited, isStack):
	visited[node] = True
	isStack[node] = True
	
	neighbors = edges[node]
	
	for neighbor in neighbors:
		if not visited[neighbor]:
			hasCycle = ContainsCycleDFS(edges, neighbor, visited, isStack)
			if hasCycle:
				return True
		elif isStack[neighbor]:
			return True
		
	isStack[node] = False
	return False

#COMPLEXITY:
#time: O(v + e) where v is the number of nodes/veritces and e is the number of edges
#space: O(v)


