def sortStack(stack):
    # Write your code here.
    # can only use:
        # .pop() ==> poping last element
        # .append() ==> appending on top of the stack
        # peek ==> view the last element
        
    if len(stack) == 1:
        return stack
    
    popedEl = stack.pop()
    
    sortStack(stack)
    
    if popedEl > stack[-1]:
        stack.append(popedEl)
    else:
        peekedEl = stack.pop()
        stack.append(popedEl)
        stack.append(peekedEl)
        
    return stack

stack = [-5, 2, -2, 4, 3, 1]

sortStack(stack)