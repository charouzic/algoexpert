def sortStack(stack):
    # Write your code here.
    # can only use:
        # .pop() ==> poping last element
        # .append() ==> appending on top of the stack
        # peek ==> view the last element
        
    if len(stack) <= 1:
        return stack
    
    poppedEl = stack.pop()
    
    if poppedEl < stack[-1]:
        poppedEl2 = stack.pop()
        stack.append(poppedEl)
        poppedEl = poppedEl2
        sortStack(stack)
    else:
        sortStack(stack)
    
    if poppedEl > stack[-1]:
        stack.append(poppedEl)
    else:
        peekedEl = stack.pop()
        stack.append(poppedEl)
        stack.append(peekedEl)
        
    return stack


def insertAtSortedPosition(stack, value):
    if len(stack) == 0:
        stack.append(value)
        return stack
    elif stack[-1] > value:
        poppedVal = stack.pop()
        insertAtSortedPosition(stack, value)
        stack.append(poppedVal)
        return stack
    else:
        stack.append(value)
        
    return stack

stack = [3, 4, 5, 1, 2]

sortStack(stack)

print(insertAtSortedPosition(stack, 10))