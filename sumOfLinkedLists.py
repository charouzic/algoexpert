# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
	firstNumber = getNumber(linkedListOne)
	secondNumber = getNumber(linkedListTwo)
	
	suma = str(firstNumber+secondNumber)
	res = []
	
	for i in suma:
		res.append(i)
	
	reversedSuma = ''.join(reversed(res))
	
	
	head = LinkedList(int(reversedSuma[0]))
	
	node = head
	
	for i in range(1, len(reversedSuma)):
		node.next = LinkedList(int(reversedSuma[i]))
		node = node.next
		
	return head

def getNumber(linkedList):
	number = []
	node = linkedList
	
	while node.next is not None:
		number.append(str(node.value))   
		node = node.next
	# adding the last node value 
	number.append(str(node.value))
	# number = "2471"
	reversedNumber = reversed(number)
	return int(''.join(reversedNumber))

firstHead = LinkedList(2)
firstHead.next = LinkedList(4)
firstHead.next.next = LinkedList(7)
firstHead.next.next.next = LinkedList(1)

secondHead = LinkedList(9)
secondHead.next = LinkedList(4)
secondHead.next.next = LinkedList(5)

sumOfLinkedLists(firstHead, secondHead)
