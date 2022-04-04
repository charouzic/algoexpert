# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    # Write your code here.
	currNode = head
	previousNode = None
	
	while currNode is not None:
		nextNode = currNode.next
		currNode.next = previousNode
		previousNode = currNode
		currNode = nextNode
		
	return previousNode

## COMPLEXITY
# time: O(n) where n is the number of elements in the linked list
# space: O(1)