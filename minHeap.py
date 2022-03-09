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
        firstParentIdx = (len(array) - 2) // 2
        
        for currIdx in reversed(range(firstParentIdx-1)):
            self.siftDown(array, currIdx, len(array) - 1)
            
        return array

    def _siftDown(self, heap, currIdx, endIdx):
        # Write your code here.
        # opposite of siftUp -> we compare both children nodes and swap it with the smaller one out of two 
        # keep in mind that they need to be smaller that the value we sift down
        
        childOneIdx = 2 * currIdx + 1
        childTwoIdx = 2 * currIdx + 2
        
        while (heap[currIdx] > childOneIdx or heap[currIdx] > childTwoIdx) and currIdx <= endIdx:
            childToSwapIdx = min(childOneIdx, childTwoIdx)
            self.swap(currIdx, childToSwapIdx, heap)
            
            currIdx = childToSwapIdx
            childOneIdx = 2 * currIdx + 1
            childTwoIdx = 2 * currIdx + 2
            
    def siftDown(self, heap, currIdx, endIdx):
        
        childOneIdx = 2 * currIdx + 1
        
        while childOneIdx <= endIdx:
            childTwoIdx = 2 * currIdx + 2 if 2 * currIdx + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
        
            if heap[idxToSwap] < heap[currIdx]:
                self.swap(currIdx, idxToSwap, heap)
                
                currIdx = idxToSwap
                childOneIdx = 2 * currIdx + 1
                
            else:
                break
            

    def siftUp(self, currIdx, heap):
        # Write your code here.
        # swapping current node and parent node until it's in the correct position
        parentIdx = (currIdx-1) // 2
        
        while heap[parentIdx] > heap[currIdx] and currIdx > 0:
            self.swap(parentIdx, currIdx, heap)
            currIdx = parentIdx
            parentIdx = (currIdx-1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
        # Write your code here.
        # when removing we swap the node we want to remove with the last value and then we just pop the array
        # then we siftDown the value 
        self.swap(0, len(self.heap) - 1, self.heap)
        valToRemove = self.heap.pop()
        
        self.siftDown(self.heap, 0, len(self.heap) - 1)
        
        return valToRemove
        

    def insert(self, value):
        # Write your code here.
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]