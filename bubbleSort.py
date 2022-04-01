def bubbleSort(array):
    noSwaps = 1

    while noSwaps > 0:
        noSwaps = 0
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1],array[i]
                noSwaps += 1

    return array

a = [1,10,2,3,5,-1]