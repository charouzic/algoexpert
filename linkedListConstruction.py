# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# going to the left we access by .prev
# going to the right we access by .next
# head is on the very left of LL
# tail is on the very right of LL

# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        while node.prev is not None:
            node.prev.prev.next = node
            
            node.prev= node.prev.prev
            #node.prev
        pass

    def setTail(self, node):
        # Write your code here.
        pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        if node.next is not None and node.prev is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        # what if it is a head?
        if self.head is node:
            self.setHead(node)
            
        # what if it is a tail?
        if self.tail is node:
            self.setTail(node)
        
        

    def containsNodeWithValue(self, value):
        # Write your code here.
        # aka search
        currNode = self.head
        while currNode is not None and currNode.value != value:
            currNode = currNode.next
                
        if currNode == None:
            return False
        return True
                
