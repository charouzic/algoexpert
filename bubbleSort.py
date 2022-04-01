def bubbleSort(array):
    noSwaps = 1

    while noSwaps > 0:
        noSwaps = 0
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1],array[i]
                noSwaps += 1

    return array

def bubbleSort_Vlastik(array):
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1],array[i]
                swapped = True

    return array

a = [1,10,1,10,2,3,5,-1]
print(bubbleSort_Vlastik(a))