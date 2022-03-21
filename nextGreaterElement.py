def nextGreaterElement(array):
    # Write your code here.
    result = [] 
    
    arrLen = len(array)

    # brute force
    for i in range(arrLen):
        currValue = array[i]
        
        idx = i + 1
        
        if idx == arrLen:
            idx = 0
            
        while currValue >= array[idx] and idx != i:
            if idx == arrLen-1:
                idx = 0
            else:
                idx += 1
        
        if idx == i:
            result.append(-1)
        else:
            result.append(array[idx])
            
    return result

## COMPLEXITY
# time: O(n^2) where n is the number of elements in the array
# space: O(n)

def _nextGreaterElement(array):
    # Write your code here.
    arrLen = len(array)
    result =  [-1 for _ in range(arrLen)]
    
    stack = []
    
    
    for i in range(2 * arrLen):
        idx = i % arrLen
        
        currentVal = array[idx]
        
        while len(stack) > 0 and array[stack[-1]] < currentVal:
            topOfTheStack = stack.pop()
            result[topOfTheStack] = currentVal
        
        stack.append(idx)
        
    return result

## COMPLEXITY
# time: O(n) where n is the number of elements in the array
# space: O(n)

array = [2, 5, -3, -4, 6, 7, 2]

nextGreaterElement(array)