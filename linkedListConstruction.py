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
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)
        # Write your code here.

    def setTail(self, node):
        # Write your code here.
        if self.head is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        
        if node.prev is None:
            self.head = nodeToInsert
            
        else:
            node.prev.next = nodeToInsert
            
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        
        if node.next is None:
            self.tail = nodeToInsert
            
        else:
            node.next.prev = nodeToInsert
            
        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.setHead(nodeToInsert)
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    def remove(self, node):
        # what if it is a head?
        if node == self.head:
            self.head = self.head.next
            
        # what if it is a tail?
        if node == self.tail:
            self.setTail = self.teail.prev
            
        self.updateAndRemoveNodePointers(node)


    def containsNodeWithValue(self, value):
        # Write your code here.
        # aka search
        currNode = self.head
        while currNode is not None and currNode.value != value:
            currNode = currNode.next
                
        return currNode is not None
                
        
    def updateAndRemoveNodePointers(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        
        if node.next is not None: 
            node.next.prev = node.prev
        
        node.prev = None
        node.next = None