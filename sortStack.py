def sortStack(stack):
    # Write your code here.
    # can only use:
        # .pop() ==> poping last element
        # .append() ==> appending on top of the stack
        # peek ==> view the last element
        
    if len(stack) <= 1:
        return stack
    
    poppedEl = stack.pop()
    
    sortStack(stack)
    
    insertAtSortedPosition(stack, poppedEl)
    
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
    
## COMPLEXITY
# time -> O(n^2) where n is the number of elements in the stack
# space -> O(n) as we need to keep the track of calls to stack