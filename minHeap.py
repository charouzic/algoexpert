# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

		# currentNode = i
		# childOne -> 2i + 1
		# childTwo -> 2i + 2
		
		# parentNode -> floor((i-1)/2) ... round down
    def buildHeap(self, array):
        # Write your code here.
        pass

    def siftDown(self):
        # Write your code here.
		# opposite of siftUp -> we compare both children nodes and swap it with the smaller one out of two 
		# keep in mind that they need to be smaller that the value we sift down
        pass

    def siftUp(self):
        # Write your code here.
		# swapping current node and parent node until it's in the correct position
        pass

    def peek(self):
        # Write your code here.
        pass

    def remove(self):
        # Write your code here.
		# when removing we swap the node we want to remove with the last value and then we just pop the array
		# then we siftDown the value 
        pass

    def insert(self, value, heap):
        # Write your code here.
		heap.append(value)
		
        pass

