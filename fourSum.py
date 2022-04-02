def fourNumberSum(array, targetSum):
    # Write your code here.
    res = []
    arrLen = len(array)
    for first in range(arrLen):
        for second in range(1+first, arrLen):
            for third in range(1+second, arrLen):
                for fourth in range(1+third, arrLen):
                    if (array[first]+array[second]+array[third]+array[fourth]) == targetSum:
                        res.append([array[first],array[second],array[third],array[fourth]])

                            
    return res