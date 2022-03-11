# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	currNode = head.next
	
	length = 1
	
	while currNode.next is not None:
		currNode = currNode.next
		
	currLen = 1
	