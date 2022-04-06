# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currNode = linkedList
    
    while currNode is not None:
        distinctNode = currNode.next
        
        while distinctNode is not None and distinctNode.value == currNode.value:
            distinctNode = distinctNode.next
            
        currNode.next = distinctNode
        currNode = distinctNode
        
    return linkedList

