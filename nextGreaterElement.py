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
            
        while currValue <= array[idx] and idx != i:
            if idx == arrLen-1:
                idx = 0
            else:
                idx += 1
        
        if idx == i:
            result.append(-1)
        else:
            result.append(array[idx])
            
    return result

