# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    currNode = linkedList
    
    while currNode.next is not None:
        if currNode.value == currNode.next.value:
            if currNode.next.next is not None:
                currNode.next = currNode.next.next
            else:
                currNode.next = None
        
        currNode = currNode.next
        
    return linkedList

