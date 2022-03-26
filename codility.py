def solution(A):
    # write your code in Python 3.6
    A.sort()

    counter = 0

    for i in range(1, len(A)):
        if A[i] <= 0:
            continue
        elif A[i]-1 !=  A[i-1] and A[i] != A[i-1]:
            return A[i-1]+1
        counter += 1

    if counter == len(A)-1:
        return A[-1]+1
    else:
        return 1

A = [1, 3, 6, 4, 1, 2]
A2 = [1,2,3]

solution(A2)