# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
	currNode = head
	
	length = 1
	
	while currNode.next is not None:
		length += 1
		currNode = currNode.next
	
	nodeBefore = head
	
	targetLen = length - k
	currLen = 1
	
	if length == k:
		head.value = head.next.value
		head.next = head.next.next
		return
	
	while currLen < targetLen and nodeBefore.next is not None:
		nodeBefore = nodeBefore.next
		currLen += 1
		
	nodeBefore.next = nodeBefore.next.next
	
## COMPLEIXITY:
# time: O(n) where n is the number of elements in the linked list
# space: O(1)

