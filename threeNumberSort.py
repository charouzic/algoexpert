def threeNumberSort(array, order):
    # Write your code here.
    
    # sliding window
    startOfTheWindow = 0
    endOfTheWindow = len(array)
    
    idxToSwap = 0
    
    for number in order:
        
        idxToSwap = startOfTheWindow
        
        for idx in range(startOfTheWindow, endOfTheWindow):
            # 1. check the current value
            if array[idx] == number and idx != idxToSwap:
                swap(array, idxToSwap, idx)
                idxToSwap += 1
        
        startOfTheWindow = idxToSwap	
    
    return array
        
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

array =[-2, -3, -3, -3, -3, -3, -2, -2, -3],
order = [-2, -3, 0]

threeNumberSort(array,order)