def solution(A):
    # write your code in Python 3.6
    # traverse throught the array and have the current sum .... every iteration check if the sum is negative or positive
    # if it is negative, add 1 to the shifts as we need to move the number to the end of the array
    minMaxSum = 0
    negatives = []
    currSum = 0
    relocations = 0

    for number in A:
        currSum += number
        if currSum < 0:
            minMaxSum = min(minMaxSum, currSum)
        if number < 0:
            negatives.append(number)

    negatives.sort()

    while minMaxSum < 0:
        minMaxSum -= negatives.pop(0)
        relocations += 1
        
    
    return relocations

#A = [10,-10,-1,-1,10, -11,11]
A = [-1,-1,-1,-1,-1,5]

print(solution(A))